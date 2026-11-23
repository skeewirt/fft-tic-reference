# Opening_LoadMessageSprites

- **Address:** `0x14037DB9C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long Opening_LoadMessageSprites(void)`
- **Callers:** sub_1402F0124, sub_14037F398
- **Callees:** MemFile_Read, EventThread_Yield, sub_14037FC0C, sub_140380020, sub_140380104

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the opening message textures and selects the language's sprite list for the opening text.

## Behavior

- V: reads two message texture files into the video buffer one after the other, waiting for the upload each time.
- V: selects one of four 12-pointer sprite list sets by the text language (0x1407BEF20 language 0, 0x1407BEFE0 language 3, 0x1407BEF80 language 2, 0x1407BF040 default) and starts the opening text task.

## State touched

- Calls: [MemFile_Read](MemFile_Read.md), [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md)
- Called by: [OpeningMenu_Task](OpeningMenu_Task.md), [OpeningTask_12](OpeningTask_12.md)
- Reads tables: [OpeningSpriteLists](../tables/OpeningSpriteLists.md), [OpeningStepMaps](../tables/OpeningStepMaps.md)

## Open questions

None recorded.
