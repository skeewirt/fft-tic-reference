# UIAgentLifecycle

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

From the manager's construction to its teardown: the 184-byte manager is built once, fills a 54-slot agent vector, attaches addons to agents, ticks them each frame, changes their states, and finally deletes every agent and container in reverse order.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [UIAgentManager_Ctor](../functions/UIAgentManager_Ctor.md) | V | The UI manager constructor sub_1400E1D30 allocates 184 bytes, calls this constructor and stores the result at 0x143CD9DA8. The constructor sets the vtable and allocators, starts the containers empty, allocates the addon map head and calls CreateAgents. |
| <a id="1"></a>1 | [UIAgentManager_CreateAgents](../functions/UIAgentManager_CreateAgents.md) | V | 54 agents are allocated in slot order; each is base-constructed or passed to a named constructor, given its derived vtable and appended to the vector at +16/+24/+32. The manager's init state becomes 1. |
| <a id="2"></a>2 | [UIAgentSlots](../registries/UIAgentSlots.md) | V | The resulting table is UIAgentSlots: one entry per slot with its id, class, vtable, constructor, allocation size and role. The vector index and the registry id are the same number. |
| <a id="3"></a>3 | [UI_FrameUpdate](../functions/UI_FrameUpdate.md) | V | The per-frame path pumps the manager first: sub_1401D1148 advances the init state (requesting font-slot rows from table 24 and waiting until they load) and processes the addon map, then every agent's vtable slot 1 is called in slot order, and sub_1401D144C drains the queued-event vector. |
| <a id="4"></a>4 | [UIAgent_AttachAddon](../functions/UIAgent_AttachAddon.md) | V | A screen addon attaches to its agent, gets an id from the manager's +0x80 counter and is inserted into the addon map at +0x30 under that id. |
| <a id="5"></a>5 | [UIAgent_SetState](../functions/UIAgent_SetState.md) | V | The old state's handler runs with 2, the new state is stored in the control block's +0x18 (agent+0x60), the selector returns the new handler, and that handler runs with 0. |
| <a id="6"></a>6 | [UIAgent_IsActive](../functions/UIAgent_IsActive.md) | V | The active test is the addon list: it compares the addon vector begin at +0x10 with the end at +0x18, so an agent with any addon attached reports active. |
| <a id="7"></a>7 | [UIAgent_DetachAddon](../functions/UIAgent_DetachAddon.md) | V | UIAgent_DetachAddon removes the addon from the agent's list, marks it closing at +0x2C and hides it. The manager's pump processes that flag and, for entries whose +0x2D byte is set, deletes the addon and erases its map node. |
| <a id="8"></a>8 |  | V | Teardown: the UI manager destructor calls the manager's vtable slot 0, sub_1401CF530. It releases the font slots, calls each addon's vtable slot +0x88, deletes the agents in reverse slot order, deletes the addon map values and nodes, frees all three vectors and the map, and clears 0x143CD9DA8. |

## Behavior

- V: the manager is built once, when 0x143CD9DA8 is null; the constructor is the only caller of CreateAgents, and the destructor clears the global.
- V: the agent vector index is the slot id; the 54 slots are contiguous and their order is fixed.
- V: the per-frame order is manager pump (font slots and addons), then every agent's vtable slot 1 in slot order, then the queued-event drain.
- V: teardown releases the font slots first, then notifies the addons, deletes the agents in reverse slot order, deletes the addon map, frees all storage and clears the global.
- V: addons get their id from the manager's +0x80 counter and are inserted into the map at +0x30 under that id.
- V: the per-frame tick calls vtable slot 1 on every vector entry without a null test.
- I: the slot order is a stable interface because screens read fixed indices (rests on the fixed-index reads at slots 1, 3, 4, 5, 6, 37 and 50).
- ?: whether the manager can be rebuilt after teardown (the constructor only runs when the global is null; no second construction path was found).
- ?: what happens after an allocation left a null agent slot.

## Notes

Read: the two manager functions, the manager destructor and deleting destructor, the frame pump, the event drain, the addon attach and detach pages, and the existing UIAgentCursor, UIAgentFFTOTitle and UIAgentFFTOSystem pages. The flow stops at the manager boundary; addon loading and screen internals belong to ScreenAddonCreation and the screen pages. The UIAgentSlots registry, UIAgent_SetState and UIAgent_IsActive are linked from the steps.

## Open questions

Whether the manager can be rebuilt after teardown; what a null agent slot does to the frame tick. The manager global 0x143CD9DA8 has no reference record.
