# SaveData_Scramble

- **Address:** `0x1400341BC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `char SaveData_Scramble(uint64_t *in, uint64_t *out, uint64_t size)`
- **Callers:** SaveData_InflateEntry, SaveDataManager_vfunc_15, sub_140035A28, sub_140036064
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

XOR-scrambles (and unscrambles: it is its own inverse) a buffer with the container's fixed key.

## Behavior

- V (reimplemented and checked against real save files): XOR with 0x0F3F80FE5F1FC4F3 per 8 bytes, then 0x5F1FC4F3 for a 4-byte tail, 0x3B0C / 0x0C for 2 / 1-byte tails.

## Referenced by

- Called by: [SaveData_InflateEntry](SaveData_InflateEntry.md)
- Reads file formats: [SavePngContainer](../formats/SavePngContainer.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
