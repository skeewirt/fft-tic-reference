# MathBytePopcount

- **Kind:** table
- **Area:** [Math](../areas/math.md)
- **Storage:** Executable
- **Address:** `0x14070A0F0`
- **Rows:** 256 rows of 1 byte
- **Keyed by:** byte value 0..255
- **Row layout:** [BytePopcountRow](../structs/BytePopcountRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number of set bits of each byte value, used to count the bits of a 32-bit mask four bytes at a time. Verdict: engine-data.

## Behavior

- V: the readers add the entries of the four bytes of a dword

## Notes

Our names. Tags: V.

## Open questions

None recorded.
