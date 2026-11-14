# JobTreeAddon

- **Kind:** structure
- **Size:** 13312 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

STOCK layout (20 panels). Vtables 0x140711618 / 0x140711718; slot 4 = JobTree_RefreshAddon.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="panels[20]"></a>`0x48` | panels[20] | `JobTreePanel` | V | starts at +72 (stock: 20 panels) |  |  |
| <a id="records[n]"></a>`0x23E8` | records[N] | `JobRecord` | V | addon+9192, 148-byte stride |  |  |
| <a id="slotrecs[n]"></a>`0x2444` | slotRecs[N] | `SlotRecord` | V | addon+9284 (record id = panel index + 80) |  |  |
| <a id="*gadgetroot"></a>`0x2F78` | *gadgetRoot | `void` | V | `*(a1+12152)` null-checked in SetPanelRecord |  |  |
| <a id="selectedslot"></a>`0x2FC8` | selectedSlot | `int` | V | a1+12232 written with job position | [JobTree_Ctor](../functions/JobTree_Ctor.md), [JobTree_OnEvent](../functions/JobTree_OnEvent.md) | [JobTree_HandleInput](../functions/JobTree_HandleInput.md) |

## Referenced by

- Observed behaviours: [JobTreePanelCountLimits](../behaviors/JobTreePanelCountLimits.md)

## Notes

Source: UIAddonFFTOUnitJobTree.

## Open questions

None recorded.
