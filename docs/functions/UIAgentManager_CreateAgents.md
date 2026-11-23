# UIAgentManager_CreateAgents

- **Address:** `0x1401CF724`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *UIAgentManager_CreateAgents(ffto::Game::UI::UIAgentModule *self)`
- **Callers:** UIAgentManager_Ctor (0x1401CF4C8)
- **Callees:** Mem_Alloc, sub_1401D14F4, sub_140031D7C, UIAgentFFTOTitle_Ctor, sub_140113830, sub_14013EE98, sub_140151678, sub_140156E78, UIAgentFFTOSystem_Ctor, sub_140182B38, sub_1401B43DC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The one-shot agent factory: allocates and constructs 54 UI agents in a fixed slot order, appends each pointer to the manager's agent vector and marks the manager ready. The vector index is the slot id that the rest of the UI code uses to reach a screen.

## Behavior

- V: performs 54 allocations, one per slot, from the allocator at 0x143CDAA80 +8 with 8-byte alignment; the sizes run from 72 to 2,704 bytes. The per-slot size, vtable, constructor and role table belongs to the UIAgentSlots registry, not to this page.
- V: 46 slots are built inline: Mem_Alloc, the base constructor sub_1401D14F4, a derived vtable store and the derived fields' initial values.
- V: 8 slots go through a named constructor: 6 UIAgentFFTOTitle_Ctor, 11 sub_140113830, 18 sub_14013EE98, 19 sub_140151678, 20 sub_140156E78, 37 UIAgentFFTOSystem_Ctor, 38 sub_140182B38 and 48 sub_1401B43DC.
- V: appends each pointer at the vector end (+24) and advances the end by 8 when the end is below the capacity (+32); when the vector is full it calls sub_140031D7C, which allocates a larger buffer through the allocator at +8, copies the old pointers, frees the old buffer and returns the insertion address.
- V: the order is fixed and contiguous from slot 0 UIAgentFade to slot 53 UIAgentFFTOSubquest; there is no gap and no duplicate. The last allocation is the slot 53 pointer.
- V: the key slots named in the IDB comment match the vtables: 3 UIAgentFFTOStartup, 5 UIAgentFFTOLauncher, 6 UIAgentFFTOTitle, 19 UIAgentAnnounce and 51 UIAgentFFTOOpCredit. Slot 37 UIAgentFFTOSystem is also confirmed by a fixed-index reader.
- V: the vector index is the slot id. Other code reaches the same agents by index, as offsets from the vector begin: slot 1 at +8 (cursor), slot 6 at +48 (title), slot 37 at +296 (system) and slot 50 at +400.
- V: every allocation-failure branch stores a null pointer and still appends it, so the vector keeps 54 entries even when an allocation fails.
- V: sets +176 to 1 at the end, the manager's first init state (agents created).
- I: returns the value of its last call (the append helper on the grow path, otherwise the base constructor's return); the constructor ignores it.
- I: the fixed order is an interface, not an implementation detail: several screens read their agent by a hard-coded index, so changing the order would change those readers (rests on the fixed-index reads above).
- ?: whether a named constructor can fail after its allocation succeeded, and what a consumer does with a null slot.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [UIAgentFFTOSystem_Ctor](UIAgentFFTOSystem_Ctor.md)

## Referenced by

- Appears in flows: [UIAgentLifecycle](../flows/UIAgentLifecycle.md)
- Called by: [UIAgentManager_Ctor](UIAgentManager_Ctor.md)
- Resolves registries: [UIAgentSlots](../registries/UIAgentSlots.md)

## Notes

Whole 6,568-byte function read; all 54 allocations counted and matched against the pre-extracted slot table. The eight named constructors keep their IDB names except UIAgentFFTOTitle_Ctor and UIAgentFFTOSystem_Ctor. The 54-entry detail is not duplicated here; it belongs to UIAgentSlots. Addresses are build-specific.

## Open questions

The UIAgentSlots registry is the place for the per-slot role text. Whether any consumer guards against a null slot is still open. The manager global 0x143CD9DA8 has no reference record.
