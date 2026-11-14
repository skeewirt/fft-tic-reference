# g_BattleMsgObject

- **Kind:** global
- **Address:** `0x143CDA388`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `ptr`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the battle message object. I: the object is the message manager: it holds the battle message record at +8 and up to 40 stored argument entries at +12 (524-byte stride), the two things the banner's argument filler reads. V: Battle_Init clears 0x51E0 bytes at +8, and 46 functions reference the qword.

## Behavior

- V: 46 functions reference the qword (cross-reference count in the 2026-10-31 study).
- V: Battle_Init clears 0x51E0 bytes at +8 (the record area).
- I: the role as battle message manager; no single function owns the object's layout.

## Referenced by

- Read by: [BattleMsg_SetKind1](../functions/BattleMsg_SetKind1.md), [sub_1401EC01C](../functions/sub_1401EC01C.md), [sub_1402371F8](../functions/sub_1402371F8.md)
- Written by: [BattleMsg_SetKind1](../functions/BattleMsg_SetKind1.md), [sub_140237CD0](../functions/sub_140237CD0.md)

## Notes

The object's fields other than +8 and +12 are not decoded (?).

## Open questions

? the object's full layout; ? where it is created; ? the stored argument entry layout (524 bytes).
