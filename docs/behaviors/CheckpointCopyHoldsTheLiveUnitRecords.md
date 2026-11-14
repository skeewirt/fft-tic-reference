# CheckpointCopyHoldsTheLiveUnitRecords

- **Kind:** observed behaviour
- **Scope:** the checkpoint copy of the slot record (g_SaveCheckpointCopy)
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [sub_1402CEEE8](../functions/sub_1402CEEE8.md), [sub_140246014](../functions/sub_140246014.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_PackFromParty](../functions/SaveWork_PackFromParty.md), [sub_1402CF768](../functions/sub_1402CF768.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The checkpoint writer packs the party into the work copy, copies the work copy to the checkpoint copy, and then overwrites the checkpoint copy's unit area with the live unit records. Whatever the pack step put in the unit area of the work copy is therefore not in the checkpoint copy; the checkpoint holds the live records.

## Behavior

- V: sub_1402CEEE8 fills g_SaveWorkCurrent with 0xFF, calls UnitWork_BuildForSlot(0) and SaveWork_PackFromParty(0), and copies the 0x9CE4 bytes to g_SaveCheckpointCopy.
- V: it then copies 0x7E90 bytes (54 unit records of 600) from g_UnitSaveData to 0x142E80968, which is g_SaveCheckpointCopy + 0x518; the pack code writes the units at work copy + 1304 = 0x518, so the live records land exactly on the unit area of the checkpoint's slot record and replace what the pack put there.
- V: the same function also copies many other live fields (item stores, event variables, world state, flags) into the checkpoint block, so the checkpoint block is a mix of the packed slot record and live fields.
- V: the restore twin sub_1402CF768 (after sub_140246014 with restore = 1 has copied the checkpoint to the work copy) copies the checkpoint's unit area back to g_UnitSaveData with one 0x7E90-byte move, so the live records survive a checkpoint round trip as they were, and the work copy's own unit area is not what is restored.
- V: sub_140246014 with restore = 0 would pack and store without the live-record copy, but its only direct caller passes restore = 1.
- V: consequence: a change to job bytes or spare bytes in the work copy's unit area (after SaveWork_PackFromLive / SaveWork_PackFromParty) reaches slot saves written from the work copy, but not the checkpoint copy built by sub_1402CEEE8; data that must survive through the checkpoint must be in the live records (g_UnitSaveData).
- I: sub_1402CEEE8 is called by sub_1402B8690, which has thirteen callers in the event and scene code; the checkpoint is captured from scene paths, not from a save-menu action (the trigger of each caller was not read).

## Notes

Evidence: IDA, sub_1402CEEE8, sub_140246014, sub_1402CF768 and SaveWork_PackFromLive read in full on 2026-11-09.

## Open questions

? which caller of sub_1402B8690 captures the checkpoint at a battle autosave; ? whether the 0x7E90 copy also runs on any path that does not go through sub_1402CEEE8.
