# PowersOfTen

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** Executable
- **Address:** `0x140672680`
- **Rows:** 10 rows of 4 bytes
- **Keyed by:** digit position 0..9
- **Read by:** [EventMessage_Task](../functions/EventMessage_Task.md)
- **Row layout:** [PowerOfTen](../structs/PowerOfTen.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Powers of ten used to split a number into decimal digits for text. Verdict: engine-data.

## Behavior

- V: ten u32 values; read as table + 4 x digit count
- V: sub_140243390 and EventMessage_Task (0x140225335): number-to-digit conversion for message text

## Notes

Our names. Tags: V.

## Open questions

None recorded.
