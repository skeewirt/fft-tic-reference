# g_TurnList

- **Kind:** global
- **Address:** `0x140D40490`
- **Type:** `battle action data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

40 x 4 bytes: byte 0 = unit (bits 0..4, 31 = end) | 0x20 command 18 | 0x40 pending action | 0x80 ability bit 8; byte 1 = ability low byte; word +2 = time. Copied from the list TurnList_BuildForSelection builds; read by the panel (TurnPanel_*)

## Referenced by

- Read by: [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md)

## Open questions

None recorded.
