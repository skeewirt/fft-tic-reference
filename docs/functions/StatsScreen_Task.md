# StatsScreen_Task

- **Address:** `0x1402E1890`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `_QWORD *StatsScreen_Task(void)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of the legacy stats screen: builds its eighteen cell primitives and the stat number strips, then waits for a close.

## Behavior

- V: tags its task slot 35, builds three VRAM strips with sub_1402EC3C8 from the number field groups at 0x1408E59B0 (three fields), 0x1408E5A10 (four) and 0x1408E5A90 (eight) and copies them to the VRAM rectangles at 0x1408E55D0 / D8 / E0.
- V: picks the 18-cell block from the four language copies (0x1408E55F0 language 0, 0x1408E56D0 default, 0x1408E57B0 language 2, 0x1408E58B0 language 3), places eighteen primitives with sub_140242AFC and copies two primitive sets.
- V: then loops one frame at a time, recolouring the cursor primitives by whether the task slot's flag is set, until the slot's close word becomes non-zero, and ends the task.

## Referenced by

- Reads tables: [StatsNumbersLive](../tables/StatsNumbersLive.md)

## Notes

Read in full.

## Open questions

?: which screen opens it in play.
