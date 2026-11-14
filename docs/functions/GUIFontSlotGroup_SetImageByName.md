# GUIFontSlotGroup_SetImageByName

- **Address:** `0x1403F3DAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIFontSlotGroup_SetImageByName(GUIFontSlotGroup *g, const char *name, int a3)`
- **Callers:** GuiImage_SetIconById, sub_1403D5934, sub_1403F495C, sub_1403FBE3C
- **Callees:** GUIFontSlots_AcquireImage, UIName_SetKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Acquires the kind-3 image slot for name and stores it as the group's image slot; on failure sets the failed flags.

## Behavior

- V: id = GUIFontSlots_AcquireImage(g_GUIFontSlots, name, a3). id != 0: +84 = id, byte +89 = 0; when the UIName at +8 is empty (id dword +8 == 0) UIName_SetKey(g, name); returns 1.
- V: id == 0: word +88 = 0x0101 (bytes +88 and +89 both 1, the 'failed' flags) and returns the (zero) result.
- V: any previous slot id at +84 is not released here (the caller released via GUIFontSlotGroup_ReleaseAll).

## State touched

- Calls: [GUIFontSlots_AcquireImage](GUIFontSlots_AcquireImage.md), [UIName_SetKey](UIName_SetKey.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Notes

The name is ours (IDB: sub_1403F3DAC).

## Open questions

? the meaning of the two flag bytes +88 / +89 (loaded / failed?).
