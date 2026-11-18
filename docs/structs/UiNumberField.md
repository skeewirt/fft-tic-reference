# UiNumberField

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the StatusNumbersActorA table and the tables that share its shape.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="x"></a>`0x0` | x | `int16` | V | x offset of the number inside its VRAM staging strip |
| <a id="y"></a>`0x2` | y | `int16` | V | y offset |
| <a id="pad"></a>`0x4` | pad | `uint32` | I | unused |
| <a id="value_ptr"></a>`0x8` | value_ptr | `pointer` | V | pointer to the s16 value shown (a field of the displayed-unit records at 0x1407832A0 / 0x140783320, or the stat words near 0x1407832E0) |
| <a id="digits"></a>`0x10` | digits | `uint8` | I | digit count passed to the number drawer (3 for HP, 2 for AT) |
| <a id="style"></a>`0x11` | style | `uint8` | ? | style flags passed with the digit count (0x10 on the max-value fields, 0xA2 on the right-hand stat columns); bit meaning ? |
| <a id="mode"></a>`0x12` | mode | `int16` | V | 0 = drawn by the digit routine sub_140242FCC, 1 = by sub_140242DD8 |
| <a id="tag"></a>`0x14` | tag | `bytes[12]` | V | developer label, ASCII, NUL-padded (for example 'hp', 'hpmax', 'wt', 'At'); not read by the code |

## Referenced by

- Described by tables: [BattlePanelNumbersActor](../tables/BattlePanelNumbersActor.md), [BattlePanelNumbersTarget](../tables/BattlePanelNumbersTarget.md), [EventUnitNumbersA](../tables/EventUnitNumbersA.md), [EventUnitNumbersB](../tables/EventUnitNumbersB.md), [StatsNumbersLive](../tables/StatsNumbersLive.md), [StatsNumbersUnitA](../tables/StatsNumbersUnitA.md), [StatsNumbersUnitB](../tables/StatsNumbersUnitB.md), [StatsPanelNumbers](../tables/StatsPanelNumbers.md), [StatusNumbersActorA](../tables/StatusNumbersActorA.md), [StatusNumbersActorB](../tables/StatusNumbersActorB.md), [StatusNumbersTargetA](../tables/StatusNumbersTargetA.md), [StatusNumbersTargetB](../tables/StatusNumbersTargetB.md), [UnitPageNumberFieldsA](../tables/UnitPageNumberFieldsA.md), [UnitPageNumberFieldsB](../tables/UnitPageNumberFieldsB.md), [UnitPanelNumberFieldsA](../tables/UnitPanelNumberFieldsA.md), [UnitPanelNumberFieldsB](../tables/UnitPanelNumberFieldsB.md), [UnitStatusNumbersMode0](../tables/UnitStatusNumbersMode0.md), [UnitStatusNumbersMode1](../tables/UnitStatusNumbersMode1.md), [UnitStatusNumbersMode2](../tables/UnitStatusNumbersMode2.md), [UnitStatusNumbersMode3](../tables/UnitStatusNumbersMode3.md)

## Open questions

None recorded.
