# UnitWork_CopySaveFields

- **Address:** `0x140276758`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int UnitWork_CopySaveFields(uint8_t *work, const uint8_t *save)`
- **Callers:** UnitWork_BuildFromSave, sub_140275EF4
- **Callees:** sub_14002630C (block copy)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the fields of a save unit record A into the work record C. It defines the A -> C offset mapping.

## Behavior

- V: single bytes: C+0 = A+0 (marker byte), C+2 = A+1 (slot id), C+3 = A+2 (job id), C+6 = A+4 (flags), C+19 = A+7, C+500 = A+289 (story stage).
- V: C+4 = A+3 only when the slot id is 0x32 or higher, else 0; C+5 and C+494 are set to 11 when the marker is below 4, otherwise 8.
- V: C+8 (word) gets a 9-bit value from A+5 / A+6 and a 4-bit value from the top nibble of A+6 in bits 12..15; words C+20, C+22, C+24 are built from byte pairs A+8..13; C+26 takes 14 bytes from A+14.
- V: C+40 = A+28, C+41 = A+29, C+42 and C+43 = A+30, C+44 and C+45 = A+31; A+32..46 land at C+123..137 as a mix of words and bytes.
- V: the 3-byte unlock mask A+47..49 goes to C+159..161.
- V: block copies: A+50 (66 bytes, learned-ability bits) -> C+162; A+116 (12 bytes, job levels) -> C+228; A+128 (46 bytes, current JP) -> C+240; A+174 (46 bytes, second JP array) -> C+286; A+220 (64 bytes) -> C+332; dword A+560 -> C+508.
- V: zeroes C+407 (dword), C+411 (word) and C+413.

## Referenced by

- Called by: [UnitWork_BuildFromSave](UnitWork_BuildFromSave.md), [sub_140275EF4](sub_140275EF4.md)

## Notes

Offsets A+116 and C+228 are both the 24-nibble job level array; the mask, learned bits and JP arrays move by a constant per block, not uniformly.

## Open questions

None recorded.
