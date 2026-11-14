# StatusScreen_BuildLists

- **Address:** `0x140112A04`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 StatusScreen_BuildLists(char *screen, _BYTE *set, _BYTE *countdowns)`
- **Callers:** JobScreen_RefreshAfterChange, sub_1402078A8
- **Callees:** sub_1400FAAB4, qsort, sub_140112B48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the Status screen's two status lists (gains, ailments) from a five-byte status set, sorts them and draws them.

## Behavior

- V: clears both counts (+0x188, +0x18C) and sets the 40 dwords of each list (+0x48, +0xE8) to -1.
- V: walks the 40 bits of the set byte by byte from bit 7 down (status = 8 x byte + position from the top bit) and puts each set status into the gains list when Status_ListCategory gives 1, into the ailments list when it gives 2.
- V: sorts both lists with qsort and CompareFunction (Status_ListSortKey), copies the 16 countdown bytes to +0x19C, then tail-jumps to StatusScreen_DrawLists.

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours. The lists hold dwords, so any status id fits; 40 entries each. The sort follows the loop (the code after the loop is at 0x140112ACF).

## Open questions

None recorded.
