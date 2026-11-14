# SceneTasks_Init

- **Address:** `0x140235F1C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneTasks_Init(void)`
- **Callers:** `sub_14020E578`
- **Callees:** `sub_1402361FC`, `sub_140242AA8`, `sub_140220264`, `sub_14023F324`, `sub_140331348`, `memset`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises the second task group: clears its task table and points its table, variable store and event buffer at their storage.

## Behavior

- V: sets the second task table `off_140783088` to `unk_140D40AA0`, the event buffer pointer `qword_140D40A90` to `unk_140D3CD50` and the variable store `off_1407830D8` to `unk_140D40060`, which is the same store the first group uses.
- V: clears the whole task table (0x8800 bytes, 17 blocks of 2048), sets the current index `dword_140D40948` to 0 and marks block 0 runnable (the flag at +144).
- V: picks a per-language table from the language-info field and stores it in `qword_140D40950`, copies two blocks of default scene records, and initialises a 63-entry record array whose flag is set only for entries 24, 25 and 58.
- V: called once from `sub_14020E578`.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Notes

Together with EventTasks_Init this shows the two task groups share one event buffer and one variable store.

## Open questions

What the 63-entry record array describes.
