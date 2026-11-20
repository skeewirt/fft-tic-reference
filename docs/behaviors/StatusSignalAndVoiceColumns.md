# StatusSignalAndVoiceColumns

- **Kind:** observed behaviour
- **Scope:** engine (battle status effects)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [UnitPanel_SetSignalList](../functions/UnitPanel_SetSignalList.md), [sub_140217A7C](../functions/sub_140217A7C.md), [Status_ListCategory](../functions/Status_ListCategory.md), [StatusVoice_SpeakEvent](../functions/StatusVoice_SpeakEvent.md), [StatusVoice_CacheLines](../functions/StatusVoice_CacheLines.md), [Status_ListSortKey](../functions/Status_ListSortKey.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Three UIStatusEffect columns decide what a status does in the battle UI: whether it is listed and raises a signal, which BattleSignal popup it shows, and which battle voice line it speaks.

## Behavior

- V: a status list (ids, bit 0x80 = removed) becomes the BattleSignal list of a panel: the UIStatusEffect row of key status id + 1 is used only when list_category (+0x14) is non-zero and battle_signal (+0x18) is not 59, and the BattleSignal row (table 214) of that key must exist (UnitPanel_SetSignalList, sub_140217A7C).
- V: the voice for a status event is chosen by StatusVoice_SpeakEvent from battle_voice (+0x1C) of every status in the event's 41-bit mask: all non-zero values must agree, then the controller's IsSuppressed (virtual slot 5) and Speak (slot 3) are called with that line.
- V: StatusVoice_CacheLines copies battle_voice of rows 1..40 into BattleControl +693504 at battle start; no reader of that array was found.
- M: stock battle_voice is 15 for ailments and 23 for gains.
- V: the sort_order column (+0x20, int16) orders the Status screen lists (Status_ListSortKey); hidden_in_equipment_detail (+0x22) keeps a status name out of the equipment detail status lines (EquipDetail_BuildCategoryLines).

## Open questions

None recorded.
