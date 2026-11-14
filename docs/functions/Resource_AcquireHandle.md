# Resource_AcquireHandle

- **Address:** `0x1400912B4`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `ResourceHandle *Resource_AcquireHandle(ResourceManager *m, const char *name, const char *ext, unsigned int hash, char load_now, void *state32, void *a7)`
- **Callers:** Resource_FindOrOpen, Pack_MountOne
- **Callees:** sub_140093108, sub_14009322C, ResourceHandle_LoadNow, sub_140092D84, sub_1400914EC, sub_140026BD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds or creates the registry entry of one resource name (a pack or a file) under its bucket's lock and, when asked, loads it before returning.

## Behavior

- V: an empty name reports error 0x96080003 and returns null.
- V: bucket = hash & 0x1FF; takes that bucket's SRW lock (manager + 56 + 8 * bucket) shared, looks the name up in the registry tree (sub_140093108) and adds a reference to a found entry (vtable +24).
- V: not found: takes the bucket lock exclusively and creates the entry (sub_14009322C, given the hash, the bucket, the name, the extension, the load flag and a copy of the 32-byte state block); a result of 1 means the entry was there after all and is returned as is.
- V: a new entry with load_now: loads it at once (ResourceHandle_LoadNow) and returns null when the load ended failed (+80 is 2 or 3), dropping the reference (vtable +32); without load_now the new entry is queued (sub_140092D84).
- V: a found entry with load_now that is not finished (+84 not 1) is waited for: the loop yields (SleepEx 0) and, on the thread qword_140C6AD58 names, runs sub_1400914EC itself.

## State touched

- Calls: [sub_140093108](sub_140093108.md), [ResourceHandle_LoadNow](ResourceHandle_LoadNow.md)

## Referenced by

- Called by: [Pack_MountOne](Pack_MountOne.md), [Resource_FindOrOpen](Resource_FindOrOpen.md)

## Notes

The name is a registry key (a leaf name for packs, Pack_MountOne), and no folder is joined here.

## Open questions

? where the pack folder is joined to the leaf name (inside the reader the created entry opens, not traced); ? what sub_1400914EC runs for the waiting thread (I: the queued loads).
