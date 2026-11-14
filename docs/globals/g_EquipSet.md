# g_EquipSet

- **Kind:** global
- **Address:** `0x141876C40`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `?`
- **Points to / is a:** [EquipSetBlock](../structs/EquipSetBlock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The equip-set structure the preview picker fills and passes to sub_140287354 together with the candidate buffer and the unit's live equipment words.

## Behavior

- V: sub_140333FE0 passes it and the five-word candidate buffer to sub_140287354.

## Referenced by

- Read by: [sub_1402C20F0](../functions/sub_1402C20F0.md), [sub_1402D58EC](../functions/sub_1402D58EC.md), [sub_1402D5CC4](../functions/sub_1402D5CC4.md), [sub_1402D6914](../functions/sub_1402D6914.md), [sub_1402D746C](../functions/sub_1402D746C.md), [sub_14032EDB8](../functions/sub_14032EDB8.md), [sub_14032F410](../functions/sub_14032F410.md), [sub_140333FE0](../functions/sub_140333FE0.md), [sub_140336444](../functions/sub_140336444.md), [sub_14036BBFC](../functions/sub_14036BBFC.md), [sub_14036C320](../functions/sub_14036C320.md)

## Notes

V: the block is 0x40 bytes at 0x141876C40; +0x24 is g_EquipCandidates (0x141876C64) and +0x10 is the two-handed word at 0x141876C50. sub_140287354 clears it and fills the stat words; sub_140287D9C fills four candidate words, not five.

## Open questions

None recorded.
