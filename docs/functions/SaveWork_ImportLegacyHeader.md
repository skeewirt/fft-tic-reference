# SaveWork_ImportLegacyHeader

- **Address:** `0x14038E330`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveWork_ImportLegacyHeader(void)`
- **Callers:** sub_1402BB6B0
- **Callees:** memmove, memset, strnlen, sub_14002620C, sub_14002630C, sub_1402BACCC (and others)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

(I) Imports a legacy PSP save header into the work copy: writes the summary bytes +274..+286.

## Behavior

- I (operand scan of the cache and work copy): one of 26 functions that touch the slot cache, the work copy or the auto slot; it writes the summary fields from a legacy header.
- V (decompile): one caller; uses string copies and memmove into the work copy.

## State touched

- Calls: [sub_14002620C](sub_14002620C.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

The legacy header layout is not decoded here (?).
