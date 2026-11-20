# JobNameAndHelpTextTags

- **Kind:** observed behaviour
- **Scope:** engine (UI text tags)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [TextTag_ExpandKeyIcon](../functions/TextTag_ExpandKeyIcon.md), [JobTable_GetNameText](../functions/JobTable_GetNameText.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The text tags 'jobname' and 'jobhelp' print a Job row's name or help text; each takes a key and a variant, and a variant whose string is empty falls back to the other.

## Behavior

- V: TextTag_ExpandKeyIcon matches the 7-letter tag names 'jobname' and 'jobhelp' (compared as packed constants) and reads one argument pair {key, variant}.
- V: JobTable_GetNameText(kind 0 = name, 1 = help, key, variant) returns the Job string +8 (name) or +0x10 (description) for variant 0 and +0x0C (name_2) or +0x14 (description_2) for variant 1, and falls back to the other variant when the chosen string is empty.
- V: the string offsets of the Job table are relative to row +8 in this path (row + 8 + the stored value); the Item and C_MES_ID_SAMPLE tables use row +4, the Ability, JobCommand and PoachItem tables row +8.

## Open questions

None recorded.
