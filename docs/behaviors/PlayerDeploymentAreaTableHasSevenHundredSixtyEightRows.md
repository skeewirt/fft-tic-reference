# PlayerDeploymentAreaTableHasSevenHundredSixtyEightRows

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The origin of the player's deployment grid comes from a 12-byte-row table of 768 rows in the executable (row number in the u16 at +10), indexed by the deployment area ids in variables 53 and 54 with no bound check; the EntryArea data table adds the slot list of the same id.

## Behavior

- I: the table starts at 0x1407AE2D0; the u16 at +10 of every row equals its own row number, 0..767.
- I: the area id read from variable 53 + i (i below variable 52) is multiplied by 12 with no comparison with the table size; bytes +4 and +5 are the origin tile, +6 the height layer, +7 packs an orientation and a size nibble.
- I: the EntryArea rows of the same id (key2 = slot, up to 25 read) give one byte per slot; a 5 x 5 grid of slots is built around the origin and oriented by +7.
- V (data): stock area ids lie in 256..722; random battles use 513..569.

## Notes

The table is not in the table census yet.

## Open questions

? the meaning of the first dword of a row and of bytes +8 and +9.
