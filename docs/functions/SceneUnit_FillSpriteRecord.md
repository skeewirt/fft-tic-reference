# SceneUnit_FillSpriteRecord

- **Address:** `0x1402C2520`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `bool SceneUnit_FillSpriteRecord(void *obj)`
- **Callers:** sub_1402C2778 (and a function-pointer slot)
- **Callees:** SceneUnit_EntryById, UnitWork_BuildFromSave, Unit_ResolvePreviewShape, SpriteRecord_Fill

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a work record from the selector-scene unit entry named by the object's byte +180 and fills the object's sprite record (+188) with its preview shape.

## Behavior

- V: SceneUnit_EntryById(obj byte +180); null returns false.
- V: sets dword_1437414A0 = 1 and UnitWork_BuildFromSave(work, entry, entry byte +1); a non-zero result returns false.
- V: Unit_ResolvePreviewShape(work, &palette, work job byte +3); the byte answer is widened into r8d at 0x1402C259A.
- V: SpriteRecord_Fill(obj + 188, id, shape, palette, 0, .., slot 6 when the id equals dword_141848B14 else 4, 0); returns true.

## State touched

- Calls: [SceneUnit_EntryById](SceneUnit_EntryById.md), [UnitWork_BuildFromSave](UnitWork_BuildFromSave.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [SpriteRecord_Fill](SpriteRecord_Fill.md)

## Notes

The name is ours (IDB: sub_1402C2520).

## Open questions

? which screen this is.
