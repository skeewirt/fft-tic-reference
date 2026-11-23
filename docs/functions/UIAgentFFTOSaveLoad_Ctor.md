# UIAgentFFTOSaveLoad_Ctor

- **Address:** `0x140182B38`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIAgentFFTOSaveLoad *__fastcall UIAgentFFTOSaveLoad_Ctor(UIAgentFFTOSaveLoad *agent)`
- **Callers:** UIAgentManager_CreateAgents (0x1401D092B)
- **Callees:** sub_1401D14F4 (base constructor), sub_140010FF8 (six-record initialiser)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the save/load UI agent: the base agent front, its vtable, two embedded state machines, five 264-byte summary slots, the embedded save-data handler and the lock and queue that carry save errors back to the screen.

## Behavior

- V: runs the base agent constructor `sub_1401D14F4` first (vtable, allocator at +8, empty add-on vector at +16/+24/+32) and then overwrites the vtable with `0x14070DE48`; the object is 1592 bytes.
- V: zeroes the mode dword at +64.
- V: state block A at +72 is owner +72 = the agent, handler +80 = the no-op guard `0x1400103E0`, selector +88 = `0x140182D04`, state +96 = 0. Block B at +104 is owner +104 = the agent, handler +112 = the same guard, selector +120 = `0x140182D14`, state +128 = 0.
- V: selector `0x140182D04` returns `off_14070DEA0[state]`; that table starts at the vtable + 0x58, so agent state n runs vtable slot 11 + n. Selector `0x140182D14` returns `off_14070DE88[state]`; that table starts at the vtable + 0x40, so dialog state n runs vtable slot 8 + n. Neither selector bounds-checks the state.
- V: zeroes the qword at +136, which clears the descriptor/auto-refresh index at +136 and the situation value at +140 that the save state passes to the slot writer. The in-game save opener `sub_140182DF8` stores its second argument there and sets mode bit 0.
- V: stores the UI module's allocator (`qword_143CDAA80` + 32, or 0 when the module is absent) at +144 and allocates a 24-byte list sentinel from it at +152; the count at +160 is zero, so the queue starts empty.
- V: places the embedded `UISaveDataHandler` at +168 (vtable `0x14070DF80`), zeroes the dword at +176 and initialises the critical section at +184. The handler pointer is stored at `g_SaveRequestManager` + 88.
- V: initialises +224 to 0 (a 32-bit flag the prompt callback clears with an interlocked exchange), +228 to -1 (the selected slot), the qword at +232 to 23 (so +232 = 23 and +236 = 0), +240 to 0 and +244 to 0 (the checkpoint/auto flag).
- V: the five 264-byte summary descriptors start at +256 and fill +256..+1575. Each descriptor's six 32-byte records at +68..+259 are initialised through `sub_140010FF8` with the element initialiser `sub_1400B7330`: dword -1, word at +28 = -1, and qwords at +4/+12/+20 = 0 in each record. The list later copies those six records into its 240-byte entries.
- V: zeroes the list-addon pointer at +1576 and the saving-overlay pointer at +1584; those are the last fields before the 1592-byte end.
- I: the +152 list carries the queued save errors that the update drains, resting on the 24-byte node size and on the pop loop in `sub_140182F68`.
- ?: what sets the +224 flag to a non-zero value; only the clear in the prompt callback was found.
- ?: what the initial +232 value 23 means beyond being the sentinel that state 10 treats as "no wait".

## State touched

- Reads: [g_SaveRequestManager](../globals/g_SaveRequestManager.md)
- Writes: [g_SaveRequestManager](../globals/g_SaveRequestManager.md)

## Referenced by

- Resolves registries: [UISaveLoadDialogStates](../registries/UISaveLoadDialogStates.md), [UISaveLoadStates](../registries/UISaveLoadStates.md)

## Notes

Whole function read (457 bytes). The two selectors are tiny table reads; their table bases are vtable + 0x58 and vtable + 0x40. The descriptor initialiser covers six records per descriptor, not only the first, so descriptor +68 is the first preview record and not a separate serializer. The overlay pointer at +1584 is created later, in state 1, as an 80-byte `UIAddonSaving`; this constructor only clears the pointer. `UIAgentBase` and `UIAgent_SetState` cover the base front and the state protocol.

## Open questions

? what sets +224; ? what the precheck in `sub_1400C480C` tests before it queues the AUTOENHANCED save; ? which situation values the in-game opener passes in +140.
