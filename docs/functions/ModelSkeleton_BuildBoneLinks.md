# ModelSkeleton_BuildBoneLinks

- **Address:** `0x1403BD428`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `unsigned short *ModelSkeleton_BuildBoneLinks(struct ModelObject *model)`
- **Callers:** the model resource set-up code
- **Callees:** strcmp, strstr, the model allocator

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the list of bone links of a loaded model by matching its bone names against the 33 bone name pairs.

## Behavior

- V: the bone count comes from the model's skeleton resource (or its override object at +1168); the list at +1184 is reset to empty and a 35-entry scratch array of 12-byte records (two bone indices, a flag byte) is cleared to all ones (the decompilation shows -1 for each 16-bit field; 0xFFFF as unsigned).
- V: for every bone name of the model, compares it with both names of each of the 33 pairs of exe.model.bone_link_pairs; a match stores the bone index in the first or second half of the pair's scratch record and the flag byte, which is set when the bone name contains 'spine'.
- V: when the model's file name contains 'c1001' or 'c1002', the flag byte of two of the scratch records is set as well.
- V: every scratch record with both bone indices found is appended to the model's link list (12 bytes per entry, grown through the model's allocator).

## Referenced by

- Reads tables: [BoneLinkPairs](../tables/BoneLinkPairs.md)

## Notes

Name is ours. The link list is stored on the model object; its use is not decoded.

## Open questions

?: what consumes the link list.
