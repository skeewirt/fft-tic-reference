# CreditRoll_Step

- **Address:** `0x1401CB254`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int CreditRoll_Step(void *roll)`
- **Callers:** sub_1401BC3E4
- **Callees:** sub_1403DBBBC, UITable_GetRow, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1401BF788, sub_1401BF8C4, sub_1401BF828, UITable_GetRowByKey, sub_1401BE41C, sub_1401BE910, sub_1401BEF44, sub_1401BFEB4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steps the credit roll: reads the script rows and builds one line widget per row until the screen is full or the script ends.

## Behavior

- V: the script table is UITitleCredit (308) when byte +92 of the roll object is 1, else UIEndCredit (307); dword +72 is the next script row.
- V: for each script row: ui_credit_line_art (+4) non-zero looks up UICreditLineArt (304) and calls sub_1401BF788 with its string; sound_enhanced (+0xC) non-zero calls CreditRoll_StartMusic for the first row and CreditRoll_QueueMusic for later rows.
- V: then the UICreditRow keyed by the script row's ui_credit_row (+8) is read: its line_type (+4) selects the builder; types 1..4, 6 and 10 draw only when the row's +0xC is at least 1, type 5 only when +0x10 is non-zero.
- V: line types and builders: 1 sub_1401BE41C, 2 sub_1401BE518, 3 sub_1401BE614, 4 sub_1401BE710, 5 CreditRoll_AddPictureLine, 6 sub_1401BE80C, 7 sub_1401BE910, 8 sub_1401BEB20, 9 sub_1401BEC2C, 10 sub_1401BF90C, 11 sub_1401BFEB4 (ends the roll), 12 sub_1401BFA08, 17 sub_1401BFB04, 18 sub_1401BFD50, 25 sub_1401BF48C, 26 sub_1401BF6D0, 27 sub_1401BF198, 28 sub_1401BF294, 29 sub_1401BF390, 36 sub_1401BEA14, 39 sub_1401BF5DC; 16 and 19..24 draw nothing.
- V: any other type (0, 13..15 and so on) only adds the script row's spacing (+0x10, a signed byte) to the roll's y position (+548).
- V: the stepper stops when a builder returns true or the y position reaches 1080; at the end of the script it calls sub_1401BFEB4 and sets byte +93.
- V: the builders draw with their own template node of the roll object (+288, +312, +360 ...) through sub_1401BED40: type 7 uses nodes 'text01' and 'text02' (template +312), type 10 template +360 with the first caption.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)
- Writes: [CreditRoll.next_row](../structs/CreditRoll.md#next_row), [CreditRoll.y_position](../structs/CreditRoll.md#y_position), [CreditRoll.finished](../structs/CreditRoll.md#finished)

## Notes

Name is ours. The per-type builders are listed, not read.

## Open questions

? what each type's template looks like on screen.
