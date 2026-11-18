# SoundPackPathPatterns

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140671F80`
- **Rows:** 7 rows of 8 bytes
- **Keyed by:** none found (no code reads the table)
- **Row layout:** [StringPointerRow](../structs/StringPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Seven sound pack path patterns: the common UI sound pack, the novel pack, the common sound pack, the per movie sound effect, voice and music packs (movie number %04d) and the per music pack (music number %05u). Verdict: text.

## Behavior

- V: the loaders address the seven strings directly (one to three instructions each); the pointer list itself has no reader, so the strings are owned by the loaders, not by the list
- V: four of the seven (slots 3 to 6) are printf patterns with one or two numeric conversions
- V: no instruction refers to the list; the path strings are used directly by the sound pack loaders (sub_1401D6600, sub_1401DFCD4, sub_1402BA7C4, sub_1401D7608, sub_1401D7450)
- I: the list is a leftover or is read through a computed address

## Notes

Our names. Tags: V layout, V no reader, I purpose.

## Open questions

- ?: any reader of the list
