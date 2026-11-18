# MsgWindow_BuildFrame

- **Address:** `0x14022BFEC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MsgWindow_BuildFrame(short *rect, short *spec, void *window)`
- **Callers:** SceneMsgTask_Run and eleven other message tasks
- **Callees:** sub_140242AFC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up the frame primitives of a message window and its decoration cells by window kind and language.

## Behavior

- V: window kinds 0..4 place one cell from a per-language table of five (0x1407B27E8..0x1407B28A8).
- V: kinds 5..9 place four cells from the per-language decoration tables (0x1407B2AD0 language 0, 0x1407B29E0 default, 0x1407B28F0 language 2, 0x1407B2BC0 language 3), starting at (kind - 5) x 4.

## State touched

- Calls: [sub_140242AFC](sub_140242AFC.md)

## Referenced by

- Reads tables: [MessageWindowTagCellsDefault](../tables/MessageWindowTagCellsDefault.md), [MessageWindowTagCellsLanguage0](../tables/MessageWindowTagCellsLanguage0.md), [MessageWindowTagCellsLanguage2](../tables/MessageWindowTagCellsLanguage2.md), [MessageWindowTagCellsLanguage3](../tables/MessageWindowTagCellsLanguage3.md)

## Notes

Read: the cell selection.

## Open questions

None recorded.
