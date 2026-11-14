# BarTop_Setup

- **Address:** `0x14019F330`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void BarTop_Setup(UIAddonFFTOBarTop *self)`
- **Callers:** (virtual: UIAddonFFTOBarTop vtable 0x14070C998, entry 4)
- **Callees:** GUIWidget_FindFirstKind1Component2, UIName_Key, GUINode_FindDescendant, UIName_ReleaseKey, UserSituation_IsMet, sub_1402AC520, sub_1402ABCE4, sub_1402AC8E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up the tavern's top menu (rumors, errands): the errand row is open only when situation 3220 holds.

## Behavior

- V: finds the BarTop node of the addon's widget, asks UserSituation_IsMet(3220) and builds the menu with sub_1402AC520 (3 when it holds, else 7, and 23).
- V: when it does not hold it also calls sub_1402ABCE4 on the menu; then selects the first row (sub_1402AC8E8 with text 1840).

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [UIName_Key](UIName_Key.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Referenced by

- Observed behaviours: [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)

## Notes

Name is ours (was sub_14019F330). I: the 3 / 7 argument and sub_1402ABCE4 lock the errand row ("???" on screen before Chapter 2, owner).

## Open questions

? what sub_1402AC520's 3 / 7 argument selects.
