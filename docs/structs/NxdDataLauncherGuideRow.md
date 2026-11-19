# NxdDataLauncherGuideRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.launcher_guide table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="icon"></a>`0x4` | icon | `int32` | V | Read in the code: An Icon id (table 118): the picture shown on an info page. Observed in the stock rows: 0 to 1006, 7 distinct values. |
| <a id="caption"></a>`0x8` | caption | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 13 distinct values, 10 empty. |
| <a id="controls_page"></a>`0xC` | controls_page | `uint8` | V | Read in the code: Marks the page that shows the controls: it is drawn by sub_1401BB9D8 ('Info' state, the controls panel shown) and filled from table 278. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="start_page"></a>`0xD` | start_page | `uint8` | V | Read in the code: Marks the guide page that carries the Start button: the launcher keeps it in the page list only when byte +614 is set (actions 110 / 112), draws it with the 'Start' state and a ButtonStart (UI text 2214) and puts the focus on that button. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataLauncherGuide](../tables/NxdDataLauncherGuide.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
