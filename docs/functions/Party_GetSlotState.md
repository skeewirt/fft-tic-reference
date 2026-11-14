# Party_GetSlotState

- **Address:** `0x140289298`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Party_GetSlotState(int party_slot)`
- **Callers:** sub_140288788, Party_GetSlotStateSpecial, sub_1402C20F0, sub_140332DB0, sub_140333974, sub_1403343E4, sub_1403358FC
- **Callees:** Job_IsHiddenFromTree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the availability state of one party slot: usable, absent, blocked or a special job, as a small signed code.

## Behavior

- V: a slot of 0x38 or above, or a negative slot, returns -1.
- V: the party unit pointer is g_PartyUnits[slot]; a non-zero byte at +0x167 returns -2.
- V: a non-zero word at +0x3E, or Job_IsHiddenFromTree on the job word at +0x24, returns -3.
- V: party unit +0x70 bit 2 returns -4.
- V: a job of 0x5D (93) returns -6 instead of 1.
- V: the normal usable result is 1.
- V: the four negative codes and the two positive values are the whole return set; there is no other branch.
- I: the codes are the party/errand list states: -1 bad slot, -2 absent, -3 blocked, -4 in use, -6 special job.
- ?: which screen maps which code to which label; the consumer switches were not read.

## State touched

- Calls: [Job_IsHiddenFromTree](Job_IsHiddenFromTree.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [Party_GetSlotStateSpecial](Party_GetSlotStateSpecial.md), [sub_140288788](sub_140288788.md), [sub_1402C20F0](sub_1402C20F0.md)

## Notes

Whole function read (134 bytes).

## Open questions

None recorded.
