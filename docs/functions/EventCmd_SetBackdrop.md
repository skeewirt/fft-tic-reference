# EventCmd_SetBackdrop

- **Address:** `0x1402F1C08`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetBackdrop(void)`
- **Callers:** EventCmd_Run through the class table, class 5
- **Callees:** sub_14017E000, EventThread_Yield, sub_14034394C, sub_140343564

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 5 handler: switches the backdrop to the one numbered by argument byte 9, loading its texture file when the mode is zero.

## Behavior

- V: the new value is argument byte 9. It is compared with the word at bytes 10-11 of xmmword_141862450. When they are equal, nothing changes and the handler sets bit 2 and returns.
- V: the word at bytes 10-11 of xmmword_141862450 (read as signed) is compared with byte 9; when equal nothing changes and the handler sets bit 2 and returns.
- V: otherwise the word at bytes 10-11 of xmmword_141862450 is set to byte 9.
- V: mode zero: when byte 9 differs from dword_140D49AC0, waits with sub_140343564, stores byte 9 into dword_140D49AC0, and calls sub_14034394C with byte 9 and qword_1437FC2E0. sub_14034394C formats the path fftpack/tex/wldbk/bk%03d.tex with byte 9 and loads it; when it returns 0, the handler waits again with sub_140343564.
- V: mode zero: when byte 9 differs from dword_140D49AC0, waits with sub_140343564 (a loop that yields with EventThread_Yield(1) while the high dword of qword_141856AB0 is non-zero), stores byte 9 into dword_140D49AC0, and calls sub_14034394C with byte 9 and qword_1437FC2E0. sub_14034394C formats the path fftpack/tex/wldbk/bk%03d.tex with byte 9 and opens it; when the open check (sub_1403D21F0) returns 1 it frees the file object and returns 1, otherwise it reads the file into the target buffer and returns 0. When the return is 0 the handler waits again with sub_140343564.

## State touched

- Calls: [EventThread_Yield](EventThread_Yield.md)

## Notes

Byte 9 is the only argument read. Byte 9 is a backdrop number used in the file name bk%03d.tex. Bytes 10 and 11 are not used.

## Open questions

What sub_14017E000 does with the object and byte 9 (it looks up a resource through qword_143CDA490 and sets up two sub-objects at +272 and +416 of the object at +64; not fully read); what the record at +16 of qword_143CD9DA8 is; why the second wait follows a 0 return of sub_14034394C.
