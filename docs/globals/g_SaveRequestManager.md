# g_SaveRequestManager

- **Kind:** global
- **Address:** `0x140C69698`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `void *`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The save-data request object the slot, settings and PNG code queues work on. The same object carries the file object's request list and the per-area write/read kicks.

## Behavior

- V: the settings writer, the slot store and the slot load all pass it to the queue and kick helpers.

## Referenced by

- Read by: [Boot_Update](../functions/Boot_Update.md), [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md), [UIAgentFFTOSaveLoad_Ctor](../functions/UIAgentFFTOSaveLoad_Ctor.md), [sub_1401E7EF8](../functions/sub_1401E7EF8.md), [sub_1402083B4](../functions/sub_1402083B4.md)
- Written by: [UIAgentFFTOSaveLoad_Ctor](../functions/UIAgentFFTOSaveLoad_Ctor.md)

## Open questions

None recorded.
