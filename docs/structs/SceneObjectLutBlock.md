# SceneObjectLutBlock

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The block of a scene unit object at +960..+979 that sub_14027032C fills from the shape's LUT parameter lookup (CharaRender_LookupLutParams) and two bytes of the CharShape row.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="lut_param_0"></a>`0x3C0` | lut_param_0 | `uint32` | V | First dword of the LUT parameter record the lookup returns (I: a float, the parameter row's first float). |
| <a id="depth_sort_height_offset"></a>`0x3C4` | depth_sort_height_offset | `int8` | V | From the CharShape depth_sort_height_offset column (+0x2D); UnitSprite_DepthSort adds it to the unit's height before the depth value is computed when the object's flag dword +0x15C has the alternate-shape bit. |
| <a id="dead_byte"></a>`0x3C6` | dead_byte | `uint8` | V | From the CharShape +0x2E column; no code reads it (a dead store). |
| <a id="lut_param_2"></a>`0x3C8` | lut_param_2 | `uint32` | V | Dword at +8 of the lookup's record (cfg +8 / +12 floats). |
| <a id="lut_param_3"></a>`0x3CC` | lut_param_3 | `uint32` | V | Dword at +12 of the lookup's record. |
| <a id="lut_short_0"></a>`0x3D0` | lut_short_0 | `uint16` | V | Word at +16 of the lookup's record. |
| <a id="lut_short_1"></a>`0x3D2` | lut_short_1 | `uint16` | V | Word at +18 of the lookup's record. |

## Behavior

- V: sub_14027032C writes the block and caches the inputs (shape key, flag dword, layer value) at +28 / +32 / +30; it is recomputed only when one of them changes.

## Referenced by

- Observed behaviours: [CharShapeDepthSortOffset](../behaviors/CharShapeDepthSortOffset.md)

## Notes

Partial: the block is the part of the scene unit object the LUT lookup fills. Sheets: sub_14027032C, CharaRender_LookupLutParams, UnitSprite_DepthSort.

## Open questions

? the types of the four LUT fields beyond what the lookup copies.
