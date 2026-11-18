# SettlementEventPicks

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407BE5B0`
- **Rows:** 11 rows of 10 bytes
- **Keyed by:** settlement id (the current location code)
- **Read by:** [sub_1403456D4](../functions/sub_1403456D4.md)
- **Row layout:** [SettlementEventPick](../structs/SettlementEventPick.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per settlement, which scene numbers a settlement event may pick (each of four values listed twice, so each has weight 2 of 8). Verdict: designer-data.

## Behavior

- V: sub_1403456D4 (event task that starts a settlement event): picks the record 10 x location, draws the random choice and writes event variables 50, 52 (set to 1), 53 and 39
- V: single reader; 0x70 bytes to the next symbol = 11 rows of 10 plus 2 padding bytes; the random index is (8 x (random & 0x7FFF)) >> 15

## Notes

Our names. Tags: V reader and layout, I count 11.

## Open questions

- ?: which event or battle the picked values start (values are 0xE1 .. 0xFC)
