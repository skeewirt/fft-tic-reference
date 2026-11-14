# g_MessageDescriptor

- **Kind:** global
- **Address:** `0x140783210`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[?]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The current battle message descriptor: the message word at +0, the item id at +4 and the text id at +8.

## Behavior

- V: BattleMsg_Dispatch writes the item id and the 0x3800-based text id of the item message; sub_140243390 fills the word and the dword from its record.

## Referenced by

- Written by: [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md), [sub_140243390](../functions/sub_140243390.md)

## Open questions

None recorded.
