# CharShapeRowsANewLookNeeds

- **Kind:** observed behaviour
- **Scope:** engine (sprite rows in the NXD data)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [CharShape_ApplyClut](../functions/CharShape_ApplyClut.md), [NxdRegistry_Find](../functions/NxdRegistry_Find.md), [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md), [sub_14026EB74](../functions/sub_14026EB74.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The CharShape rows (NXD table 174, keyed by look number) end at key 158 and twelve functions look a look up there.

## Behavior

- V: CharaRender_LookupLutParams (menu renderer: shadow size and LUT region rows) takes the key as an unsigned 32-bit value; CharShape_ApplyClut (the palette colour override, called by CharaPalette_LoadClassic on the menu path) takes it as a byte, so a look of 256 or more reaches it truncated.
- V: a missing row is a null return in every lookup; sub_140216EB4 (battle formation) turns a null entry into a null row pointer and then reads byte +0x2C of it (0x140217172), a fault.

## Open questions

None recorded.
