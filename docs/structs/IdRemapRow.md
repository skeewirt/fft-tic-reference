# IdRemapRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 56 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Seven id pairs.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="pairs"></a>`0x0` | pairs | `uint32[14]` | V | Seven (from, to) pairs: the lookup returns the to of the first pair whose from matches; a to of -1 means none; ids up to 0xA7 pass through unchanged. |

## Referenced by

- Described by tables: [IdRemapPairs](../tables/IdRemapPairs.md)

## Open questions

None recorded.
