# BattleKoCountsAndGreatestContribution

- **Kind:** observed behaviour
- **Scope:** engine (battle results)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [g_BattleControl](../globals/g_BattleControl.md), [BattleAct_NoEffectStep](../functions/BattleAct_NoEffectStep.md), [sub_1402C53F0](../functions/sub_1402C53F0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle counts the KOs each battle record deals, and the victory page's 'Greatest Contribution' names the party unit in records 16..20 with the most.

## Behavior

- V: g_BattleControl +0xA9494 holds 21 dwords, one per battle record. BattleAct_NoEffectStep, for each target left at 0 HP (+0x30) by the action, writes the acting unit's record index (its +0x1BC) to the target's +0x1F5 and adds 1 to the acting record's dword, capped at 9999 (0x140206844..0x140206859).
- V: sub_1402C53F0 picks the top unit among records 16..20 whose slot byte (+1) is not 0xFF: the highest dword (read from +0xA94D4, record 16's), the first of them on a tie; it passes that record's display name (CharaName_GetDisplayName of +0x1FC) and slot byte to sub_1400EB048. A party unit in records 0..15 is not weighed.
- V (seen live, Mandalia random battle): the victory page's panel is titled 'Greatest Contribution' and shows the picked unit's sprite and name. At the first player turn, before any KO, all 21 dwords read 0.

## Open questions

None recorded.
