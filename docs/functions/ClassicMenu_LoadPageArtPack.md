# ClassicMenu_LoadPageArtPack

- **Address:** `0x140343770`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long ClassicMenu_LoadPageArtPack(int page)`
- **Callers:** the legacy menu page setup
- **Callees:** Mem_CopyChecked, Resource_GetSlotObject, GameData_StartTrackedRead, EventThread_PumpAudioWhileBusy

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the art pack of a legacy menu page (0..5) into the shared menu texture buffer.

## Behavior

- V: sets up the draw list with the page's run of cells from two dword tables (table[page] and table[page + 1] - table[page], and a second pair with a stride of 60 entries).
- V: selects one of six resource slots (39..44) and copies 98304 bytes of its data to the shared buffer, with a separate source for each page.

## State touched

- Calls: [Mem_CopyChecked](Mem_CopyChecked.md), [Resource_GetSlotObject](Resource_GetSlotObject.md), [GameData_StartTrackedRead](GameData_StartTrackedRead.md), [EventThread_PumpAudioWhileBusy](EventThread_PumpAudioWhileBusy.md)

## Referenced by

- Reads tables: [LegacyAbilityMenuSkillsetByTab](../tables/LegacyAbilityMenuSkillsetByTab.md)

## Open questions

None recorded.
