# JobTable_GetNameText

- **Address:** `0x1400F4800`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `char JobTable_GetNameText(String *out, int language, unsigned int jobId, int variant)`
- **Callers:** TextTag_ExpandKeyIcon
- **Callees:** UITable_GetRowByKey, sub_1400769EC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies one of the four Job text slots (name +8, name_2 +0x0C, description +0x10, description_2 +0x14) into out, chosen by the kind (0 name, 1 help text) and the variant (0 or 1), falling back to the other variant when the chosen string is empty.

## Behavior

- V: UITable_GetRowByKey(0x2E, jobId) gets the Job row; the second argument is the kind (0 = name slots, 1 = help slots; any other value returns 0) and the fourth the variant: kind 0 variant 0 = +8, variant 1 = +0x0C; kind 1 variant 0 = +0x10, variant 1 = +0x14.
- V: when the chosen string is empty it tries the other variant of the same kind; returns 0 when both are empty or the row is missing, else 1 after copying the string into out.
- V: the offsets are string offsets relative to row +8 (the string is at row + 8 + the stored value).
- V: its caller TextTag_ExpandKeyIcon passes kind 0 for the 'jobname' tag and kind 1 for the 'jobhelp' tag, the key from the tag argument and the variant from the argument pair (see behavior JobNameAndHelpTextTags).

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [TextTag_ExpandKeyIcon](TextTag_ExpandKeyIcon.md)
- Observed behaviours: [JobNameAndHelpTextTags](../behaviors/JobNameAndHelpTextTags.md)

## Notes

Table 0x2E = 46 = Job-en (columns name, name_2, description, description_2). The offsets 8, 0x0C, 0x10 and 0x14 are reached as dword indexes 2..5 of the row pointer (the +0x14 slot is dword index 5), so no byte offset 0x14 appears in the body.

## Open questions

None recorded.
