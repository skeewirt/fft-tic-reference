# NxdDataEventId

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** NXD file
- **NXD table id:** 156
- **Rows:** 887 rows of 44 bytes
- **Keyed by:** one key: id (0..886)
- **Read by:** [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md), [EventControl_PausedTick](../functions/EventControl_PausedTick.md), [EventScript_LoadCurrent](../functions/EventScript_LoadCurrent.md), [EventScript_Run](../functions/EventScript_Run.md), [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md)
- **Row layout:** [NxdDataEventIdRow](../structs/NxdDataEventIdRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per story event (887): sortie confirm link, sound state parameter and parameters. Verdict: designer-data.

## Behavior

- V: 887 rows, one key id (0..886); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 9 of 19 columns not decoded (see the row layout)
