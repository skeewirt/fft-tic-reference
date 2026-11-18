# EventTasks_Init

- **Address:** `0x1402EA2F0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *EventTasks_Init(void)`
- **Callers:** `sub_1402B2EB0`, `sub_1402B2FA4`, `sub_1402B32D4`, `sub_1402B340C`
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises the first task group: points its task table, variable store and event buffer at their storage.

## Behavior

- V: picks a per-language table from the language-info field at +8 (`unk_1408DE240` for 0, `unk_1408E0DA0` for 3, `unk_1408E2350` for 2 and `unk_1408DF7F0` otherwise) and stores it in `qword_14184B230`.
- V: sets the first task table `off_14078D5D8` to `unk_14184B3C0`, the event buffer pointer `qword_141853BC0` to `unk_140D3CD50`, and the event variable store `off_14078DCE8` to `unk_140D40060`.
- V: also sets `qword_141853BD0` and `qword_14184B220` to fixed blocks and clears `word_14184B288` and `word_14184B360`.
- I: the per-language table is the phase-record bank selected for the game language.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)
- Writes: [g_EventScriptBuffer](../globals/g_EventScriptBuffer.md), [g_EventWorkPtr](../globals/g_EventWorkPtr.md)

## Referenced by

- Called by: [LegacyMenu_InitWorld](LegacyMenu_InitWorld.md)
- Reads tables: [EventMenuNodesDefault](../tables/EventMenuNodesDefault.md), [EventMenuNodesLanguage0](../tables/EventMenuNodesLanguage0.md), [EventMenuNodesLanguage2](../tables/EventMenuNodesLanguage2.md), [EventMenuNodesLanguage3](../tables/EventMenuNodesLanguage3.md)

## Notes

SceneTasks_Init points the second task group at the same event buffer and variable store, which is why both groups see the same variables.

- V: 0x1402EA368 is a label inside this function (a branch target, not an entry; an earlier sheet named it `EventScene_SetBuffers`). What that path does:
  - V: it stores the fixed pointer 0x140D3CD50 in the global at 0x141853BC0; that address is the event-script file buffer.
  - V: it stores the fixed pointer 0x140D40060 in the global at 0x14078DCE8, the pointer the event work block is reached through.
  - V: it writes the 16-bit argument to the words at 0x14184B288 and 0x14184B360.
  - V: the event id arrives in r8w (the third integer argument), not rcx or rdx.
  - V: the body is 45 bytes with two pointer stores, two word stores and no call or branch.
  - V: it has no direct caller in the image; the scene setup reaches it through a stored pointer or an inlined copy.
  - I: the two buffers are the script image and the event work area, because the first is the buffer the script loader fills and the second is the pointer the event tasks read.
  - I: the two words are the current event id and its mirror, because the same id is written to both.
  - ?: what the second buffer at 0x140D40060 holds; its size and owner are not established.

## Open questions

What the language values 0 to 3 stand for.
