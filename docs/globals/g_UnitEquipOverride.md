# g_UnitEquipOverride

- **Kind:** global
- **Address:** `0x14184A680`
- **Area:** [Unit data](../areas/unit-data.md)
- **Type:** `uint16[]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Five override equipment words per unit, ten bytes per unit index: when the pair is non-zero the equip pickers use it in place of the unit record's own hand words.

## Behavior

- V: sub_1402875A4 and sub_140287D9C read the override word for the selected unit and mark entries that match neither it nor the record word.

## Referenced by

- Described by tables: [UnitEquipOverride](../tables/UnitEquipOverride.md)
- Read by: [sub_1402875A4](../functions/sub_1402875A4.md), [sub_140287D9C](../functions/sub_140287D9C.md), [sub_1402D58EC](../functions/sub_1402D58EC.md), [sub_1402D5CC4](../functions/sub_1402D5CC4.md), [sub_1402D6464](../functions/sub_1402D6464.md), [sub_1402D64CC](../functions/sub_1402D64CC.md), [sub_1402D65D4](../functions/sub_1402D65D4.md), [sub_1402D6914](../functions/sub_1402D6914.md), [sub_1402D6FB8](../functions/sub_1402D6FB8.md), [sub_1402D7280](../functions/sub_1402D7280.md), [sub_1402D7584](../functions/sub_1402D7584.md)
- Written by: [sub_1402D5CC4](../functions/sub_1402D5CC4.md), [sub_1402D6464](../functions/sub_1402D6464.md), [sub_1402D64CC](../functions/sub_1402D64CC.md), [sub_1402D65D4](../functions/sub_1402D65D4.md), [sub_1402D6914](../functions/sub_1402D6914.md)

## Notes

V: five words per unit, ten bytes per unit index, at 0x14184A680. sub_1402D6464 stores a non-flagged unit word here before clearing the slot; sub_1402D5B6C restores it on cancel; sub_1402D65D4 returns it to the inventory on commit. A bit-14 word can be stored here (the 0x8000 test does not reject it) but no stock writer produces one on a unit word.

## Open questions

None recorded.
