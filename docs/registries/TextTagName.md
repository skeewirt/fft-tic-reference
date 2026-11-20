# TextTagName

- **Kind:** registry
- **Area:** [Data access](../areas/data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The first 40 records of the UI text engine's tag-name table (16 bytes each: a name pointer and a flag dword). A text tag is looked up in it by name; the four counted-noun tags are the last four of these records.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="nil"></a>0 | `nil` | `0` | V | First record; flag 1. |
| <a id="br"></a>1 | `br` | `1` | V | Flag 1. |
| <a id="nbsp"></a>2 | `nbsp` | `2` | V | Flag 1. |
| <a id="--"></a>3 | `--` | `3` | V | Flag 1. |
| <a id="string"></a>4 | `string` | `4` | V | Flag 1. |
| <a id="num"></a>5 | `num` | `5` | V | Flag 1. |
| <a id="kilo"></a>6 | `kilo` | `6` | V | Flag 1. |
| <a id="if"></a>7 | `if` | `7` | V | Flag 1. |
| <a id="switch"></a>8 | `switch` | `8` | V | Flag 1. |
| <a id="head"></a>9 | `head` | `9` | V | Flag 1. |
| <a id="headall"></a>10 | `headall` | `10` | V | Flag 1. |
| <a id="lower"></a>11 | `lower` | `11` | V | Flag 1. |
| <a id="disp"></a>12 | `disp` | `12` | V | Flag 1. |
| <a id="hide"></a>13 | `hide` | `13` | V | Flag 1. |
| <a id="cmt"></a>14 | `cmt` | `14` | V | Flag 0. |
| <a id="b"></a>15 | `b` | `15` | V | Flag 0. |
| <a id="i"></a>16 | `i` | `16` | V | Flag 0. |
| <a id="left"></a>17 | `left` | `17` | V | Flag 0. |
| <a id="center"></a>18 | `center` | `18` | V | Flag 0. |
| <a id="right"></a>19 | `right` | `19` | V | Flag 0. |
| <a id="just"></a>20 | `just` | `20` | V | Flag 0. |
| <a id="color"></a>21 | `color` | `21` | V | Flag 0. |
| <a id="scale"></a>22 | `scale` | `22` | V | Flag 1. |
| <a id="xy"></a>23 | `xy` | `23` | V | Flag 1. |
| <a id="x"></a>24 | `x` | `24` | V | Flag 1. |
| <a id="y"></a>25 | `y` | `25` | V | Flag 1. |
| <a id="icon"></a>26 | `icon` | `26` | V | Flag 1. |
| <a id="keyicon"></a>27 | `keyicon` | `27` | V | Flag 1; the button glyph of a named input action (TextTag_ExpandKeyIcon). |
| <a id="moveicon"></a>28 | `moveicon` | `28` | V | Flag 1. |
| <a id="moveicon2"></a>29 | `moveicon2` | `29` | V | Flag 1. |
| <a id="cameraicon"></a>30 | `cameraicon` | `30` | V | Flag 1. |
| <a id="aimicon"></a>31 | `aimicon` | `31` | V | Flag 1. |
| <a id="player"></a>32 | `player` | `32` | V | Flag 1. |
| <a id="speaker"></a>33 | `speaker` | `33` | V | Flag 1. |
| <a id="date"></a>34 | `date` | `34` | V | Flag 1. |
| <a id="time"></a>35 | `time` | `35` | V | Flag 1. |
| <a id="ennoun"></a>36 | `ennoun` | `36` | V | Flag 1; counted noun with an English article (TextTag_CountedNounArticle: arguments category, key, count, article kind). |
| <a id="denoun"></a>37 | `denoun` | `37` | V | Flag 1; counted noun with a German form (TextTag_CountedNounForms: five arguments). |
| <a id="frnoun"></a>38 | `frnoun` | `38` | V | Flag 1; counted noun with a French form (TextTag_CountedNounIndexed: four arguments). |
| <a id="esnoun"></a>39 | `esnoun` | `39` | V | Flag 1; counted noun with no grammar byte (TextTag_CountedNounPlain: four arguments). |

## Behavior

- V: TextTag_ExpandKeyIcon compares the tag name (4 + 2 bytes for the noun tags) and calls the matching builder.

## Notes

The table starts at 0x14066F710 in the executable; the meaning of the flag dword (1 / 0) is not decoded. The name of each tag is the engine's own syntax word.

## Open questions

? the meaning of the flag dword; whether the table has records after index 39.
