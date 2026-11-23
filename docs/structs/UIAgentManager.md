# UIAgentManager

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 184 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The singleton UI agent manager (IDB class UIAgentModule): a 184-byte module object that owns the 54-agent vector, the addon map, the queued-event vector and the font-slot vector. Screen code reaches agents by vector index (the slot id), and addons by the id counter at +0x80.

## Fields

| Offset | Field | Type | Conf | Meaning | Indexed by registries |
|---|---|---|---|---|---|
| <a id="module_vtable"></a>0x00 | module_vtable | `void *` | V | The module vtable 0x140713280; its first slot is the deleting destructor sub_1401CF4DC, which frees this 184-byte object through the allocator that created it. |  |
| <a id="allocator"></a>0x08 | allocator | `void *` | V | Allocator for the agent vector's storage; copied from the service global at 0x143CDAA80 +32. |  |
| <a id="agents_begin"></a>0x10 | agents_begin | `void **` | V | Agent vector begin: 8-byte pointers, one per slot; element N is slot N. | [UIAgentSlots](../registries/UIAgentSlots.md) |
| <a id="agents_end"></a>0x18 | agents_end | `void **` | V | Agent vector end; CreateAgents appends 54 pointers here. | [UIAgentSlots](../registries/UIAgentSlots.md) |
| <a id="agents_capacity"></a>0x20 | agents_capacity | `void **` | V | Agent vector storage end; a full vector grows through sub_140031D7C. |  |
| <a id="addon_map_allocator"></a>0x28 | addon_map_allocator | `void *` | V | Allocator for the addon map's 48-byte head and nodes; same source as +0x08. |  |
| <a id="addon_map_head"></a>0x30 | addon_map_head | `void *` | V | Head of the ordered addon map; AttachAddon inserts a node keyed by the addon id at node +0x20 and stores the addon pointer at +0x28. |  |
| <a id="addon_map_size"></a>0x38 | addon_map_size | `uint64` | V | Number of addons in the map; the map insert keeps it. |  |
| <a id="event_callback"></a>0x40 | event_callback | `void *` | V | Callback called by the queued-event drain sub_1401D144C once per 24-byte entry. |  |
| <a id="event_context"></a>0x48 | event_context | `void *` | V | First argument passed to the event callback. |  |
| <a id="event_arg"></a>0x50 | event_arg | `byte[16]` | V | 16-byte block passed to the event callback as its second argument; cleared at construction. |  |
| <a id="events_allocator"></a>0x60 | events_allocator | `void *` | V | Allocator for the queued-event vector. |  |
| <a id="events_begin"></a>0x68 | events_begin | `void *` | V | Queued-event vector begin; entries are 24 bytes and are pushed by sub_1401D1650. |  |
| <a id="events_end"></a>0x70 | events_end | `void *` | V | Queued-event vector end. |  |
| <a id="events_capacity"></a>0x78 | events_capacity | `void *` | V | Queued-event vector storage end. |  |
| <a id="next_addon_id"></a>0x80 | next_addon_id | `uint32` | V | Counter for addon ids: AttachAddon increments it, stores the value at the addon's +0x20, and wraps to 1 after -1. |  |
| <a id="font_allocator"></a>0x88 | font_allocator | `void *` | V | Allocator for the font-slot vector. |  |
| <a id="font_slots_begin"></a>0x90 | font_slots_begin | `uint64 *` | V | Font-slot vector begin; 8-byte entries whose low 32 bits are a font-slot id. |  |
| <a id="font_slots_end"></a>0x98 | font_slots_end | `uint64 *` | V | Font-slot vector end. |  |
| <a id="font_slots_capacity"></a>0xA0 | font_slots_capacity | `uint64 *` | V | Font-slot vector storage end. |  |
| <a id="font_slots_state"></a>0xA8 | font_slots_state | `uint8` | V | Font-slot request state: 0 none, 1 requests pending, 2 all requested slots loaded; set by sub_1400F4E24 and sub_1400F4F20 and cleared by sub_1400F4EC4. |  |
| <a id="init_state"></a>0xB0 | init_state | `uint32` | V | Manager init state: 0 constructed, 1 agents created (set by CreateAgents), 2 font-slot requests made, 3 ready; the per-frame pump sub_1401D1148 advances it. |  |

## Behavior

- V: constructed by UIAgentManager_Ctor and stored at 0x143CD9DA8 by the UI manager constructor sub_1400E1D30; the allocation is 184 bytes and the caller clears all of them before the constructor runs.
- V: CreateAgents fills the agent vector with 54 slots in a fixed order and sets init_state to 1.
- V: the per-frame pump sub_1401D1148 advances init_state, requests font slots from table 24 and processes the addon map; UI_FrameUpdate then ticks every agent in slot order and drains the event queue.
- V: the destructor sub_1401CF530 releases the font slots, calls each addon's vtable slot +0x88, deletes the agents in reverse slot order, deletes the addon map values and nodes, frees the three vectors and the map, and clears 0x143CD9DA8.
- I: the three vector groups plus the addon map are the manager's whole mutable state; the scalar fields only track ids and states (rests on the constructor, destructor and frame pump covering every field).
- ?: who installs event_callback and what the event_arg block carries; what happens if an agent slot is null.

## Notes

Read: UIAgentManager_Ctor, UIAgentManager_CreateAgents, the manager destructor sub_1401CF530 and deleting destructor sub_1401CF4DC, the frame pump sub_1401D1148, the event drain sub_1401D144C, UIAgent_AttachAddon and the existing UIAgentCursor, UIAgentFFTOTitle and UIAgentFFTOSystem pages. The addon map is an ordered map keyed by addon id; its head and nodes are 48 bytes. Field names are project names.

## Open questions

The manager global 0x143CD9DA8 has no reference record. Who installs event_callback (+0x40) and what the 16-byte event_arg (+0x50) carries. What a null agent slot means to consumers.
