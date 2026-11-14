# FormatArgs_Push

- **Address:** `0x1400FE4E4`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void FormatArgs_Push(FormatArgVec *vec, const void *entry)`
- **Callers:** 120 direct sites, including BattleMsg_FillArgs, UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs, ItemCell_BindIconAndName, sub_140142014, sub_14014AC94 and sub_14014ADC8
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends one 264-byte format-argument record to a format-argument vector.

## Behavior

- V: appends one 264-byte (0x108) record: a 256-byte string area and a type dword at +256; the copy ends with the qword at source +256.
- V: the write pointer is at +0x10 of the part/vector object it is given and the end pointer at +0x18; the write pointer advances by 264.
- V: the type dword is 1 for an integer argument; any other value marks a string argument (the item-name path passes 4).
- V: when the write pointer equals the end pointer it does not copy: it jumps to the buffer's grow/append routine instead (a conditional jump to the thunk at 0x1400FE55B, which jmps to sub_1400FE9D0).
- V: 120 direct call sites; the item-cell binder uses it for the icon path and for the item id/argument block.
- V: the job-detail setter UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs pushes two records through it (job id and a flag, both type 1).
- I: the 264-byte block is a small string table entry: the item binder passes an id, a size and a type alongside the text.
- ?: the ring's capacity, whether the write pointer wraps, and who drains it.

## Referenced by

- Called by: [BattleMsg_BuildArgs](BattleMsg_BuildArgs.md), [BattleMsg_FillArgs](BattleMsg_FillArgs.md), [ItemCell_BindIconAndName](ItemCell_BindIconAndName.md), [UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs](UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs.md), [sub_140109134](sub_140109134.md), [sub_140142014](sub_140142014.md)

## Notes

The name is ours (IDB: sub_1400FE4E4). The record shape is the one GUIText_Expand consumes. Whole body read (0x77 bytes, 119); the grow routine was not read.

## Open questions

The full set of type values and how GUIText_Expand interprets each; the vector growth policy (not read); the block layout beyond the first dword.
