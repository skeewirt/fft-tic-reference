# g_EventEffectWord

- **Kind:** global
- **Address:** `0x140D40930`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

int16: the effect word set by event command 0x18 (a 16-bit little-endian operand of script bytes 1 and 2), -1 = none; the event effect starter reads it with a sign extension and passes it to EventEffect_Start; the event state snapshot keeps it as a word at +554; EventScript_SkipTick resets it to -1

## Open questions

None recorded.
