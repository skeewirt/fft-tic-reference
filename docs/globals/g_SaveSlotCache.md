# g_SaveSlotCache

- **Kind:** global
- **Address:** `0x142C8B970`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `uint8[2008200]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The fifty-slot image in memory: 50 records of 0x9CE4 bytes, the same bytes the PNG container carries. The slot screens read and write this cache, and the frame step copies it to and from the manager image.

## Behavior

- V: the image-to-cache step moves 0x1EA488 bytes; the clear step fills it with 0xFF.

## Referenced by

- Read by: [sub_1402185A4](../functions/sub_1402185A4.md), [sub_14021A030](../functions/sub_14021A030.md), [sub_14021BD04](../functions/sub_14021BD04.md), [sub_14021C620](../functions/sub_14021C620.md)
- Written by: [sub_1402185A4](../functions/sub_1402185A4.md), [sub_140218C04](../functions/sub_140218C04.md), [sub_14021A030](../functions/sub_14021A030.md), [sub_14021AEC0](../functions/sub_14021AEC0.md), [sub_140245C84](../functions/sub_140245C84.md)

## Open questions

None recorded.
