# Guide_TryAutoShow

- **Address:** `0x1400D6DAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Guide_TryAutoShow(int id)`
- **Callers:** not recorded
- **Callees:** Guide_GetEntry, UserSituation_IsMet, sub_1400DA454, sub_1400EDFBC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The entry point that shows a guide automatically when the game reaches its moment.

## Behavior

- V: the guide is shown (sub_1400DA454 then sub_1400EDFBC) when seen_bit (+0x2A) is 0, or when the guide is not yet unlocked and user_situation_2 (+0x1C) is 0 or met.
- V: about 47 callers across battle, shop, world map and menus.

## State touched

- Calls: [Guide_GetEntry](Guide_GetEntry.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Referenced by

- Called by: [EventMenu_NodeListTask](EventMenu_NodeListTask.md), [UISaveLoad_StateEnter](UISaveLoad_StateEnter.md)
- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
