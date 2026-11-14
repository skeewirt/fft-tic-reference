# BattleSnapshot

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 668112 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 668,112-byte battle image a kind-1 resume entry carries, as the capture builds it in g_BattleState: a battle context, five blocks (A..E), the 21 x 512-byte unit records and 3,000 more bytes of scene-task state. Only the unit records hold object ids in bulk; the blocks are copied byte for byte and most of the image is never written.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="context"></a>`0x0` | context | `24 + 16 bytes` | V | Battle entry context: a pointer plus seven scene variables and an argument dword. |
| <a id="sub_object_1"></a>`0x2E0` | sub_object_1 | `sub-object` | V | Set up by a constructor call during the capture; shape not decoded. |
| <a id="sub_object_2"></a>`0x3948` | sub_object_2 | `0x400` | V | A 1 KB sub-object built by the same constructor; 45 nonzero bytes in the observed capture. |
| <a id="block_a"></a>`0x3D51` | block_a | `0x2800` | V | A 10,240-byte event-script file image (the buffer at 0x140D3CD50); item and job ids appear only as operands inside the script bytecode. |
| <a id="block_b"></a>`0x6552` | block_b | `0x6EE` | V | 887 u16 values: a per-map word table built from 24-byte static map records and indexed by scene variable 39; identical in all 24 payloads checked. |
| <a id="unit_records"></a>`0x81994` | unit_records | `unit_record[21]` | V | 21 x 512 bytes from g_BattleUnitTable: job at +3, skillsets at +18/+19, abilities at +20/+22/+24, seven item words at +26..+39, name key at +508. |
| <a id="block_c"></a>`0x844B0` | block_c | `0x1000` | V | 512 eight-byte tile records of the battle map, indexed x + y * width; flag and movement-cost bytes only. |
| <a id="extra_capture"></a>`0x8DA04` | extra_capture | `0xBB8` | V | 3,000 bytes copied from 0x14114A4F0: 12-byte-ish entries with fill words; no id field identified. |
| <a id="block_d"></a>`0x91834` | block_d | `0x5E8` | V | Nine 168-byte scene-task data slots at 0x14114B150; captured but never restored. |
| <a id="no_work_copy"></a>`0x994EC` | no_work_copy | `(none)` | V | No slot work copy ends the snapshot: from +0x994EC the bytes are zero in every observed battle entry (no slot header), and block E lies inside that range at +0xA0418. An earlier reading that the last 40,164 bytes repeat the work copy was wrong. |
| <a id="block_e"></a>`0xA0418` | block_e | `0x19D0` | V | The battle action state at 0x1418716A0: the current action word at +2 (an ability id masked to 10 bits), unit and action flags, and the wide action tables. |

## Behavior

- V: the capture writes 32 intervals, not the whole image; the largest never-written span is 501,656 bytes, so those bytes keep what an earlier battle left there and are still copied back on load.
- V: the restore reads 117 sites; block D has no restore site and is reloaded by the scene-task path instead of from the image.
- V: the only item ids are the 147 equipment words of the 21 unit records; the action word stores an ability id and an item use derives the item as the action number minus 128.
- V: the image holds absolute pointers (the context pointer and a heap pointer at the start of the body), so it is a same-build snapshot and not a portable format.
- I: blocks A, B, D and E carry no object id of their own because their writers are scene, map and action code rather than item or job stores; block C is a tile table.

## Notes

An earlier reading placed block E at 0x9F418. The capture's destination for 0x1418716A0 lands at g_BattleState + 0xA0418 and ends exactly where the tail fields begin, so 0xA0418 is the block and the older offset is 4,100 bytes of stale data.

## Open questions

? the shape of the 20 x 512-byte block at 0x3D51 (zero in the observed capture); ? the role of the 3,000-byte capture; ? the id content of block B's high bits and of block E's inner tables.
