# Pack_MountOne

- **Address:** `0x140092A04`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int Pack_MountOne(void *manager, const char *leafName)`
- **Callers:** Pack_MountList, one further site in sub_140092A04's neighbourhood
- **Callees:** sub_140037CA4 (name hash), sub_140093108 (registry tree), Resource_AcquireHandle (reader open)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds or creates the registry entry for one pack leaf name and opens the pack behind it.

## Behavior

- V: hashes the leaf name, then uses the hash's low nine bits as a bucket index in the manager's pack table.
- V: looks the name up in a per-bucket tree; equal hashes are resolved by a byte-wise name comparison.
- V: takes the leaf name only, not a directory path.
- V: an already-present entry is returned as-is under the manager lock; the pack is not reopened.
- V: a failed open reports error code 0x96080010; the tail also holds a "list too long" message for a full list.
- V: the same bucket mask and tree serve the file registry, so both pack names and file names share 512 buckets.
- V: two direct call sites.

## State touched

- Calls: [sub_140093108](sub_140093108.md), [Resource_AcquireHandle](Resource_AcquireHandle.md)

## Referenced by

- Called by: [Pack_MountList](Pack_MountList.md)

## Notes

- V: head and main body read; the tail after the open was not read.

## Open questions

- ?: the exact lifetime of the old handle when a name is mounted twice.
