# FaceNumber_Remap

- **Address:** `0x1400F8338`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int FaceNumber_Remap(int face)`
- **Callers:** FaceWidget_SetFace, sub_14010ABE4, sub_1401389C4, sub_140144E24, sub_140147D94, sub_1401480D4
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Replaces a few face numbers by the face the UI shows for them; every other number passes unchanged.

## Behavior

- V: 17 -> 23, 18 -> 26, 20 and 44 -> 48, 22 -> 34, 30 -> 52, 40 -> 195, 41 -> 25, 42 -> 47, 45 -> 58, 46 -> 59, 51 -> 175, 53 -> 99, 54 -> 107, 55 -> 108, 56 -> 118.
- V: 57 and 87 to 92 -> 96; 61 -> 100, 63 -> 102, 66 -> 108, 68 -> 111, 70 -> 118, 71 -> 113; 152 -> 148; 205 -> 72.
- V: every other value, including any number above 205, is returned as it is.

## Referenced by

- Appears in flows: [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md)
- Called by: [FaceWidget_SetFace](FaceWidget_SetFace.md)

## Notes

So a class's own face number (256 or more) passes through unchanged. The name is ours (IDB: sub_1400F8338).

## Open questions

None recorded.
