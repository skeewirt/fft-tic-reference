# AbilityEventPairs

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14071F060`
- **Rows:** 15 rows of 4 bytes
- **Keyed by:** pair index
- **Read by:** [JobChange_RunPreviewAnim](../functions/JobChange_RunPreviewAnim.md)
- **Row layout:** [AbilityEventPair](../structs/AbilityEventPair.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pairs (key, event variable) that mark achievements when the job screen learns something; the object starts 0x30 earlier and also holds an unreferenced 16-byte list and a vtable. Verdict: designer-data.

## Behavior

- V: true table start is 0x14071F090 (the candidate is the object start); 15 pairs, then 0xFFFF
- V: sub_140369AB0 (legacy job screen state step): loops the pairs of the table at 0x14071F090 until key 0xFFFF and writes the event variable of the matching pair
- V: JobChange_RunPreviewAnim (0x140367F38) references the vtable that sits in the same object at +0x18

## Notes

Our names. Tags: V layout, I key meaning.

## Open questions

- ?: what the key is (ability or job id)
- ?: the 16-byte list at the object start (no reader)
