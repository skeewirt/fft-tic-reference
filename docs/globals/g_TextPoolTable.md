# g_TextPoolTable

- **Kind:** global
- **Address:** `0x140D40990`
- **Area:** [Data access](../areas/data.md)
- **Type:** `char *[32]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The thirty-two text-pool pointers the generic decoder indexes by a text id's five kind bits. Slot 0 is filled at load and slots 1..31 by one loop.

## Behavior

- V: the decoder maps (id >> 11) & 0x1F through this table and then walks the pool to the (id & 0x7FF)-th string.

## Referenced by

- Described by tables: [TextPools](../tables/TextPools.md)

## Open questions

None recorded.
