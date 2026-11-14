# JobChangeListAddon

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 19024 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Change Job list screen object (the list addon, reached as [[[root]+0x10]+0x58]+0x78 and as field 15 of the screen object): 19 cell records of 148 bytes, 19 cell gadgets of 256 bytes, and the cursor state; every array in it has exactly 19 cells.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="cell_records"></a>+8832 | cell_records | `JobRecord[19]` | V | Cell i at +8832 + 148*i; JobList_StoreCell copies the record in and returns early when the cell index is 19 or more (compare at 0x14012EC81). |
| <a id="cell_gadgets"></a>+11712 | cell_gadgets | `byte[19][256]` | V | One 256-byte gadget per cell (star, current/text, unit node); the cell root node is in slot 24 of each gadget. |
| <a id="detail_target"></a>+16576 | detail_target | `gadget` | I | Target of JobList_ApplyCellRecord when the screen mode is 9 (ability detail); the next gadget at +16832 serves modes 1 to 3 and the tree-selected case. |
| <a id="mode"></a>+19008 | mode | `int32` | V | Screen mode; JobList_StoreCell compares it with 2 and 9, and stores a cursor only for modes 2 and below. |
| <a id="phase"></a>+19012 | phase | `uint8` | V | 1, 2 or 3 selects the pad-cursor-on-cell-0 behaviour in JobList_StoreCell. |
| <a id="cursor"></a>+19016 | cursor | `int32` | V | The cell the cursor is on; JobList_StoreCell writes it when a stored record has its current flag (record +141) set; in mode 9 it names the cell whose ability list is shown. |
| <a id="tree_selected"></a>+19020 | tree_selected | `int32` | I | Non-zero while a tree click owns the selection; JobList_StoreCell then draws into the +16832 gadget instead of the cell's own. |

## Open questions

? the full size of the object and the fields between the listed ones were not decoded; the 19024 size is the end of the last field read, not the allocation.
