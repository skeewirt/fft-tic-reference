# PanelStateOffsets

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140684810`
- **Rows:** 16 rows of 1 bytes
- **Keyed by:** panel state value
- **Row layout:** [PanelStateOffset](../structs/PanelStateOffset.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A short list of signed offsets a unit panel row builder adds to a position; the bytes 0x2E, 0, 0, 0, 0, 0, 13, 13, 31, 31, 0, 0, -2, -1, -1, -1. Verdict: designer-data.

## Behavior

- V: sub_140338484 (unit panel row builder): sign-extended byte read at table[index] when it places a row
- V: 16 bytes up to the next symbol; read with a sign-extending byte load

## Notes

Our names. Tags: V extent and reader, ? meaning.

## Open questions

- ?: what the index is
- ?: whether all 16 entries are used
