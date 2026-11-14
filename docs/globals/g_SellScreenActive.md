# g_SellScreenActive

- **Kind:** global
- **Address:** `0x141874A14`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint16`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Non-zero while the sell screen owns a list; the row price helper returns 0 without reading the list while it is zero.

## Behavior

- V: sub_14036C468 refuses to price a row when this word is zero.

## Referenced by

- Read by: [sub_14036C468](../functions/sub_14036C468.md)

## Open questions

None recorded.
