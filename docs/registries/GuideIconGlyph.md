# GuideIconGlyph

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The guide icon numbers (UIButtonGuide guide_icon / guide_icon_2) and the glyph GuideIcon_ToGlyph draws for them.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="icon_1"></a>1 | `icon_1` | `slot 26` | V | Goes to the glyph slot function with 26. |
| <a id="icon_2"></a>2 | `icon_2` | `slot 27` | V | Same with 27. |
| <a id="icon_13"></a>13 | `icon_13` | `11` | V | Always drawn. |
| <a id="icon_15"></a>15 | `icon_15` | `16` | V | Always drawn. |
| <a id="icon_16"></a>16 | `icon_16` | `17` | V | Always drawn. |
| <a id="icon_17"></a>17 | `icon_17` | `18` | V | Always drawn. |
| <a id="icon_18"></a>18 | `icon_18` | `19` | V | Always drawn. |
| <a id="icon_19"></a>19 | `icon_19` | `13` | V | Always drawn. |
| <a id="icon_3"></a>3 | `icon_3` | `3` | V | Only with variant byte 0. |
| <a id="icon_4"></a>4 | `icon_4` | `1` | V | Only with variant byte 0. |
| <a id="icon_5"></a>5 | `icon_5` | `2` | V | Only with variant byte 0. |
| <a id="icon_6"></a>6 | `icon_6` | `4` | V | Only with variant byte 0. |
| <a id="icon_7"></a>7 | `icon_7` | `5` | V | Only with variant byte 0. |
| <a id="icon_8"></a>8 | `icon_8` | `8` | V | Only with variant byte 0. |
| <a id="icon_9"></a>9 | `icon_9` | `6` | V | Only with variant byte 0. |
| <a id="icon_10"></a>10 | `icon_10` | `9` | V | Only with variant byte 0. |
| <a id="icon_11"></a>11 | `icon_11` | `7` | V | Only with variant byte 0. |
| <a id="icon_12"></a>12 | `icon_12` | `10` | V | Only with variant byte 0. |
| <a id="icon_14"></a>14 | `icon_14` | `12` | V | Only with variant byte 0. |
| <a id="icon_20"></a>20 | `icon_20` | `14` | V | Only with variant byte 0; in the stock rows icon 20 marks the four-direction group and 155 is its keyboard key texture. |
| <a id="icon_21"></a>21 | `icon_21` | `15` | V | Only with variant byte 0. |

## Behavior

- V: with a non-zero variant byte the icons 3..12, 14, 20 and 21 draw nothing; the stock variant bytes are 1 only on rows that show an action and no icon.

## Notes

Glyph numbers are the numbers GuideIcon_ToGlyph passes on; what each glyph looks like is not decoded.

## Open questions

? the meaning of the variant byte.
