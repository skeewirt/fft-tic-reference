# GUIFontTable_Load

- **Address:** `0x1403D9728`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIFontTable_Load(_QWORD *table, __int64 unused1, __int64 unused2)`
- **Callers:** sub_1403D5934 (0x1403D5A25)
- **Callees:** sub_1403DBBBC, UITable_GetRow, UIFontSetRow_Default, sub_1403EEECC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the in-memory UIFontSet row vector from UI table id 21: each 80-byte row starts from UIFontSetRow_Default and is then overwritten field by field from the source record.

## Behavior

- V: table[3] = table[2] (end = begin: the vector is emptied first). Vector members: begin table[2], end table[3], cap table[4] (the `a1+1` base is passed to the grow helper sub_1403EEECC).
- V: count = sub_1403DBBBC(21); for i in 0..count-1, src = UITable_GetRow(21, i); dst row is built on the stack (80 bytes) with UIFontSetRow_Default first.
- V: field copy (src offset -> dst offset): +4 -> +0, +8 -> +4, +12 -> +12... precisely: src dwords 1,2,3 -> dst +0, +4, +12; src +84..+87 (4 bytes) -> dst +8; src dword 4 -> dst +20, dword 5 -> +24; dword 22 -> +16(low of 2nd qword group), 23 -> +20 region, 24 -> +24 region as decompiled (stack-temporary layout, see raw decompile); src +56, +72, +76, +80 bytes -> dst bytes at +68..+74 area.
- V: if end == cap it calls the grow helper sub_1403EEECC(table+1, end, &tmp); else copies five 16-byte blocks to *end and adds 80 to table[3].
- V: callers: sub_1403D5934 (0x1403D5A25) and a data ref 0x143D41560.
- I: the column to field mapping above is only approximate: the decompiler merged the stack temporary into overlapping xmm stores. Treat exact offsets as ? until the per-row layout is read from disassembly.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md), [UIFontSetRow_Default](UIFontSetRow_Default.md)

## Referenced by

- Called by: [UiNames_InstallCoreNames](UiNames_InstallCoreNames.md)

## Notes

Row size 80 is confirmed by both Load (add 80) and GetSetRow (/80 and *80). The UIFontSet table id is 21 (V: literal 21 in both calls).

## Open questions

? exact per-column mapping (see behaviour 3). ? what the source row size is (largest src offset read is +87).
