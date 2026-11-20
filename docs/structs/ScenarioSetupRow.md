# ScenarioSetupRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the ScenarioSetup table: the scene setup of one story event, keyed by the event number; read field by field by ScenarioSetup_ApplyRecord (scene variables) and turned into the per-event word.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="event_id"></a>`0x0` | event_id | `int16` | V | event number (scene variable 39), read sign-extended; the searches stop at the first row whose number is 0, so 1..32,767 |
| <a id="map"></a>`0x2` | map | `int8` | V | battle map id, written to scene variable 51 (a negative byte is stored as its low byte, so 0..255); event 93 keeps the current variable 51 instead |
| <a id="weather"></a>`0x3` | weather | `uint8` | V | low nibble (mask 0x0F): weather level 0..4 -> scene variable 35 (skipped for map 32 in the resume case). Stock: 0 on 594 rows, 1 on 47, 2 on 33, 3 on 25, 4 on 14. Uses: see ScenarioWeatherLevelAndNightFlag |
| <a id="map_state"></a>`0x3` | map_state | `uint8` | V | high nibble (mask 0xF0): map state 0..15 -> scene variable 48 (stock 0 on 691 rows, 1 on 20, 2 on 2). Only the Map row variation selector and the mesh set read it: see ScenarioMapStateIsOnlyAMapVariationSelector |
| <a id="night"></a>`0x4` | night | `uint8` | V | night flag -> scene variable 36 (stock 0 on 601 rows, 1 on 112). Uses: see ScenarioWeatherLevelAndNightFlag |
| <a id="music"></a>`0x5` | music | `uint8` | V | music track of music slot 1, sign-extended into the scene word at 0x140D407C4; 0 = none (61 distinct stock values). Started by Scene_StartMusic through Music_StartSceneTracks |
| <a id="music_2"></a>`0x6` | music_2 | `uint8` | V | music track of music slot 2, sign-extended into the scene word at 0x140D407C8; 0 = none (26 distinct stock values) |
| <a id="entry"></a>`0x7` | entry | `uint16` | V | unit entry number -> scene variable 50 when non-zero (the word at +15 is used instead while variable 508 is set and the resume flag is clear). 199 distinct stock values; 80 of them are first keys of OverrideEntryData, whose rows only overwrite entries |
| <a id="entry_area"></a>`0x9` | entry_area | `uint16` | V | deployment area id -> scene variable 53 (when non-zero; variable 52 counts the non-zero areas). The id is the first key of EntryArea (nxd 244) and the index of a 12-byte placement record at 0x1407AE2D0 (Deployment_SelectArea, Deployment_LoadAreaPlacement). Stock: 89 of 90 values are EntryArea keys |
| <a id="entry_area_2"></a>`0xB` | entry_area_2 | `uint16` | V | second deployment area id -> scene variable 54, same two uses (32 of 32 stock values are EntryArea keys) |
| <a id="face"></a>`0xD` | face | `uint8` | V | portrait (face) code, copied to the scene byte at 0x140C6AD7A (also by the mid-event refresh from the LINKED record): the turn panel gives the unit named by +14 this face code, and entry 54 of the portrait cache takes its code from it. Stock: 76 rows use it, 11 codes |
| <a id="face_unit"></a>`0xE` | face_unit | `uint8` | V | event unit number (unit work +401) that shows the portrait code of +13; copied to the scene byte at 0x140C6AD76. Stock unit numbers: 75, 128..134, 137, 240 |
| <a id="entry_replay"></a>`0xF` | entry_replay | `uint16` | V | the unit entry number used instead of +7 while variable 508 is set (the replay of an event from the event viewer sets it). Stock: non-zero on 181 rows, equal to +7 on 146 |
| <a id="ramza_required"></a>`0x11` | ramza_required | `int8` | V | scene variable 511, written only when the area at +9 is non-zero: non-zero = party member 0 must be deployed (see ScenarioRamzaRequiredRule). Stock: 0 on 363 rows, 1 on 350 (23 rows hold 1 with no area, never applied) |
| <a id="value_lo"></a>`0x12` | value_lo | `uint8` | V | per-event word = this byte + (byte +19 << 10), OR (byte +20 << 8), 16 bits; this byte is the low 8 bits of the link (the event number of another record) |
| <a id="value_hi6"></a>`0x13` | value_hi6 | `uint8` | V | word bits 10..15: bits 0..1 = link bits 8..9, bits 2..5 = word flag bits 12..15, bits 6..7 are shifted out |
| <a id="value_mid2_flags"></a>`0x14` | value_mid2_flags | `uint8` | V | OR'ed into the word at bit 8 (bits 0..1 = flag bits 8..9, bit 7 = bit 15); exactly 0x80 = Scenario_CheckBattleRecord lets the battle set-up continue |
| <a id="unknown_21"></a>`0x15` | unknown_21 | `uint8` | V | read by no function of the game (neither ScenarioSetup_ApplyRecord nor Scenario_CheckBattleRecord, and nothing else refers to the block); 0 on all 713 used stock rows |
| <a id="enhanced_battle_event"></a>`0x16` | enhanced_battle_event | `uint16` | V | key of the EnhancedBattleEvent rows; the applier returns before writing the map variable when that key has no row or 16 or more entries |

## Referenced by

- Described by tables: [ScenarioSetup](../tables/ScenarioSetup.md)
- Observed behaviours: [RecordBytesTheGameNeverReads](../behaviors/RecordBytesTheGameNeverReads.md)

## Open questions

None recorded.
