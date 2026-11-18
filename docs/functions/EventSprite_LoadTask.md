# EventSprite_LoadTask

- **Address:** `0x140233EA0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventSprite_LoadTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x58
- **Callees:** GameData_ReadSectors, SceneTask_WaitFrame, SceneTask_Terminate, `sub_1402F3888` (allocate), `sub_1402F3A04` (free), the file helpers `sub_1403D2004`, `sub_1403D21F0`, `sub_1403D2358`, `sub_1403D21C8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x58: loads the sprite data for an event character into memory for one of two display sides, then ends.

## Behavior

- V: reads two values from its task block: a side number (0 or 1) and a sprite id, which the interpreter stored there before the task ran.
- V: allocates a 30,720-byte buffer and reads 15 sectors of data kind 44 for that sprite id with GameData_ReadSectors (start sector = 15 * sprite id).
- V: for the sprite ids 35, 61, 96, 112 and 135 it also reads a texture file named `fftpack/spr/evtchr/evtchr_<id>.tex` into the buffer at offset 2432 (28,288 bytes).
- V: when the global scale value `dword_142C81554` is at least 2.0 and `DWORD2(xmmword_142E7FC80)` is non-zero, it records the sprite id and a derived value for the chosen side in one of two global pairs.
- V: stores the side in `dword_140D40818` and the buffer in `qword_140D40820`, waits one frame, frees the buffer and ends through SceneTask_Terminate.
- I: the evtchr textures are the enhanced portraits or full-body art for those five characters.

## State touched

- Calls: [GameData_ReadSectors](GameData_ReadSectors.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Reads tables: [EventSpriteHdTextures](../tables/EventSpriteHdTextures.md)
- Started by event opcodes: [0x58](../opcodes/README.md)

## Notes

The opcode record for 0x58 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the two global pairs control and what the 15-sector data of kind 44 contains.
