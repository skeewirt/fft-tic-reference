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
- V (seen live 2026-11-23, trace): opening the Warriors' Guild recruit list calls it once per candidate, entry ids 0..14 in order, each from the candidate record 0x1408E6CB0 + 564 * id with save index byte +1 = 13 (the first free record); the shapes passed to SpriteRecord_Fill were 0x60 / 0x61 (the male / female Squire). At 0x1402C259A edx still holds the entry id (byte +180 of the object).
- V (seen live): reopening the list from the guild menu does not rebuild the figures; leaving the guild and entering again does.

## State touched

- Calls: [SceneUnit_EntryById](SceneUnit_EntryById.md), [UnitWork_BuildFromSave](UnitWork_BuildFromSave.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [SpriteRecord_Fill](SpriteRecord_Fill.md)

## Notes

The name is ours (IDB: sub_1402C2520).

## Open questions

? the other selector scenes it draws (scene ids 21, 44, 51).
