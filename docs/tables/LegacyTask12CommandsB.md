# LegacyTask12CommandsB

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1409014E0`
- **Rows:** 1 block (length unknown)
- **Keyed by:** command row 0..1
- **Read by:** [LegacyTask12_Build](../functions/LegacyTask12_Build.md)
- **Row layout:** [LegacyTask12CommandsBRow](../structs/LegacyTask12CommandsBRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Command row block of the legacy scene task 12 for the other mode. Verdict: designer-data.

## Behavior

- V: extent unknown (the next candidate is 0x5690 later: the block is followed by a large zeroed area)
- V: LegacyTask12_Build (0x14039A518): the block of the other mode

## Notes

Our names. Tags: V reader, ? extent.

## Open questions

- ?: true length of the block
