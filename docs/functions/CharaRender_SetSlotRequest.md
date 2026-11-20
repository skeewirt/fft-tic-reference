# CharaRender_SetSlotRequest

- **Address:** `0x1400EDAE0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `char CharaRender_SetSlotRequest(CharaRenderMgr *m, SlotRecord *r)`
- **Callers:** CharaRender_RegisterSlot and about nine screen builders (sub_1401199CC, sub_14011BF0C, sub_14011C940, sub_14012FC6C, sub_140132DC8, sub_140132E1C, sub_14014386C, ...)
- **Callees:** CharaSlot_SetParams, CharaRender_PlaceSlotImage, sub_1400CC52C (release slot), sub_1400CCAF8 (clear entry)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes one unit-preview request (slot id, shape, palette, pose, flags) into the global unit renderer's 92-byte slot entry and restarts its animation when the request changed.

## Behavior

- V: slot id r[0] <= 0xFF; the renderer is qword_143CC96B8, its slot array at +148144 (92 bytes each: +16 live flag, +24 id, +28 shape).
- V: shape 0x9B/0x9D/0x9E are special (a8 = 96 / 48, pose 42) and shapes flagged in byte table unk_140673302 turn pose 6/7 into 12/13; otherwise r[6] is the pose/animation id (V: tree records carry 2: SpriteRecord_Fill derives it from word_140672D7A[0]).
- V: forwards (palette r.u16[4], r.u16[5], r[5], r[3] flags, r.b[28], r.b[29], a8, pose) to CharaSlot_SetParams, then repositions the slot image with CharaRender_PlaceSlotImage.

## State touched

- Calls: [CharaSlot_SetParams](CharaSlot_SetParams.md), [CharaRender_PlaceSlotImage](CharaRender_PlaceSlotImage.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)

## Referenced by

- Called by: [CharaRender_RegisterSlot](CharaRender_RegisterSlot.md), [JobChangeAddon_SetState](JobChangeAddon_SetState.md), [sub_140132DC8](sub_140132DC8.md), [sub_140132E1C](sub_140132E1C.md)
- Observed behaviours: [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md), [UnitFigureRenderSlotNumbers](../behaviors/UnitFigureRenderSlotNumbers.md)
- Reads tables: [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Open questions

Meaning of pose 2 is not decoded: the empirical best frame is type1 frame 2 (docs/reference/sprites.md).
