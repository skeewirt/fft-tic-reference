# UnitMarkerPersonVariables

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14071F060`
- **Rows:** 15 rows of 4 bytes
- **Keyed by:** pair index
- **Read by:** [JobChange_RunPreviewAnim](../functions/JobChange_RunPreviewAnim.md)
- **Row layout:** [UnitMarkerPersonVariable](../structs/UnitMarkerPersonVariable.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Fifteen pairs of (unit marker, person variable): the marker is the unit key of the CharaName table kept in the party record, the variable is the entry of that person (960 + position) in the event variable space. The legacy job screen state step writes 12 into the variable when a dismissal is confirmed, which records the unit as dismissed. The object starts 0x30 earlier and also holds an unreferenced 16-byte list and a vtable. Verdict: designer-data.

## Behavior

- V: true table start is 0x14071F090 (the candidate is the object start); 15 pairs, then 0xFFFF
- V: sub_140369AB0 (legacy job screen state step): loops the pairs of the table at 0x14071F090 until key 0xFFFF and, on the match of the unit being handled, writes the value 12 into the event variable of the pair
- I: the writing step is the dismissal confirm of the unit screen (inferred from the state the step runs in); 12 is the dismissed value of the person variable (see the registry EventVariableRanges, people)
- V: the variables are ids 974 to 1013, all in the people range of the event variables
- V: JobChange_RunPreviewAnim (0x140367F38) references the vtable that sits in the same object at +0x18

## Notes

Our names. Tags: V layout, V key meaning (unit marker, CharaName key), I confirm state. Earlier read as an ability or job id table: it is not.

## Open questions

- ?: the 16-byte list at the object start (no reader)
