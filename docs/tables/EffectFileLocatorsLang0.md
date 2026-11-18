# EffectFileLocatorsLang0

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406749C0`
- **Rows:** 512 rows of 8 bytes
- **Keyed by:** effect number 0..511
- **Read by:** [EffectFile_GetTrackRow](../functions/EffectFile_GetTrackRow.md)
- **Row layout:** [EffectFileLocatorRow](../structs/EffectFileLocatorRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pack file number and size of every battle effect file (text language 0). Verdict: pointer-table.

## Behavior

- V: EffectFile_GetTrackRow picks this copy by the text language record
- V: about 398 of the 512 rows are filled; the rest are zero

## Notes

Our names. Tags: V.

## Open questions

- ?: what the effect files hold
