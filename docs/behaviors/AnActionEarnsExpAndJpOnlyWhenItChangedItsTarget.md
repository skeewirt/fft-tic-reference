# AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_ApplyActionResult](../functions/Battle_ApplyActionResult.md), [BattleResult_RaiseActionExp](../functions/BattleResult_RaiseActionExp.md), [Battle_AwardUnitJp](../functions/Battle_AwardUnitJp.md), [Unit_AwardJobJp](../functions/Unit_AwardJobJp.md), [Battle_StatusResolve](../functions/Battle_StatusResolve.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The acting unit's EXP for an action is set while each target's result is applied: Battle_ApplyActionResult passes 'did this target change' to BattleResult_RaiseActionExp, which keeps the largest EXP amount in a global byte; Battle_AwardUnitJp later adds that amount and gives JP only when the amount is not 0. A target whose HP, MP, stats, status bytes and status countdowns all stayed the same earns nothing.

## Behavior

- V: Battle_ApplyActionResult keeps a flag for the target (esi at its end): the HP / MP / stat steps set it, and after Battle_StatusResolve it becomes 1 when one of the unit's 5 status bytes (unit +0x61..+0x65) or one of the 16 countdown bytes (+0x66..+0x75) differs from the copy taken before the resolve (loops at 0x14030AA06 and 0x14030AA37). A unit that goes to KO takes the value 2 instead (and its KO count +0x18C rises).
- V: the flag is the argument of the call of BattleResult_RaiseActionExp at 0x14030AA58: with the flag 0 the function does nothing. With 1 the base is 10, with 2 it is 20 divided by the target's KO count; EXP = target level - actor level + base, at least 1, doubled when the actor's byte +0x99 has 0x20, at most 99; the global byte 0x1407B078A keeps the largest amount of the action's targets. A flag that is not 0 also sets the target's byte +0x1BB to 2.
- V: Battle_AwardUnitJp(unit, out) returns at once when the byte 0x1407B078B is 0; else it adds the amount to the unit's EXP (+0x28, capped at 255) and, unless unit +6 has 0x20, gives JP: (level / 4 + 8 + 2 x job level) when the EXP amount is not 0, else 0; a quarter of it to every other unit through Unit_AwardJobJp, and the amount times the play mode's rate (and 1.5 with the JP boost) to the unit itself.
- V (seen live 2026-11-24): a plain attack for 26 damage gave the level 2 attacker 11 EXP and 20 JP (job level 4: 0 + 8 + 8 = 16, rate 130), and 4 JP to each other unit. A status-only hit (formula 56) whose only effect left the 5 status bytes and 16 countdowns unchanged gave 0 EXP and 0 JP: Battle_AwardUnitJp ran and wrote the EXP byte with the same value. With the flag forced to 1 before that call the same hit gave 11 EXP and 20 JP.

## Open questions

? who clears the global EXP byte between actions (BattlePreview_BuildAction writes the word).
