# Ability

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** NXD file
- **NXD table id:** 39
- **Keyed by:** ability id
- **Read by:** [AbilityTable_GetRow](../functions/AbilityTable_GetRow.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The ability rows the game reads through AbilityTable_GetRow, loaded lazily and cached. The columns are not all decoded.

## Behavior

- V: UIText_ResolveCategoryRow sends the category 'Ability' to table 0x27 (39).
- I: AbilityTable_GetRow reads this same table (its page names the Ability NXD row but not the id).

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
