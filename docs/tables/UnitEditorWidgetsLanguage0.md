# UnitEditorWidgetsLanguage0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F8EF0`
- **Rows:** 22 rows of 24 bytes
- **Keyed by:** unit editor field 0..21
- **Row layout:** [UnitEditorWidget](../structs/UnitEditorWidget.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Widget records of the 22 editable fields of the unit editor screen, text language 0. Verdict: designer-data.

## Behavior

- V: sub_14033BE88 picks table 0x1408F8EF0 for text language 0 and 0x1408F9100 otherwise, then indexes it by the editor field
- V: 22 rows of 24 bytes: the first qword of each row is a pointer into the executable (a position record)
- I: the 22 rows match the 22 range rows of the unit editor range tables

## Notes

Our names. Found beside the table at 0x1408F8E40; tags V pointer, ? rest.

## Open questions

- ?: the descriptor and tail bytes of a row
