# ErrandActiveSlot

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 9 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One of the eight active errand slots at g_ErrandActive (9 bytes each, count g_ErrandActiveCount): a dispatch in progress or back, its errand, its days, the town it left from and up to three units.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flags"></a>`0x0` | flags | `uint8` | V | 1 when Errand_Start creates it; 0x04 when its days are done (the day ticks), 0x02 makes the day tick end it at once. |
| <a id="errand"></a>`0x1` | errand | `uint8` | V | The errand id (Errand_Start: the record's number word - 1); readers compare it with board entries and pass it to Errand_LoadRecord and EventVar(864 + it). |
| <a id="days_done"></a>`0x2` | days_done | `uint8` | V | Days so far; the daily tick adds 1, the calendar jump adds the days. |
| <a id="days"></a>`0x3` | days | `uint8` | V | The days chosen on dispatch (between the record's words 6 and 7). |
| <a id="town"></a>`0x4` | town | `uint8` | V | The settlement the units left from (dword_140D493E8 at dispatch); the board shows the errand returned (state 3) only there. |
| <a id="unit_count"></a>`0x5` | unit_count | `uint8` | V | 1..3. |
| <a id="units"></a>`0x6` | units | `uint8[3]` | V | Party record indices of the units sent (below 0x36: their g_UnitSaveData record +0x11E is the away byte). |

## Behavior

- V (Errand_Start, Errand_ApplyResult, Errand_Recall, sub_1402CCEE0): created at index count, removed by moving the later slots down 9 bytes.

## Referenced by

- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Open questions

None recorded.
