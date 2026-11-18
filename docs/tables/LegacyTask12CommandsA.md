# LegacyTask12CommandsA

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140901300`
- **Rows:** 1 block (0x1E0 bytes)
- **Keyed by:** command row 0..1
- **Read by:** [LegacyTask12_Build](../functions/LegacyTask12_Build.md)
- **Row layout:** [LegacyTask12CommandsARow](../structs/LegacyTask12CommandsARow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Command row block of the legacy scene task 12 (text labels and live pointers). Verdict: designer-data.

## Behavior

- V: reader selects it for mode 12; 0x1E0 bytes
- V: LegacyTask12_Build (0x14039A518): in mode 12 uses this block for the command rows

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: field layout
- ?: what the pointers reference
