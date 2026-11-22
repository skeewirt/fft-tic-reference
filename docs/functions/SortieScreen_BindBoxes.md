# SortieScreen_BindBoxes

- **Address:** `0x140145AC8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SortieScreen_BindBoxes(UIAddonFFTOBattleSortie2 *screen)`
- **Callers:** the UIAddonFFTOBattleSortie2 vtable (no direct call)
- **Callees:** Str_Format, UIName_Key, GUINode_FindDescendant, sub_140409240, GUINode_FindPartByName, sub_140146DA8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds the deployment screen's layout: among its steps, the portrait column's boxes by name (T<area>_<position>) with their faces' Eye and Mouth parts.

## Behavior

- V: for area 1..2 and position 1..5 it formats the name `T%02d_%d` (T01_1..T01_5, T02_1..T02_5), finds the node under the screen's root (+0x48) with GUINode_FindDescendant and stores it at +0x310 + 0x18 x (area - 1) + 0x30 x (position - 1); when found, the node's 'Face' reference (sub_140409240) and that face's parts 'Eye' and 'Mouth' (kind 2) go to the next two qwords (0 when missing).
- V: the stock layout (ffto_battle_sortie_ver02.uib, component Team) has T01_1..T01_5 and T02_1..T02_4: T02_5 binds as 0.
- V: after the loop it calls sub_140146DA8 (the screen's reset).

## State touched

- Calls: [Str_Format](Str_Format.md), [UIName_Key](UIName_Key.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md)

## Referenced by

- Observed behaviours: [DeploymentPortraitColumnBoxes](../behaviors/DeploymentPortraitColumnBoxes.md)

## Notes

Only the box binding part was read.

## Open questions

None recorded.
