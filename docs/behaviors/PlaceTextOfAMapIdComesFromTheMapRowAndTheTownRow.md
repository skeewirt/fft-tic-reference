# PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow

- **Kind:** observed behaviour
- **Scope:** engine (battle HUD, save list, title card)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SaveHeader_FillBattleFields](../functions/SaveHeader_FillBattleFields.md), [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md), [EventMapTitle_LoadTexture](../functions/EventMapTitle_LoadTexture.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle's place text reads the place-name id at row +8 of the Map row of variable 51; the save list reads row +12 (else +8) of the Map row of the low byte of the map id for a battle save, and the Town row of the location otherwise; the title card is a picture chosen by variable 51 minus 1.

## Behavior

- V: SaveHeader_FillBattleFields stores variable 49 at header +0x29 and the low byte of the 32-bit battle map id at +0x2C; the resume capture keeps the id as 32 bits.
- I: the save list's place label uses the Map row (table 60) of an 8-bit value for a slot with the battle flag and the Town row (table 52) otherwise; a map id of 256 or more therefore shows the place of its low byte, and a missing Map row gives an empty label.
- I: the battle HUD place text is the PlaceName title of the id at Map row +8, with the map taken from variable 51 when the battle state machine enters state 0x4B.
- V: EventMapTitle_LoadTexture takes variable 51 minus 1 as the index and keeps it when it is 119 or less (signed compare), else 0; the classic path loads maptitle_%03d.tex with it.
- I: with the enhanced flag and graphics level 2.0 or more the scene entry stores the unclamped map id minus 1, and the HD sheet binder uses that index plus 193 as the entry of its fourth slot.

## Notes

The Map data table has ids 0..128 in the shipped data; map ids 127 and 128 have no place id.

## Open questions

? whether the sheet entry of index + 193 exists above map 120; ? that the fourth HD sheet slot is the title card.
