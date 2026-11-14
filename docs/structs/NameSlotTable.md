# NameSlotTable

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A name-to-slot table of the render device (constant buffers, textures, samplers): names hashed into a tree, each with a dense slot id.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="tree"></a>`0x10` | tree | `ptr` | V | Tree head; nodes keyed by the name hash (+28), slot id at +32. | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) |
| <a id="lock"></a>`0x20` | lock | `CRITICAL_SECTION` | V | Held during a lookup. | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) entered and left |  |
| <a id="entries"></a>`0x48` | entries | `{...}[40 B]` | V | Entry array, 40 bytes each, the name string at +8. | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) |
| <a id="count"></a>`0x50` | count | `int16` | V | Number of slots in use. | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) |
| <a id="capacity"></a>`0x54` | capacity | `int32` | V | Maximum number of slots. | [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) |  |

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
