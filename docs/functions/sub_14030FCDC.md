# sub_14030FCDC

- **Address:** `0x14030FCDC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int sub_14030FCDC(void *unit)`
- **Callers:** PartyUnit_FillFromWorkRecord, sub_140226CA0, sub_14039625C
- **Callees:** sub_14030FE18, sub_14030FFC4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the position of a unit's status in the 40-entry status display list and returns it, or one of the negative codes for the missing cases.

## Behavior

- V: It returns -1 when the unit's second byte is 0xFF.
- V: It calls the can-act predicate sub_14030FE18 first and returns -3 when that says the unit cannot act.
- V: It sets the UI core dword at +0x347C to 1 and builds the list with sub_14030FFC4.
- V: It scans up to 40 entries, comparing (entry & 0x1F) with the unit's status id from +0x1BC; a match returns the index and no match returns -2.
- V: Three callers: PartyUnit_FillFromWorkRecord, sub_140226CA0 and sub_14039625C.

## State touched

- Calls: [sub_14030FE18](sub_14030FE18.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)
- Writes: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Notes

V: the -1 / -3 / -2 are its return codes; the 40-entry bound is the 0x28 loop limit read here.

## Open questions

None recorded.
