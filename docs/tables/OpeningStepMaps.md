# OpeningStepMaps

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071F118`
- **Rows:** 40 rows of 1 bytes
- **Keyed by:** opening scene step
- **Read by:** [Opening_LoadMessageSprites](../functions/Opening_LoadMessageSprites.md)
- **Row layout:** [OpeningStepMapsRow](../structs/OpeningStepMapsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Byte step maps of the opening sequence plus three resource path strings (the title texture and two message texture files). Verdict: designer-data.

## Behavior

- V: readers use displacements 0x118, 0x120, 0x130, 0x140, 0x14C and 0x154; the 0xC8-byte object ends in text paths and a small value list
- V: sub_14037BDC4 (opening / credits page step): reads the byte maps at +0x00, +0x08, +0x18, +0x28, +0x34 and +0x3C by page number
- V: Opening_LoadMessageSprites and sub_140380020 use the three resource path strings that follow the maps at +0x48

## Notes

Our names. Tags: V readers, ? maps.

## Open questions

- ?: what the six maps select
- ?: the trailing value list (5, 10, 20, 35, 60, 75, 90, 95)
