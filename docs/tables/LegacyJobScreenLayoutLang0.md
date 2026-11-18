# LegacyJobScreenLayoutLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F57C8`
- **Rows:** 1 record (0x19B0 bytes)
- **Keyed by:** text language
- **Row layout:** [LegacyJobScreenLayoutLang0Row](../structs/LegacyJobScreenLayoutLang0Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Language 0 variant of the legacy page layout: a header of row sizes and a grid of cell codes (the other languages are smaller blocks). Verdict: designer-data.

## Behavior

- V: reader selects one of four blocks by text language; this block is 0x19B0 bytes before the language 1 block
- V: sub_140365F34 (legacy job / options page builder): chooses by text language 0x1408F57C8 (language 0), 0x1408F7178 (language 1), 0x1408F7678 (language 2), 0x1408F7558 (language 3)

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: field meaning
- ?: the other three variants are not candidates of this batch
