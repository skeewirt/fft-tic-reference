# Battle_UnitStatusFill

- **Address:** `0x1402158F4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void __fastcall Battle_UnitStatusFill(int slot)`
- **Callers:** `Battle_TimelineRefresh` (0x140216A8F, called once per slot 0..20 when the panel is not in timeline
- **Callees:** `TurnPanel_SetTag`, `sub_14022AA88`, `sub_1400E4C48`, `sub_140214134`, `sub_1400E4CD0`,

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the battle status panel's view record (and the addon's cached fields) from the live unit table, for one slot.
This is the best independent reader of the record's stat offsets.

## Behavior

- V: the body runs only when bit `slot` of `dword_140D4058C` is set, and it clears that bit. It then calls
  `TurnPanel_SetTag` for the timeline rows that show this slot. The header block below is filled only when
  `g_BattleState` is not 91, the first `g_TurnList` entry's unit is this slot, and the panel word at +65664 has
  bit 0x1000 clear.
- V: for slot <= 20 the field pointers are computed from `g_BattleUnitTable + 512*slot`:
  `+0x29` (level), `+0x28` (EXP), `+0x1FC` (name id), `+0x14C`, `+0x66` (status countdowns), `+0x61`
  (effective status byte 0), `+0x41`, `+0x2B` (Brave), `+0x2D` (Faith), `+0x8` (zodiac), `+0x01` (occupied),
  `+0x1F8`, `+0x06` (flags), `+0x1EC`, `+0x1BC` (slot), `+0x32`, `+0x30`, `+0x36`, `+0x34`, `+0x1B8`
  (active-unit marker). The code adds these offsets to the table's own address (for example 0x141853D21 = unit
  +0x41, 0x141853D41 = unit +0x61), so they do not appear as separate immediates.
- V: the setters write these panel fields (panel base +65464, view size 212):
  - `+156` slot, `+160` level (`+0x29`), `+164` EXP (`+0x28`), `+168/+170` HP current/max (`+0x30/+0x32`),
  - `+172/+174` MP current/max (`+0x34/+0x36`), `+176` CT source, `+178` Brave (`+0x2B`), `+180` Faith (`+0x2D`),
  - `+182` zodiac (`u16(+8) >> 12`), `+185` flags bit 2 of `+6`, `+186` team/auto code, `+188` slot,
  - `+196` job-derived value, `+200` u32 at `+0x1F8`.
- V (2026-11-22, correction): the "CT" value is `100` when the unit's active-marker byte `+0x1B8` is non-zero;
  otherwise it is the unit's CT byte `+0x41`. The old text read the gate as `+0x38` (PA); it is `+0x1B8`.
- V: the HP/MP pair is passed to the addon gauge setters, and the name id plus the `+0x14C` block is resolved by
  `CharaName_GetDisplayName`.
- V: the team/auto code: when `+0x1EC` is above 10 it is 3; otherwise it is 0 when `+0x1EE` bit 0x08 is set, 1
  when `+0x1EE & 0x30` is non-zero, and 2 when that is zero.
- V: the status icons read the effective status bytes `+0x61` and the countdown bytes `+0x66`.
- V (2026-11-09, correction): the record built at the end is the unit's job record: `BattleUnit_BuildJobRecord(unit +1,
  record)` builds it from the battle unit's job byte (+3) and its level, JP and total JP arrays through JobRecord_FromJobId,
  and `BattleMain_SetPanelJobRecord` hands it to the panel (job name, level, JP); it is not a portrait record.

## State touched

- Calls: [TurnPanel_SetTag](TurnPanel_SetTag.md), [sub_14022AA88](sub_14022AA88.md), [sub_140214134](sub_140214134.md)

## Referenced by

- Called by: [Battle_TimelineRefresh](Battle_TimelineRefresh.md)
- Observed behaviours: [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md)

## Notes

The companion `Battle_UnitStatusFillAlt` (`0x140228778`) gets the same CT from its stat block's `+0x18` entry,
which `sub_140226CA0` fills from `unit[0x41]` (or 100 while `+0x1B8` is set). Both paths therefore read the unit's
CT byte.

## Open questions

Why the active unit (`+0x1B8` non-zero) is shown as `100` instead of its `+0x41` CT value; the byte itself is the
per-unit CT. Whether 100 is the full-gauge display value or a sentinel is not established.
