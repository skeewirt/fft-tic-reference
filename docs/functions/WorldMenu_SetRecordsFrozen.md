# WorldMenu_SetRecordsFrozen

- **Address:** `0x1402CCC38`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall WorldMenu_SetRecordsFrozen(int release)`
- **Callers:** sub_1402D4A3C, sub_1402D50E4, MenuCtl_Entry43, MenuCtl_Entry28, sub_1403793DC
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets or clears bit 3 (value 8) of the flag word of every registered world-menu record: set when the argument is 0, cleared otherwise.

## Behavior

- V: it walks two pointer lists, `unk_140D4C980` (count `dword_140D4C968`) and `qword_140D4C0B0` (count `dword_140D4C978`), and ORs 8 into (argument 0) or masks 8 out of (non-zero) the first dword each pointer addresses.
- V: returns the last record pointer visited in the first list, or the count `dword_140D4C968` when that list is empty (not a flag word); the second list does not change the return value.
- I: bit 8 holds the records while a blocking wait runs: callers pass 0 right before `AudioQueue_WaitIdle` and pass 1 before popping a menu level (rests on those call orders).

## Notes

Whole body read.

## Open questions

What bit 8 does in the records' consumer.
