# BattleMsg_TextFromDescriptor

- **Address:** `0x1400FCBB4`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `const char *BattleMsg_TextFromDescriptor(BattleMsgDescriptor *desc)`
- **Callers:** UIMessageBanner_Show
- **Callees:** UIText_Get, CMesId_GetText, BattleMsg_IdFromDescriptor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the template text for a message descriptor from one of two text sources.

## Behavior

- V: class 1 subtype 27 returns UIText_Get(word).
- V: class 1 subtype 171 returns the table-172 text of word (CMesId_GetText with word as the row id).
- V: class 0 subtype 2 returns the table-172 text of BattleMsg_IdFromDescriptor(desc).
- V: any other input returns null.
- V: the result is the template string; the stored text keeps its tags such as <string=lstr0> / <num=...>.

## State touched

- Calls: [UIText_Get](UIText_Get.md), [CMesId_GetText](CMesId_GetText.md), [BattleMsg_IdFromDescriptor](BattleMsg_IdFromDescriptor.md)

## Referenced by

- Called by: [ErrorBanner_Show](ErrorBanner_Show.md), [UIMessageBanner_Show](UIMessageBanner_Show.md)

## Notes

The name is ours (IDB: sub_1400FCBB4). The function is 80 bytes.

## Open questions

What uses class 1 subtype 171; what table UIText_Get reads (not recorded).
