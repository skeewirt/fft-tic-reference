# JobTreePanel

- **Kind:** structure
- **Size:** 456 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Stride 456 bytes (stock: 20 panels). Edge slots are indexed job*19 + j (19 x 24 B = 456 = one record); only 6 per table are used.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="*node"></a>`0x0` | *node | `GUINode` | V | panel node; node+544 == 18 (kind), node+548 == job index |
| <a id="*unitgadget"></a>`0x8` | *unitGadget | `GUINode` | V | the 'Unit' gadget |
| <a id="*namegadget"></a>`0x10` | *nameGadget | `GUINode` | V | 'TextBoardJobName' gadget |
| <a id="*title"></a>`0x18` | *title | `GUINode` | V | 'Title' text |
| <a id="reqs[6]"></a>`0x88` | reqs[6] | `Edge` | V | 24 B each: +0 GUINode *line (arrow), +8 GUINode *board (label), +16 int32 requiredJob, +20 int32 level; filled by JobTree_RefreshAddon |
| <a id="dependents[6]"></a>`0x118` | dependents[6] | `Edge` | V | 24 B each: +0 line, +8 board, +16 int32 childJob, +20 int32 level; the arrows leaving this job |
| <a id="nav[8][2][2]"></a>`0x1A8` | nav[8][2][2] | `uint8` | V | 8 directions x 2 candidates x {panel index, flag}; read by JobTree_HandleInput |

## Referenced by

- Observed behaviours: [JobTreeCursorNeighbourTable](../behaviors/JobTreeCursorNeighbourTable.md)

## Notes

Source: addon+72+456*i.

## Open questions

None recorded.
