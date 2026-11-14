# Effect_PatchPolygonSeams

- **Address:** `0x140381834`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Effect_PatchPolygonSeams(int64 prim)`
- **Callers:** sub_140380878
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Nudges the texture coordinates of a few primitives of five stock effects by one or two units, keyed by the effect number.

## Behavior

- V: it compares word_141D330BC with 65, 71, 73, 451 and 485 and does nothing for any other number.
- V: for each of those it first checks that the primitive count (byte +3) and the original coordinate bytes have the stock values, then writes changed bytes; a primitive that does not match is left alone.

## Notes

Name is ours. I: these are hand fixes for the Enhanced renderer (texture seams); the matching of stock coordinates means only the stock primitives are touched.

## Open questions

? the primitive layout (+3 count, +4..+7 coordinates).
