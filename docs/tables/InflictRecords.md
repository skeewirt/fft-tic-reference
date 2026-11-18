# InflictRecords

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14080FBA0`
- **Rows:** 128 rows of 6 bytes
- **Keyed by:** inflict index (weapon byte +7, chemist byte +2, action record byte +11)
- **Read by:** [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [sub_1400FA7AC](../functions/sub_1400FA7AC.md), [sub_1400FA94C](../functions/sub_1400FA94C.md), [sub_140388EB4](../functions/sub_140388EB4.md)
- **Row layout:** [InflictRecordRow](../structs/InflictRecordRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Statuses an attack, item or ability inflicts or cures.

## Behavior

- V: the weapon record, chemist record and ability action record all index this table.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
