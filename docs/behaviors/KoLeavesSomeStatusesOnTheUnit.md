# KoLeavesSomeStatusesOnTheUnit

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_StatusApply](../functions/Battle_StatusApply.md), [BTurn_OnTurnStartStatus](../functions/BTurn_OnTurnStartStatus.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

KO does not end every status: its property row (status 2) cancels the action states 4..7, Confusion, Vampire, Float, Invisibility, Berserk, Critical and every status 23..39, and leaves Undead, Stone, Traitor, Blindness, Silence, Oil, Reraise, Chicken and Toad on a KO'd unit. Reraise acts on the KO'd unit at its next turn.

## Behavior

- V (live 2026-11-12, Mandalia): a Squire with Reraise was KO'd by an attack (+0x61 held KO 0x20 of byte 0 and Reraise 0x20 of byte 2, the applied set only KO); at her next turn she revived with 4 HP (41 / 10) and the Reraise was used up (no longer applied, Reraise bit clear).
- V (data): g_StatusPropertyTable row 2 bytes +6..+10 (data/tables/exe_status.jsonl id 2: cancels 4, 5, 6, 7, 11, 13, 17, 19, 20, 23..39).
- V (code read): Battle_StatusApply copies the applied status's cancels into the pending remove before it sets the bit, so applying KO removes those statuses.
- V (code read): BTurn_OnTurnStartStatus revives a unit that is KO, not Undead and has Reraise: heal max HP / 10 (at least 1), KO and Reraise into the pending remove.

## Open questions

None recorded.
