# EventVoice_PlayTask

- **Address:** `0x140221488`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventVoice_PlayTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0xC2; EventScript_Run starts it only when `dword_1407D453C` is 1
- **Callees:** `sub_1401E8A9C`, `sub_1401DA210`, `sub_1401DA4B8`, `sub_1401DA410`, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0xC2 when the enhanced flag is set: starts a table entry for its id, keeps it in the list while it is present, and stops it when the object or the skip test says so.

## Behavior

- V: tags its task slot with 72 (0x48) in `qword_140D40B38[256 * index]`.
- V: reads the dword at +8 of its task block as the entry id (`ebx`); the opcode handler stores the operand there.
- V: `sub_1401E8A9C(qword_143CD9DD0)` returns the dword at object+96, or 0 when `qword_140C69690` is set and its byte at +55 is 1, or is 2 while object+96 is 2.
- V: when that value is 0, or the dword at object+88 is 0, and the list pointer p (`qword_143CD9DB8 + 40`) and p+32 are both non-null, it calls `sub_1401DA210(p, id)` to start the entry.
- V: `sub_1401DA210` finds row `id` with `sub_1403D4534` in the table at p+24. When that row has a non-empty string at its offset and the id is not yet in the tree at p+56, it inserts the entry with `sub_1401DAB54`, creates an object through `sub_140091124` stored at entry+48, and sets the entry's byte at +64 to 1.
- V: loop: while p and p+32 are set and `sub_1401DA4B8(p, id)` returns true (the id is present in the tree at p+56), each pass tests the object again: if sub_1401E8A9C is non-zero and object+88 is non-zero, or the skip test holds (dword +4 of `qword_142FF9E08` non-zero and dword +4 of `qword_142FF9E00` equal to 3), it calls `sub_1401DA410(p, id)` when p+32 is set and ends.
- V: otherwise it calls SceneTask_WaitFrame and repeats the loop.
- V: `sub_1401DA410(p, id)` finds the entry; if its +64 byte is 1 it sets it to 2, releases its +56 object through `sub_14009B550` when `qword_143CD9B60` and the field are set, calls `sub_1401D9EE8` on the field at +40, and removes the entry with `sub_1401DAAB4`.
- V: ends through SceneTask_Terminate.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0xC2](../opcodes/README.md)

## Notes

The opcode record for 0xC2 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the table at `qword_143CD9DB8 + 40` holds and what its entries are (the PanzerVoice vtable name in the IDB suggests voice lines, which is not confirmed), what `qword_143CD9B60` and `sub_140091124` create, and what the object at `qword_143CD9DD0` is.
