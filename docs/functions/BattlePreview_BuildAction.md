# BattlePreview_BuildAction

- **Address:** `0x140282234`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattlePreview_BuildAction(const void *unit)`
- **Callers:** sub_14028198C, Battle_PreviewUnitAction, sub_140282E38, Battle_ResolveReaction
- **Callees:** AbilityAction_GetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the battle preview block for the action a unit is about to take: the preview word, the ability or item id, the target and the flags the cursor and forecast read.

## Behavior

- V: it sets the preview word at 0x1407B0762 to 1 and clears the neighbouring words before reading the unit.
- V: the unit action command byte is at +0x1A1 and the action word at +0x1A2.
- V: the command kind comes from 0x14067E010; kind 2 takes the item id from unit +0x1A8 and returns early.
- V: for the other kinds it reads the ability id and calls AbilityAction_GetRecord to get the action record flags.
- V: the unit hand words at +0x20 and +0x24 are written into the preview block when they are not 0xFF and not above the marker.
- V: the ability id 0x165 is special-cased before the record lookup.
- V: the preview block fields at 0x1407B0764 through 0x1407B0790 are written with the record range, area, vertical and element bytes.
- I: the block is the forecast/cursor preview rather than the committed action, because the callers include the preview and reaction paths.
- ?: the meaning of the 0x165 special case; the record is fetched but the branch is not documented.
- V (2026-11-10): the 0x165 test is on id 357 and sits at 0x140282306 (the ability word at +0x1A2 compared before the record lookup); id 357 also has a test in Battle_ResolveAction (it skips the clear of the weapon or item word), so only ability 357 gets either special case.

## State touched

- Calls: [AbilityAction_GetRecord](AbilityAction_GetRecord.md)

## Referenced by

- Called by: [Battle_PreviewUnitAction](Battle_PreviewUnitAction.md), [Battle_ResolveReaction](Battle_ResolveReaction.md)
- Observed behaviours: [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Whole function read (626 bytes). The preview globals are the action preview block of the targeting code.

## Open questions

None recorded.
