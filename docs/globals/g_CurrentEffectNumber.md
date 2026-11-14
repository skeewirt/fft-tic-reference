# g_CurrentEffectNumber

- **Kind:** global
- **Address:** `0x141D330BC`
- **Type:** `battle action data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

s16: the battle effect now loaded or running (-1 = none, 0..511 after the 0x1FF mask). Written by Effect_SelectForAbility (raw value, then masked), Effect_ClearCurrent and EventDataLoad_Poll (falls back to 1 when the table size is 0); read by EventDataLoad_Poll, EffectFile_UploadTexture, Effect_RunStateMachine, the sub_14034xxx primitive renderers, Effect_PatchPolygonSeams, Effect_TintByNxdScale and sub_1400D28E4

## Open questions

None recorded.
