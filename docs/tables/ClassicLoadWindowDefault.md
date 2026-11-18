# ClassicLoadWindowDefault

- **Kind:** table
- **Area:** [Save data](../areas/save-data.md)
- **Storage:** Executable (initialised data, written at run time)
- **Address:** `0x140782D18`
- **Rows:** ?
- **Keyed by:** text language (1 / default)
- **Row layout:** [ClassicLoadWindowDefaultRecord](../structs/ClassicLoadWindowDefaultRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Window template and live fields of the classic load menu, one of three language variants. Verdict: designer-data.

## Behavior

- V: 37 accesses at offsets +0..+0xD1 from one function
- V: sub_14021C620 (classic load menu): picks 0x140782AA8 / 0x140782BA8 / 0x140782D18 by language and draws it; reads and writes many fields between +0x18 and +0xD1 (cursor rows, slot labels)

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: exact record length and field list
- ?: whether Enhanced mode ever shows this menu
