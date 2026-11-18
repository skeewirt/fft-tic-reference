# BattleUnitTableListsEnemyRowsThatAreNotOnTheField

- **Kind:** observed behaviour
- **Scope:** engine (battle unit table, random battle start)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

In a random battle the unit table holds up to nine enemy rows from the start, but only the rows with the slot byte (+0x01) equal to their own slot and the on-field byte (+0x1B5) equal to 1 stand on the field; the others keep stale tiles (several rows on one tile) and take no part. A battle can also start with no enemy row on the field and end at once in victory.

## Behavior

- V (seen live, Mandalia Plain random battles): at the first turn, enemy rows 1, 6 and 7 had +0x01 = their slot and +0x1B5 = 1 in one battle (three enemies moved in the enemy phase); in others only one row (+0x1B5 = 1) or none; the remaining rows read +0x01 = 0xFF with +0x1B5 = 0 or 0xFF and tiles (9, 12), (2, 11), (0, 2) shared by two rows each.
- V (seen live): killing the one on-field enemy ended the battle with the victory page although the other rows still had full hit points; so the battle-end test counts on-field enemies, not rows.
- V (seen live, 4 of about 14 random battles on one map): the victory page ('The enemy is vanquished', spoils 0) appeared about 10 s after Commence with no turn played, the table then showing no enemy row on the field; the same map id in the other battles had one to three enemies on the field. ? the rule that decides the count (random roll, or a condition at the start); it did not follow the Move-Find row, the load path or the map id in the tests made.

## Notes

Read the field state from +0x01 and +0x1B5, never from the tile or the hit points of a row.

## Open questions

? the rule that gives a random battle zero enemies on the field.
