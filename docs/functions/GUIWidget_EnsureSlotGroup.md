# GUIWidget_EnsureSlotGroup

- **Address:** `0x1403FBE3C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIWidget_EnsureSlotGroup(GUIWidget *w, const char *name, char addRef)`
- **Callers:** JobTreePanel_SetTextKey and about 34 UI addon methods (sub_14010824C, sub_140108828, sub_140109134, ... each with one texture / part name), sub_1403DC7BC, sub_1403DC8D0, UIAddonFFTOTitlePlaymode_vfunc_14
- **Callees:** UIName_Key, GUIWidget_FindResourceByName, Str_Format, sub_1403D8D1C, sub_1403DA4C0, GUIWidget_NewSlotGroup, sub_1403F3DAC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes sure the widget owns a texture slot group called `name` (a UI texture atlas) and starts loading its '<name without the first 17 characters>.utexpt' part table when it is new; with addRef set an existing group gets one more reference on its part-table slot.

## Behavior

- V: name == null returns 0. Otherwise key = UIName_Key(name); group = GUIWidget_FindResourceByName(w, key) (the group vector w+224); the key's interned id is released when it has one.
- V: path = Str_Format(buf[256], "%s.utexpt", name + 17): the first 17 characters of the name are skipped (what they are is not shown here).
- V (found): when addRef != 0 sub_1403DA4C0(g_GUIFontSlots, group+84) adds one reference to the group's part-table slot; returns 1.
- V (new): group = GUIWidget_NewSlotGroup(w, name); when it is null returns 0; otherwise sub_1403F3DAC(group, path) requests the part-table file (sets group+84 to the new slot id, group+89 = 0 and names the group when still unnamed; a failed request sets +88 = +89 = 1) and returns 1.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUIWidget_FindResourceByName](GUIWidget_FindResourceByName.md), [Str_Format](Str_Format.md), [GUIWidget_NewSlotGroup](GUIWidget_NewSlotGroup.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md), [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [FaceWidget_SetFace](FaceWidget_SetFace.md), [SortieScreen_SetArea0Face](SortieScreen_SetArea0Face.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [sub_1401560D0](sub_1401560D0.md)

## Notes

The name is ours (IDB: sub_1403FBE3C). Job Tree: JobTreePanel_SetTextKey calls it (addRef 0) with the new text key before it sets the name board's key, so changing a panel's key can trigger the load of a texture atlas named by that key. The sheet GUIWidget_FindResourceByName and this one agree on the group name key layout {char *, id}.

## Open questions

? the 17-character prefix (a fixed resource path prefix?). ? which names the 35 callers pass.
