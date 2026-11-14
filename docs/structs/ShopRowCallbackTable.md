# ShopRowCallbackTable

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 56 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The seven qword row handlers at 0x141876AD0..0x141876B00 that the list gadget calls per visible row; the shop, equip and item screens install different functions in the same slots.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="slot0"></a>+0 | slot0 | `ptr` | V | Equipped count or job level: sub_140332C8C (shop/equip) or JobMenu_ReadLevel. |
| <a id="slot1"></a>+8 | slot1 | `ptr` | V | Total count or JP: sub_140332C54 (shop/equip) or JobMenu_ReadJp. |
| <a id="slot2"></a>+16 | slot2 | `ptr` | V | Name/icon source: sub_140332CD0, or JobMenu_ReadJp in the job list. |
| <a id="slot3"></a>+24 | slot3 | `ptr` | V | Help/description: sub_140332D48. |
| <a id="slot4"></a>+32 | slot4 | `ptr` | V | Price: sub_14036A994 (shop) or sub_14036C468 (sell). |
| <a id="slot5"></a>+40 | slot5 | `ptr` | V | Equipped count: sub_14036A95C, or sub_140332C8C in the sell screen; JobScreen_FillUnitRows installs JobMenu_ReadNextLevelJp here for the job list. |
| <a id="slot6"></a>+48 | slot6 | `ptr` | V | Total count: sub_14036A924, or sub_140332C54 in the sell screen; JobScreen_FillUnitRows installs JobMenu_ReadTotalJp here for the job list. |

## Behavior

- V: sub_14036A9D8 (shop) and sub_14036C49C / sub_140333974 (equip and item pages) fill the same slots with the sub_140332Cxx readers, so those readers see two list kinds.
- V: JobScreen_FillUnitRows fills slots 0, 2, 5 and 6 with job-menu readers for the job list.

## Notes

V: the sheets sub_14036A9D8, sub_14036C49C, sub_140333974 and JobScreen_FillUnitRows.

## Open questions

? the exact column each slot draws; the gadget that reads the table is outside the exported set.
