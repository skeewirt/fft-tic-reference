# BattleSpawnEntry

- **Kind:** structure
- **Area:** [Unit data](../areas/unit-data.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 40-byte entry of a scripted battle's entry block: the description of one unit to build. The OverrideEntryData row of the same index overwrites several of its fields in place before the units are built.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="marker"></a>`0x0` | marker | `uint8` | V | Look / unit marker; 0 = no unit. Becomes work +0 (Battle_PlaceEntryUnits, Unit_ApplySpawnRecord). |
| <a id="flags"></a>`0x1` | flags | `uint8` | V | Bit 3 = build from the guest save record (50..53) with the same marker; bits 0x11 are kept into work +6 on that path; bit 5 = no generic job levels (UnitWork_InitFromSpawnRecord); bits 6 and 7 clear two job level nibbles. |
| <a id="name_byte"></a>`0x2` | name_byte | `uint8` | V | Name byte; becomes work +508 and is replaced by the OverrideEntryData chara_name column when that is set. |
| <a id="level"></a>`0x3` | level | `uint8` | V | 1..99 as given; 100..253 = relative to the highest party level; 0 or 0xFE = random below it (Unit_ApplySpawnRecord). |
| <a id="birth_month"></a>`0x4` | birth_month | `uint8` | V | Birthday month; out of range = random day. |
| <a id="birth_day"></a>`0x5` | birth_day | `uint8` | V | Birthday day; out of range = random day. |
| <a id="brave"></a>`0x6` | brave | `uint8` | V | Brave; above 100 = 45 + random 0..29. |
| <a id="faith"></a>`0x7` | faith | `uint8` | V | Faith; above 100 = 45 + random 0..29. |
| <a id="job"></a>`0xA` | job | `uint8` | V | Job id (one byte); copied to work +3 by UnitWork_InitFromSpawnRecord; job 0x97 forces zodiac 0xC. |
| <a id="head"></a>`0x12` | head | `uint8` | V | Starting head item id; 0xFF = empty, 0xFE = default pick (UnitWork_ApplyStartingEquipment). |
| <a id="body"></a>`0x13` | body | `uint8` | V | Starting body item id; same markers. |
| <a id="accessory"></a>`0x14` | accessory | `uint8` | V | Starting accessory item id; same markers. |
| <a id="first_hand"></a>`0x15` | first_hand | `uint8` | V | Starting item of the first hand; same markers. |
| <a id="second_hand"></a>`0x16` | second_hand | `uint8` | V | Starting item of the second hand; same markers. |
| <a id="byte_23"></a>`0x17` | byte_23 | `uint8` | V | Copied to work +4 (Unit_ApplySpawnRecord); its meaning is not decoded. |
| <a id="side_presence"></a>`0x18` | side_presence | `uint8` | V | Copied to work +5 and work +494: bits 0x30 = side, bits 0xC0 = presence at battle start (see Battle_PlaceEntryUnits). |
| <a id="byte_28"></a>`0x1C` | byte_28 | `uint8` | V | Becomes work +40; above 99 = random 0..99. |
| <a id="slot_override"></a>`0x20` | slot_override | `uint8` | V | Becomes work +401 when not 0xFF (else a running counter from 0xFE) (Battle_PlaceEntryUnits). |
| <a id="tail"></a>`0x21` | tail | `uint8[7]` | V | Bytes +33..+39 are copied to work +407..+413 (Unit_ApplySpawnRecord). |

## Behavior

- V: OverrideEntry_FillUnitEntry writes level, brave, faith, the guest-record bit, the five item bytes and the presence bits from the OverrideEntryData row (columns level, brave, faith, from_guest_record, head, body, accessory, right_hand, left_hand, presence).
- V: the bytes +25..+27, +30 and +31 are read by Battle_PlaceEntryUnits into work +79..+81, +404 and +406; their meaning is not decoded.

## Notes

Detail and evidence: the function sheets Unit_ApplySpawnRecord, OverrideEntry_FillUnitEntry and Battle_PlaceEntryUnits.

## Open questions

? the bytes +8, +9, +11..+17 other than those listed, +25..+27, +29..+31 as a whole.
