# SceneObjects_StepStates

- **Address:** `0x14026E194`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SceneObjects_StepStates(void)`
- **Callers:** CharaPalette_ReloadForShape, sub_140207880, sub_14020BCF0, sub_14020CC50, sub_14020DC78, sub_14020E174, sub_140210AF0
- **Callees:** sub_14026CAA4, sub_140266180, sub_140266288, sub_1402F7C20, SceneUnit_SetFlag156, SceneUnit_Release

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-update pass over the drawn units: runs three per-unit helpers and, for a unit whose two state bits read 'gone', takes it off the field and releases its drawing.

## Behavior

- V: for each node of g_SceneObjectList: sub_14026CAA4; sub_140266180 unless a byte at +27 of its third block is 45 or 49 (masked compare); sub_140266288 when a flag byte is set.
- V: state bits (byte +60 of its eighth block, bits 4..5): value 1 -> becomes 2 and starts a screen-tint step (sub_1402F7C20(4, 4, slot, -31, -31, -31)); value 2 -> unless the unit is the one dword_140CF873C names (SceneUnit_SetFlag156 for it), sets both bits, writes 0xFF to its battle record's slot byte and 0x80 to its on-field byte (when the slot byte was not already 0xFF), and calls SceneUnit_Release.
- I: the state value 2 is a unit vanishing from the field (the step that frees its drawing slot and, when unshared, its look).

## State touched

- Calls: [SceneUnit_SetFlag156](SceneUnit_SetFlag156.md), [SceneUnit_Release](SceneUnit_Release.md)

## Open questions

? which game events set the state to 1 or 2 (KO, crystal, chest, leaving).
