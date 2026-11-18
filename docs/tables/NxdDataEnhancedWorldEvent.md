# NxdDataEnhancedWorldEvent

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** NXD file
- **NXD table id:** 199
- **Rows:** 540 rows of 32 bytes
- **Keyed by:** three keys: id (0..46) x id2 (0..23) x id3 (0..6)
- **Read by:** [SettlementEvent_EvaluateConditions](../functions/SettlementEvent_EvaluateConditions.md)
- **Row layout:** [NxdDataEnhancedWorldEventRow](../structs/NxdDataEnhancedWorldEventRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

World-map event rows keyed by event, step and sub-step: event type and parameters. Verdict: designer-data.

## Behavior

- V: 540 rows, three keys id (0..46) x id2 (0..23) x id3 (0..6); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 5 of 7 columns not decoded (see the row layout)
