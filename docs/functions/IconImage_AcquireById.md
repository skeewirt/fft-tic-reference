# IconImage_AcquireById

- **Address:** `0x1403DB6B8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void IconImage_AcquireById(void *out, int iconId)`
- **Callers:** GUITextNode_PlaceIcon
- **Callees:** sub_1403DB420, sub_1403DB5B4, sub_1403DB140, GUIFontSlots_AcquireImage

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the image of an icon id.

## Behavior

- V: maps icon ids 50..71 (pad icons) and 1100..1265 to other image sets first (sub_1403DB420, sub_1403DB5B4); other ids take the path of IconPath_FromIconId and load it with GUIFontSlots_AcquireImage.

## State touched

- Calls: [GUIFontSlots_AcquireImage](GUIFontSlots_AcquireImage.md)

## Notes

Name is ours.

## Open questions

None recorded.
