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
| <a id="nibbles"></a>`0x3` | nibbles | `int8` | V | high nibble -> scene variable 48, low nibble -> scene variable 35 (skipped for map 32 in the resume case) |
| <a id="var36"></a>`0x4` | var36 | `int8` | V | scene variable 36 |
| <a id="scene_word_a"></a>`0x5` | scene_word_a | `int8` | V | sign-extended into the scene word at 0x140D407C4 |
| <a id="scene_word_b"></a>`0x6` | scene_word_b | `int8` | V | sign-extended into the scene word at 0x140D407C8 |
| <a id="entry_key"></a>`0x7` | entry_key | `uint16` | V | unit entry key -> scene variable 50 when non-zero (the word at +15 is used instead while variable 508 is set and the resume flag is clear) |
| <a id="area_a"></a>`0x9` | area_a | `uint16` | V | deployment area id -> scene variable 53 (when non-zero; variable 52 counts the non-zero areas) |
| <a id="area_b"></a>`0xB` | area_b | `uint16` | V | deployment area id -> scene variable 54 |
| <a id="scene_byte_a"></a>`0xD` | scene_byte_a | `uint8` | V | copied to the scene byte at 0x140C6AD7A (also by the mid-event refresh from the LINKED record); saved in the battle capture |
| <a id="scene_byte_b"></a>`0xE` | scene_byte_b | `uint8` | V | copied to the scene byte at 0x140C6AD76, as +13 |
| <a id="entry_key_resume"></a>`0xF` | entry_key_resume | `uint16` | V | the entry key used instead of +7 while variable 508 is set |
| <a id="var511"></a>`0x11` | var511 | `int8` | V | scene variable 511 (written only when the area at +9 is non-zero) |
| <a id="value_lo"></a>`0x12` | value_lo | `uint8` | V | per-event word = this byte + (byte +19 << 10), OR (byte +20 << 8), 16 bits; this byte is the low 8 bits of the link (the event number of another record) |
| <a id="value_hi6"></a>`0x13` | value_hi6 | `uint8` | V | word bits 10..15: bits 0..1 = link bits 8..9, bits 2..5 = word flag bits 12..15, bits 6..7 are shifted out |
| <a id="value_mid2_flags"></a>`0x14` | value_mid2_flags | `uint8` | V | OR'ed into the word at bit 8 (bits 0..1 = flag bits 8..9, bit 7 = bit 15); exactly 0x80 = Scenario_CheckBattleRecord lets the battle set-up continue |
| <a id="battle_event_key"></a>`0x16` | battle_event_key | `uint16` | V | key of the EnhancedBattleEvent rows; the applier returns before writing the map variable when that key has no row or 16 or more entries |

## Referenced by

- Described by tables: [ScenarioSetup](../tables/ScenarioSetup.md)

## Open questions

None recorded.
