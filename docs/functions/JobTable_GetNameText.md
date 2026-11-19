# JobTable_GetNameText

- **Address:** `0x1400F4800`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `char JobTable_GetNameText(String *out, int language, unsigned int jobId, int variant)`
- **Callers:** text helpers
- **Callees:** UITable_GetRowByKey, sub_1400769EC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies one of four Job-en string slots (+8, +12, +16, +20) into out, chosen by language (0/1) and variant (0/1), falling back to the other.

## Behavior

- V: UITable_GetRowByKey(0x2E, jobId); picks RowByKey[2..5].

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [TextTag_ExpandKeyIcon](TextTag_ExpandKeyIcon.md)

## Notes

Table 0x2E = 46 = Job-en.

## Open questions

None recorded.
