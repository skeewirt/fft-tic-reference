# BTurn_StatusFlags

- **Address:** `0x14030FB9C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `unsigned int __fastcall BTurn_StatusFlags(uint8_t *unit)`
- **Callers:** `Battle_TurnEngine` (`0x14030F2D2`, `0x14030F310`, `0x14030F362`, `0x14030F435`, `0x14030F477`, `0x14030F510`, `0x14030F782`), `sub_1403107A4`, `sub_140204B78`
- **Callees:** `sub_140278FA8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the turn-scheduling flags of one unit work record: whether it can act at all, and whether Haste/Slow modify
its CT increment.

## Behavior

- V: returns bit 0 (`1`) when the slot is empty (`unit[1] == 0xFF`), when `sub_140278FA8(unit, 3) != 0`, or when
  `unit[0x1B4] & 0x40` is set. The turn engine skips such units in the CT tick and in selection.
- V: returns `6` when `unit[0x61] & 0x20` is set (a "cannot be selected" status; the engine then treats the unit as
  not acting this pass).
- V: `0x10` is returned when `unit[0x64] & 0x08` is set; the engine multiplies speed by 1.5 on it (Haste).
- V: `0x20` is returned when `unit[0x64] & 0x04` is set; the engine halves speed on it (Slow).
- V: an extra `0x0A` is OR-ed in when `unit[0x65] & 0x10` is set. No caller in the paths read tests those bits; their
  meaning is **?**.
- V: `sub_140278FA8(unit, 3)` is the same guard used by the event/unit code for "unit is gone".

## Referenced by

- Called by: [Battle_TurnEngine](Battle_TurnEngine.md), [sub_140204B78](sub_140204B78.md)

## Notes

The return value is a bit set, not an enum: the engine tests individual bits (`& 1`, `& 0x20`, `& 0x10`).

## Open questions

The meaning of `sub_140278FA8`'s second argument (3) and of `unit[0x1B4] & 0x40`.
