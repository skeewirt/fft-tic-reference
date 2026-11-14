# g_EquipCandidates

- **Kind:** global
- **Address:** `0x141876C64`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint16[5]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The five candidate equipment words of the equip screen's preview; filled by the picker or zeroed, then read by the caller after the call.

## Behavior

- V: five words, one per equipment slot (sub_140333FE0 zeroes it or fills it from sub_1402875A4).

## Referenced by

- Read by: [sub_1402C20F0](../functions/sub_1402C20F0.md), [sub_1402D6FB8](../functions/sub_1402D6FB8.md), [sub_1402D746C](../functions/sub_1402D746C.md), [sub_140333FE0](../functions/sub_140333FE0.md), [sub_14036C2A8](../functions/sub_14036C2A8.md), [sub_14036C320](../functions/sub_14036C320.md)
- Written by: [sub_1402C20F0](../functions/sub_1402C20F0.md), [sub_1402D5CC4](../functions/sub_1402D5CC4.md), [sub_1402D6914](../functions/sub_1402D6914.md), [sub_1402D746C](../functions/sub_1402D746C.md), [sub_140333FE0](../functions/sub_140333FE0.md), [sub_14036C2A8](../functions/sub_14036C2A8.md)

## Notes

V: five words at 0x141876C64..0x141876C6D, the +0x24 field of g_EquipSet. sub_140287D9C marks the first four with 0x8000; the fifth (0x141876C6C) is copied from the unit's +0x5C by sub_1402D5CC4, sub_1402D6914, sub_1402D746C, sub_1402C20F0 and sub_14036C2A8. A flagged word in the source travels with the copy.

## Open questions

None recorded.
