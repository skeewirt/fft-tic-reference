# g_ErrandBoardList

- **Kind:** global
- **Address:** `0x140D498F0`
- **Type:** `errands`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint16[128]: the tavern board list: an entry is a kind in the top 5 bits and an 11-bit id (an errand is errand - 0x3000 = 0xD000 + errand; 0xB800 is another kind, sub_1403456D4). Errand_BuildBoard and Errand_BuildActiveList fill it, the board UI reads `& 0x7FF`; the builder range-checks the index against 0x100 bytes

## Referenced by

- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)
- Written by: [Errand_BuildActiveList](../functions/Errand_BuildActiveList.md)

## Open questions

None recorded.
