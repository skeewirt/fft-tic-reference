# BattleHudAndUnitFields

- **Kind:** observed behaviour
- **Scope:** the Jobs screen and a battle's first turn
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUICore_GetFocus](../functions/GUICore_GetFocus.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What the game shows from the Jobs screen into a battle, as seen live.

## Behavior

- V (live): in the Siedge Weald battle Ramza's battle unit (unit table slot 16) has job byte 76 (0x4C), the Knight job. The battle HUD names his job 'Knight' with the Knight icon, Lv. 8 and 3004 JP, which is the Knight job's progress. HP is 77/77, MP 12/12.
- V (live): the command menu is Move, Abilities, Wait, Status, Auto-battle; the Abilities list has Attack (description 'Attacks with the equipped weapon, or bare fists if no weapon is equipped.', under a Knight heading). The move range was 54 tiles from tile (3, 5).
- V (live): after moving to (5, 5) the first command row reads 'Reset Move' and turn.acted is 1; Abilities > Attack with the cursor on the enemy at (5, 4) (yellow target tiles (5,4), (6,5), (5,6)) opens an attack confirm screen (footer 'Confirm'); A took the enemy (unit slot 4, job byte 171, 70 HP) to 44 HP: 26 damage from a normal attack at level 20.
- V (live): the tile record byte +3 holds a half step in bit 0 and the water depth in bits 5 to 7 (the HUD's 'Submerged N'); tile (5, 5) of this map has byte +2 = 0 and +3 = 0x20, HUD 'Height 1', 'Submerged 1'.
- V (live): the battle opening plays a dialogue event (Argath, Delita, Ramza lines, one speech box each, advanced with A); the pause overlay during it offers only 'Esc Resume', no skip, and holding Space did nothing; the scene-kind line stays 'in-engine cutscene, event 31' after the dialogue has ended and the HUD is up, so it is not an end-of-event signal.
- V (live): a guest unit's turn (Argath, team 0) reports player_turn true with no command menu and a footer of 'Pause Battle', 'Next', 'Status' ...; a command menu means one of the player's own units has the turn (corrected 2026-11-08: every party member gets it, not only Ramza; guests never do).
- V (live, 2026-11-05): battle slot 16 job byte 76, save unit 0 job byte 0x4C, Knight job level 8 = the HUD's Lv. 8.
- V (live, 2026-11-05): unit +0x05 and +0x1EE held the same byte in all 21 slots (guests 0x84, Ramza 0x0B, enemies 0x90, empty 0): +0x05 bits 4-5 is the current team and +0x1EE the original one (Charmed changes only +0x05, BattleStatuses). Bit 7 of +0x05 is set on the guests and enemies only (I: units acting on their own).

## Notes

Unit table fields used: +5 flags (team in bits 4-5), +79/+80 tile, +0x30 HP, +3 job (g_BattleUnitTable, stride 512).

## Open questions

? Which battle HUD reader turns the job byte into the label and icon. ? Whether +0x05 bit 7 means AI-controlled (one battle seen).
