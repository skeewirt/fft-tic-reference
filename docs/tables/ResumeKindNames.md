# ResumeKindNames

- **Kind:** table
- **Area:** [Save data](../areas/save-data.md)
- **Storage:** Executable
- **Address:** `0x140671E70`
- **Rows:** 4 rows of 8 bytes (the run continues with two more string pointers)
- **Keyed by:** resume save kind 0..3
- **Read by:** [sub_1400C4360](../functions/sub_1400C4360.md)
- **Row layout:** [StringPointerRow](../structs/StringPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Short names of the four kinds of a resume (suspend) save entry: main, world, attack, fturn. They are appended to the resume save file names. Verdict: text.

## Behavior

- V: the four kind strings are separate pooled strings, one of them is addressed by one further instruction; no string is a tail of another (no reference points inside any of them)
- V: the name builder formats resume_en<NN>_<kind>.sav for save modes 2..4 and resume_enbtl_<kind>.sav for mode 1 with kind_name[kind]; mode 0 uses a fixed world map name with no kind
- I: the two string pointers after the fourth entry (the name format and a fixed file name) are separate globals; no code indexes them from this table

## Notes

Our names. Tags: V layout, V reader, I count.

## Open questions

- ?: whether the fifth and sixth pointers are read by index anywhere
