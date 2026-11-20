# CharShapeDepthSortOffset

- **Kind:** observed behaviour
- **Scope:** engine (unit sprites)
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Affects:** [sub_14027032C](../functions/sub_14027032C.md), [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md), [UnitSprite_DepthSort](../functions/UnitSprite_DepthSort.md), [SceneObjectLutBlock](../structs/SceneObjectLutBlock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

CharShape +0x2D is a signed byte added to the unit's height coordinate before the sprite depth value is computed; +0x2E is copied into the scene object and read by nothing.

## Behavior

- V: CharaRender_LookupLutParams returns row byte +45 as output byte +3 and row byte +46 as output byte +20; sub_14027032C stores them at scene object +964 and +966.
- V: UnitSprite_DepthSort adds the signed byte at +964 to the height component before the depth sum, only when the object's flag dword +0x15C has the alternate-shape bit.
- V: the same flag chooses the _2 columns of the CharShape row for the shadow size and the LUT parameter record.
- V: no reader of the byte at +966 was found.

## Open questions

None recorded.
