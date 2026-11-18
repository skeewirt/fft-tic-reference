# SceneUnitShapeIsTheQueueWord

- **Kind:** observed behaviour
- **Scope:** engine (battle unit shape)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [Battle_BuildRosterTeam](../functions/Battle_BuildRosterTeam.md), [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md), [LookQueue_Add](../functions/LookQueue_Add.md), [SceneObject_FindByUnitIndex](../functions/SceneObject_FindByUnitIndex.md), [LookQueueEntry](../structs/LookQueueEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A scene unit's shape (sprite byte +0xA) is the sprite word of its load queue entry; a battle unit's shape byte +0x18F is written only by the unit builders and comes back in the battle snapshot, while the save keeps no shape byte.

## Behavior

- V: SceneUnit_BuildFromQueueEntry writes the scene unit's sprite byte +0xA from its sprite argument (bpl, 0x14026EDA0) and the pool index +9; its caller CharaPalette_ReloadForShape (load step 2) passes the queue entry's word +6 as that argument.
- V: Battle_BuildRosterTeam queues a placed unit with LookQueue_Add(unit +0x4F, +0x50, +0x51 >> 7, +0x51 & 0xF, shape, palette, 255, unit, 0) after Unit_ResolvePreviewShape (shape -> unit +0x18F, palette -> +0x190). The queue entry: bytes +0 / +1 / +2 = x, y, layer, word +4 facing, +6 sprite, +8 palette, +0xA slot, qword +0x10 unit, dword +0x18 flag; the loader passes them to SceneUnit_BuildFromQueueEntry in that order. M: the runtime test that ran LookQueue_Add on the mapped executable agreed.
- V: the battle unit record's shape +0x18F is written only by the unit builders through Unit_ResolvePreviewShape (marker + job rule) and comes back in the battle snapshot together with the unit table, the queue words +6, the 15 look pool records (+0 claim, +1 sprite) and g_UnitLookPoolIndex.
- I: the save's unit record (600 bytes) holds no shape byte: the menus and every fresh battle load derive the shape from the marker and the job byte (Unit_ResolvePreviewShape, from record bytes +0 and +2); the save slot summary stores up to four shapes, but only of Ramza and the guests 50..53, whose shape is their marker (job-independent). So only the battle snapshot keeps job-derived shape bytes.
- V: scene object +0x148 points at the battle unit record (g_PreviewUnitTable entry), +0xA is the sprite byte, +0x1E a byte the formation scales by 12, +0x15C bit 2 selects the formation's +0x2F test. SceneObject_FindByUnitIndex walks `g_SceneObjectList` for the object whose record has the given unit index (+444).

## Open questions

None recorded.
