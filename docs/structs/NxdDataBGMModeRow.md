# NxdDataBGMModeRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.bgm_mode table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="tab"></a>`0x8` | tab | `int32` | V | Read in the code: The tab of the music player (BGM Mode screen) the track is listed under: 0 the first tab, 1 the second. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="title_alt"></a>`0xC` | title_alt | `string (int32 offset)` | V | Read in the code: A second title of the track, shown instead of title when the player switches the list's title language (action 195), which is offered only for languages 2 and 3. Observed in the stock rows: 97 distinct values, 0 empty. |
| <a id="title"></a>`0x10` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 97 distinct values, 0 empty. |
| <a id="sound_enhanced"></a>`0x14` | sound_enhanced | `int32` | M | Measured over every stock row: Every value is a key of nxd.SoundEnhanced. Observed in the stock rows: 150 to 246, 97 distinct values. |

## Referenced by

- Described by tables: [NxdDataBGMMode](../tables/NxdDataBGMMode.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
