# LegacyOptionsDefaultChoices

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FA420`
- **Rows:** 12 rows of 4 bytes
- **Keyed by:** option 0..11
- **Row layout:** [OptionChoice](../structs/OptionChoice.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Default choice of each of the 12 options of the legacy options screen. Verdict: designer-data.

## Behavior

- V: readers copy 12 dwords (three 16-byte copies) and compare 12 pairs; the live copy is the next object
- V: sub_140365F34: on 'defaults' copies the 12 dwords into the live selections (0x1408FA460)
- V: sub_140364D2C: compares live selections with them to see whether anything changed

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which option is which
