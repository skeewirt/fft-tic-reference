# TurnList_InsertEntry

- **Address:** `0x140310490`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool TurnList_InsertEntry(int unit, int isAction, uint16 time, uint8 *list)`
- **Callers:** TurnList_Build (4 sites)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Inserts one 4-byte entry into a 40-entry turn-order list, sorted by its time key; a pending-action entry also carries the unit's ability (9 bits).

## Behavior

- V: entry = byte 0 flags, byte 1 ability low byte, word +2 time; the list is kept ascending by time: the first entry whose time is above `time` and every entry after it move down one (the 40th drops); returns 0 when no entry was above `time` (list full).
- V: byte 0 = unit (bits 0..4; 31 marks the end of the list); isAction adds 0x40; then, when the unit's command byte (unit work record +0x1A1) is 18, 0x20 and no ability; otherwise byte 1 = low byte of the unit's ability word (+0x1A2) and 0x80 when that word is above 0xFF.
- V: so 9 bits of the ability survive: 512 is stored as (0x80, 0) and read back as 256 (Vengeance).

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [TurnList_Build](TurnList_Build.md)

## Notes

The only writer of the ability byte of a turn-order entry (V: xrefs of g_TurnList and of the local lists of TurnList_Build's callers).

## Open questions

None recorded.
