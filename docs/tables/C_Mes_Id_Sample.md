# C_Mes_Id_Sample

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 172
- **Keyed by:** message id
- **Read by:** [CMesId_GetText](../functions/CMesId_GetText.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md)
- **Held in:** [g_CMesIdTable](../globals/g_CMesIdTable.md)
- **Row layout:** [NxdDataC_Mes_Id_SampleRow](../structs/NxdDataC_Mes_Id_SampleRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle message text table: CMesId_GetText reads one row by message id and the registry result is cached in g_CMesIdTable.

## Behavior

- V: CMesId_GetText calls NxdRegistry_Find with id 172 and keeps the result; a missing row gives null.

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
