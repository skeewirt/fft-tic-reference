# CreditLineType

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The line types of UICreditRow (line_type) and the builder CreditRoll_Step calls for each.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="type_1"></a>1 | `type_1` | `sub_1401BE41C` | V | Template +288, node 'text'; drawn only when row +0xC is at least 1. |
| <a id="type_2"></a>2 | `type_2` | `sub_1401BE518` | V | Drawn only when row +0xC is at least 1. |
| <a id="type_3"></a>3 | `type_3` | `sub_1401BE614` | V | Drawn only when row +0xC is at least 1. |
| <a id="type_4"></a>4 | `type_4` | `sub_1401BE710` | V | Drawn only when row +0xC is at least 1. |
| <a id="picture"></a>5 | `picture` | `CreditRoll_AddPictureLine` | V | Picture line (icon, icon_height); drawn only when row +0x10 is non-zero. No stock row uses it. |
| <a id="type_6"></a>6 | `type_6` | `sub_1401BE80C` | V | Drawn only when row +0xC is at least 1. |
| <a id="name_line"></a>7 | `name_line` | `sub_1401BE910` | V | Template +312, nodes 'text01' and 'text02'; the common name line (792 rows). |
| <a id="type_8"></a>8 | `type_8` | `sub_1401BEB20` | V | Builder not read. |
| <a id="type_9"></a>9 | `type_9` | `sub_1401BEC2C` | V | Builder not read. |
| <a id="type_10"></a>10 | `type_10` | `sub_1401BF90C` | V | Template +360, node 'text', first caption; drawn only when row +0xC is at least 1. |
| <a id="end"></a>11 | `end` | `sub_1401BFEB4` | V | Ends the roll (byte +93 = 1). |
| <a id="type_12"></a>12 | `type_12` | `sub_1401BFA08` | V | Builder not read. |
| <a id="two_captions"></a>17 | `two_captions` | `sub_1401BFB04` | V | Two captions. |
| <a id="type_18"></a>18 | `type_18` | `sub_1401BFD50` | V | Builder not read. |
| <a id="type_25"></a>25 | `type_25` | `sub_1401BF48C` | V | Builder not read. |
| <a id="type_26"></a>26 | `type_26` | `sub_1401BF6D0` | V | Builder plus a reset. |
| <a id="type_27"></a>27 | `type_27` | `sub_1401BF198` | V | Builder not read. |
| <a id="type_28"></a>28 | `type_28` | `sub_1401BF294` | V | Builder not read. |
| <a id="type_29"></a>29 | `type_29` | `sub_1401BF390` | V | Builder not read. |
| <a id="type_36"></a>36 | `type_36` | `sub_1401BEA14` | V | Builder not read. |
| <a id="type_39"></a>39 | `type_39` | `sub_1401BF5DC` | V | Builder not read. |
| <a id="spacing_only"></a>0 | `spacing_only` | `none` | V | Only adds the script spacing to the y position; 226 of the 227 rows without captions use it. |

## Behavior

- V: types 16 and 19..24 draw nothing; any other value only adds the spacing.

## Open questions

? what each template looks like on screen.
