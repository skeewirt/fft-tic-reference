# LegacyOptionsTextBases

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FA4E0`
- **Rows:** 12 rows of 4 bytes
- **Keyed by:** option 0..11
- **Row layout:** [OptionTextBase](../structs/OptionTextBase.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per option of the legacy options screen, the message id of its first choice label. Verdict: designer-data.

## Behavior

- V: reader adds the live choice to dword [option]; 12 dwords, then a window template
- V: sub_140364FAC: message id = base + choice for each option row; sub_140365F34 too

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: the window template that follows in the same 0xA0-byte object
