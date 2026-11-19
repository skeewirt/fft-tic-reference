# BattleVoice_IsSuppressed

- **Address:** `0x1401ED4E0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleVoice_IsSuppressed(void *controller, void *request, int line)`
- **Callers:** none (virtual call)
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides by sides whether a battle voice line is spoken: 0 speak, or a reason 1..5 to suppress (CharacterBattleVoiceController virtual, slot 5).

## Behavior

- V: runs only when the BattleVoice row's side (+0x20) is non-zero; side 0 never suppresses.
- V: with side_test_on_unit (+0x28) set the test is on one unit, the request's unit (request +12; the speaker itself when 0xFF): the same slot as the speaker returns 3; the same side ((unit +494 xor other +494) & 0x30 == 0) suppresses unless side is 2; the other side suppresses when side is 2.
- V: with +0x28 clear the same side test runs over the request's target list (+24..+32): side 2 is spoken only when every target is on the speaker's side (else 5); otherwise it is spoken only when every target is on the other side (else 4).
- V: the sides are read as bits 0x30 of unit byte +494.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)

## Notes

Name is ours. Vtable 0x140713F68.

## Open questions

? what fills request byte +12 (which unit the request names): the request builder was not found.
