# SceneUnit_TestGroupMember

- **Address:** `0x1402408F0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int SceneUnit_TestGroupMember(uint16_t *id, uint16_t key, int32_t *groupMode)`
- **Callers:** EventScript_Run (opcode 0x80 through the call at 0x14023D735 and opcode 0x81 through the call at 0x14023D7BB, both as the loop test); SceneGroup_SetFlag04 (opcodes 0x6C and 0x6D); the helper bodies listed under SceneGroup_ResolveId.
- **Callees:** SceneObject_FindBySlot (unit lookup), ScenePreview_IndexOfSlot (preview index of a unit)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests whether unit key 'key' (0 to 20 in the callers' loops) is a member of the group selected by *groupMode. Used in a loop over 21 keys by the callers of SceneGroup_ResolveId.

## Behavior

- V: if *groupMode is 0 it returns 1 at once, without writing *id. That case is a single unit whose id was already resolved, so the caller's loop runs once.
- V: for any other mode it first writes key to *id, then calls SceneObject_FindBySlot(key) to find the unit node. Without a node it returns 0 for every mode.
- V: with a node, it calls ScenePreview_IndexOfSlot(key) to get the preview index: the byte at node+0x148 then +0x1BC, or -1 when there is no such record. An index of 0 to 20 selects the entry g_BattleUnitTable + index*512; otherwise there is no entry.
- V: mode 1 (from id 0) returns 1 for every key that has a unit node.
- V: mode 2 returns 1 when the preview index is -1. Otherwise it returns 1 only when the entry's byte +5 has bits 0x30 clear.
- V: mode 3 returns 1 when the preview index is -1. Otherwise it returns 1 only when none of the five bytes +97 to +101 of the entry is nonzero (each mask byte at 0x1411A6A98 to 0x1411A6A9C reads as 0xFF) and the entry's byte +5 has bits 0x30 clear.
- V: mode 4 returns 1 only when the preview index is 0 to 20 and the entry's byte +5 has bits 0x30 set.
- V: mode 5 returns 1 only when the preview index is 0 to 20, the entry's byte +5 has bits 0x30 set, and none of the bytes +97 to +101 is nonzero, with bit 0x10 of byte +97 ignored.
- V: modes 6 and above return 0 for every key.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md)

## Referenced by

- Called by: [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [SceneGroup_SetFlag04](SceneGroup_SetFlag04.md), [ScenePlacement_WriteGroup](ScenePlacement_WriteGroup.md), [ScenePlacement_WritePair](ScenePlacement_WritePair.md), [SceneUnit_ApplyModeAndAction](SceneUnit_ApplyModeAndAction.md)

## Notes

The mode values are the ones SceneGroup_ResolveId writes. Mode 0 means a single unit; modes 1 to 5 are the group kinds read from the code.

## Open questions

What the mask bytes at 0x1411A6A98 to 0x1411A6A9C mean in the game (they all read 0xFF in the file), and what bytes +97 to +101 and +5 of the preview entry describe. The meaning of each group kind (modes 2 to 5) is read from the tests only.
