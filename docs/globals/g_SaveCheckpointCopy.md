# g_SaveCheckpointCopy

- **Kind:** global
- **Address:** `0x142E80450`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `uint8[72564]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The checkpoint copy: 40,164 bytes of slot record whose unit area (offset 0x518) is overwritten with the live unit save data by the checkpoint writer sub_1402CEEE8, followed by further live fields. The autosave materialiser restores kind 0 here and the capture side copies the live state into it.

## Behavior

- V: the resume payload copies 40,164 bytes to this block and the kind-0 body is byte-identical to it.

## Referenced by

- Read by: [Save_ResumeCheckpoint](../functions/Save_ResumeCheckpoint.md), [sub_140217EF8](../functions/sub_140217EF8.md)
- Written by: [sub_1402181EC](../functions/sub_1402181EC.md), [sub_140246014](../functions/sub_140246014.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md)

## Open questions

None recorded.
