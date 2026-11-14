# GUIText_Expand

- **Address:** `0x1403F0B10`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUIText_Expand(std::string *out, const char *text, FormatArgs *args)`
- **Callers:** GUITextNode_SetTextExpanded, JobRecord_FromJobId, sub_1400FA2C4, sub_1400FA670
- **Callees:** sub_14007D060, sub_14007D160

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the text formatter (qword_143CD9C00) over text with the argument vector (264-byte records) into out; returns 1 on success.

## Behavior

- V: clears out (sub_140025C74). When qword_143CD9C00 = 0 returns 1 (out left empty). Otherwise r = sub_14007D060(formatter, out, text, args.begin = args+8, count = (args+16 - args+8) / 264); r >= 0 returns 1; r < 0 logs the error (sub_140026BD4) and returns 0.
- V: sub_14007D060 packs up to 32 of the 264-byte argument records into 16-byte {value, type} cells (type at record+256: 1 and 2 = int, 3 = byte, 4 = pointer to the record, 0 = none) and calls sub_14007D160.

## Referenced by

- Called by: [GUITextNode_SetTextExpanded](GUITextNode_SetTextExpanded.md)

## Notes

The name is ours (IDB: sub_1403F0B10). 1276 hits per 4 s. With the formatter missing the node would be set to the empty string (the bool is 1 but out is empty); I: the formatter is always present at run time. sub_14007D160 (placeholder substitution) was not read.

## Open questions

? Placeholder syntax and the int type codes 1 vs 2 (sub_14007D160).
