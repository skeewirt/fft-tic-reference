# Battle_UnitStatusFill

- **Address:** `0x1402158F4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Battle_UnitStatusFill(int slot)`
- **Callers:** the battle scene/AT-bar task (`sub_140215540`, `sub_1402158F4` is called from the turn-order code
- **Callees:** `sub_1400E4C48`, `sub_1400E4CD0`, `sub_1400E4D5C`, `sub_1400E4DE8`, `sub_1400E4E74`,

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the battle status panel's view record (and the addon's cached fields) from the live unit table. This is the
best independent reader of the record's stat offsets.

## Behavior

- V: for slot <= 20 the field pointers are computed from `g_BattleUnitTable + 512*slot`:
  `+0x29` (level), `+0x28` (EXP), `+0x1FC` (name id), `+0x14C`, `+0x66` (status countdowns), `+0x61`
  (effective status byte 0), `+0x41`, `+0x2B` (Brave), `+0x2D` (Faith), `+0x8` (zodiac), `+0x01` (occupied),
  `+0x1F8`, `+0x06` (flags), `+0x1EC`, `+0x1BC` (slot), `+0x32`, `+0x30`, `+0x36`, `+0x34`, `+0x38` (PA). The code adds
  these offsets to the table's own address (for example 0x141853D21 = unit +0x41, 0x141853D41 = unit +0x61), so they do not
  appear as separate immediates.
- V: the setters write these panel fields (panel base +65464, view size 212):
  - `+156` slot, `+160` level (`+0x29`), `+164` EXP (`+0x28`), `+168/+170` HP current/max (`+0x30/+0x32`),
  - `+172/+174` MP current/max (`+0x34/+0x36`), `+176` CT source, `+178` Brave (`+0x2B`), `+180` Faith (`+0x2D`),
  - `+182` zodiac (`u16(+8) >> 12`), `+185` flags bit 2 of `+6`, `+186` team/auto code, `+188` slot,
  - `+196` job-derived value, `+200` u32 at `+0x1F8`.
- V: the "CT" value is `100` unless `unit[0x38] (PA) == 0`, in which case it is `unit[0x41]`.
- V: the HP/MP pair is passed to the addon gauge setters, and the name id plus the `+0x14C` block is resolved by
  `sub_1401E8B7C`.
- V: the team/auto code comes from `+0x1EE & 0x30 == 0x10` -> 1, `!= 0` -> 2, else 0; a `+0x1EC > 10` forces 3.
- V: the status icons read the effective status bytes `+0x61` and the countdown bytes `+0x66`.
- V (2026-11-09, correction): the record built at the end is the unit's job record: `BattleUnit_BuildJobRecord(unit +1,
  record)` builds it from the battle unit's job byte (+3) and its level, JP and total JP arrays through JobRecord_FromJobId,
  and `sub_14010141C` hands it to the panel (job name, level, JP); it is not a portrait record.

## Referenced by

- Observed behaviours: [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md)

## Notes

The companion `Battle_UnitStatusFillAlt` (`0x140228778`) builds the same panel for the target-info window and
takes CT from `*(i16*)(*(qword*)(turnRecord+0x88))`. Neither path reads a CT field from the unit record, which is
evidence that CT lives in the turn system (C2).

## Open questions

The exact meaning of `+0x41` and why it stands in for CT when PA is 0.
