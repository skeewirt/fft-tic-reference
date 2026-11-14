# SceneUnit_RunPlacement

- **Address:** `0x140269074`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_RunPlacement(uint8_t *node, int32_t offset_sel, int32_t flag)`
- **Callers:** EventScript_Run (opcode 0x97 path, see findings), EventSubScript_RunTask (EventSubScript_RunTask), sub_1401009E8, sub_140269330, sub_14026A1DC.
- **Callees:** SceneVar_Read, sub_1402F7594, sub_1402F78A4, SceneUnit_BuildPalette, SceneUnit_SetFlag12C (not read)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the placement setup for one scene object record, using the record's bytes 8 to 11 to choose a table entry and a position table.

## Behavior

- V: reads the record bytes +8 (slot), +9 (table index), +10 (selector) and +11 (sub-index).
- V: chooses a table pointer from unk_140D005A0 at 13014 bytes per entry indexed by byte +9, choosing one of two sub-regions by testing the byte at entry offset +1 against a set of values.
- V: calls sub_1402F7594 with a buffer, the count 10 and the slot byte.
- V: the second argument selects a base offset: 0 gives 0, 1 gives -4, 2 gives -8, 3 gives -12; other values give 0.
- V: reads SceneVar 35 and 36 (both are tested against the bits of dword_140D3A830 first) and selects offsets for three values from the results.
- V: when the selector byte +10 is 0x9B, 0x9C, 0x9D or 0x9E it uses base offsets 320, 0, 160 or 512 plus 32 times byte +11, and calls sub_1402F78A4 with these, the slot, and the third argument as the last value.
- V: for any other selector it calls SceneUnit_BuildPalette and SceneUnit_SetFlag12C on the node, then calls sub_1402F78A4 with another base.
- V: the function does not wait.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [sub_1402F7594](sub_1402F7594.md), [SceneUnit_BuildPalette](SceneUnit_BuildPalette.md), [SceneUnit_SetFlag12C](SceneUnit_SetFlag12C.md)

## Referenced by

- Called by: [SceneUnit_ApplyStatusTint](SceneUnit_ApplyStatusTint.md), [SceneUnit_SyncSpriteFromPool](SceneUnit_SyncSpriteFromPool.md)
- Called by event opcodes: [0x97](../opcodes/README.md)
- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

This pass decoded only the structure of the routine; the meaning of the table entries and the arguments of sub_1402F78A4 are not established.

## Open questions

What the two sub-regions and the 13014-byte entries hold; what sub_1402F78A4 does with its base offsets.
