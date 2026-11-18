# NxdDataConfigItemVoiceLanguage

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 259
- **Rows:** 2 rows of 12 bytes
- **Keyed by:** one key: id (0..1)
- **Read by:** [ConfigMenu_ReadSettings](../functions/ConfigMenu_ReadSettings.md)
- **Row layout:** [NxdDataConfigItemVoiceLanguageRow](../structs/NxdDataConfigItemVoiceLanguageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Option values for the voice-language setting (two). Verdict: engine-data.

## Behavior

- V: 2 rows, one key id (0..1); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
