# UIName_Intern

- **Address:** `0x1403D8A24`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIName_Intern(NameTable *table, NameKey *outKey, const char *str, bool adopt)`
- **Callers:** UIName_Key, UIName_SetKey, UIAnim_ApplyTrack, sub_1400F6148, sub_1401F6C6C, sub_1403D5934, sub_1403D9038
- **Callees:** sub_140011750 (alloc), sub_140011804 (free), sub_14002620C, sub_14006635C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Interns a UI name string: finds or adds it in the name table and fills `outKey` with its key id, adding one reference.

## Behavior

- V: hash is seeded 0x9C43A61E and folds each byte as `h = byte ^ rol32(h, 7)`; the bucket is `h % 0x7F + 1`.
- I: probes the bucket's slots for an equal string, otherwise takes a free slot, and increments the reference count at slot+12 (head of the function read; the rest follows the release function's slot layout).
- I: `adopt` decides whether the table keeps the caller's string or copies it (allocator call sub_140011750 present).
- V: null or empty strings return without a key.
- V: callers include UIName_Key, UIName_SetKey and UIAnim_ApplyTrack (7 total).

## State touched

- Calls: [sub_14002620C](sub_14002620C.md)

## Referenced by

- Called by: [UiNames_InstallCoreNames](UiNames_InstallCoreNames.md)

## Notes

The table is the global g_UINameTable (qword_143CDA2A0, 127 buckets). Release with UIName_ReleaseKey.

## Open questions

None recorded.
