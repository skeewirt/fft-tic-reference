# MovieSound_LoadBank

- **Address:** `0x1401D7608`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MovieSound_LoadBank(void *sound, int slot, int number)`
- **Callers:** Movie_Start
- **Callees:** sub_1401D5F34, Str_Format, Mem_Alloc, sub_1401D5E2C, sub_1401D7760

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads one sound bank of a movie.

## Behavior

- V: returns at once when the number is negative.
- V: slot 20 / 21 / 22 formats 'sound/movie/movie%04d/movie%04d_bgm.sab' / '_voice.sab' / '_se.sab' with the number and loads that bank.

## State touched

- Calls: [Str_Format](Str_Format.md), [Mem_Alloc](Mem_Alloc.md)

## Referenced by

- Appears in flows: [MovieStart](../flows/MovieStart.md)

## Notes

Name is ours.

## Open questions

None recorded.
