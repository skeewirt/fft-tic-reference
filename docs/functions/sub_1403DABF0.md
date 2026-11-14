# sub_1403DABF0

- **Address:** `0x1403DABF0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void sub_1403DABF0(GUIFontSlots *slots, const SlotRec32 *rec)`
- **Callers:** sub_1403D9C14, sub_1403D9EE0
- **Callees:** Str_Format, UIName_Key, GUIWidget_FindResourceByName, sub_1403D8D1C, sub_1403FBB20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Unloads the texture-part resource of a kind-2 record: builds its name from the UITextureParts scheme prefix (the word UITextureParts, a colon, two slashes), finds the resource in the owning widget and unregisters it.

## Behavior

- V: only when the owner widget pointer qword slots+432 != 0. name = *(*(rec + 0) + 24) or Str; Str_Format(buf, 256, the UITextureParts scheme prefix followed by %s, name); the last 7 characters are cut off (buf[len - 7] = 0); UIName_Key(&n, buf); res = GUIWidget_FindResourceByName(widget, &n); the name reference is released (sub_1403D8D1C); res non-null: sub_1403FBB20(widget, res) removes it from the widget's resource list (erases the pointer at widget+224..232 and calls sub_1403FECD0).

## State touched

- Calls: [Str_Format](Str_Format.md), [UIName_Key](UIName_Key.md), [GUIWidget_FindResourceByName](GUIWidget_FindResourceByName.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

Name unknown. The 7 stripped characters are presumably a file extension (I); the format string uses the same UITextureParts scheme prefix as sub_1403DC8D0.

## Open questions

? which extension the 7 characters are.
