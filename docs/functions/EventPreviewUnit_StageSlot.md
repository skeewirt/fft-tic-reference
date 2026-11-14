# EventPreviewUnit_StageSlot

- **Address:** `0x140214284`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int32_t EventPreviewUnit_StageSlot(int16_t unit_ref)`
- **Callers:** EventScript_Run, case 0xC3 (call site 0x14023E366).
- **Callees:** EventRef_ResolveSlot, ScenePreview_IndexOfSlot, `sub_140103C50`, `sub_1402CBCA0`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a preview-unit slot for a 16-bit reference, copies its 512-byte record into the staging buffer and sets the staged flag.

## Behavior

- V: the argument is a signed 16-bit value. EventScript_Run builds it from the byte at instruction offset 1 (low) and the byte at offset 2 (high), shifted left by 8 and sign-extended.
- I: the value is given to EventRef_ResolveSlot as its reference. The decompiled call shows no argument, and the argument register is not changed before the call, so this is inferred.
- V: when EventRef_ResolveSlot returns 2000 and dword_140782A94 is 281 and the argument is 25, it scans the 21 slots of g_BattleUnitTable for one whose byte +0 is 25. When one is found, it saves that slot's byte +1, writes the slot index into byte +1, sets dword_142FCF86C to 25, and uses that slot. Otherwise no slot is used.
- V: when the resolver returns a value other than 2000, it calls ScenePreview_IndexOfSlot with that value. The slot is used only if the index is 0 to 20.
- V: when a slot is used, it copies 512 bytes from the slot to the staging buffer unk_142FD1390 (four 128-byte blocks) and sets byte_142FCF85F to 1.
- V: it zeroes a 156-byte scratch record (sub_140103C50), then fills it from the slot with sub_1402CBCA0. The dword just after the scratch record is the value it uses as the result.
- V: result = dword_142FCF86C. When the dword after the scratch record is not -1, that value is the result. The result is written back to dword_142FCF86C. When the saved byte +1 is positive, it is restored to the slot. The function returns the result.
- I: the dword after the scratch record is treated as an output of sub_1402CBCA0, which was not checked in full.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md)

## Referenced by

- Called by event opcodes: [0xC3](../opcodes/README.md)

## Notes

The 2000 special case for argument 25 under state 281 is a temporary change to byte +1 of one slot that is undone before return.

## Open questions

What sub_1402CBCA0 writes into the scratch record and its trailing dword, and what consumes the staging buffer (sub_140214404 reads it in EventPreviewUnits_RunFrames).
