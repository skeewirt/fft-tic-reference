# Launcher_DrawPage

- **Address:** `0x1401BB5EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Launcher_DrawPage(void *launcher)`
- **Callers:** UIAddonFFTOLauncher_ShowPage, UIAddonFFTOLauncher_vfunc_13, sub_1401BB1D0, sub_1401BB404
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryByKeys2, NxdEntry_GetRow, sub_1401BB9D8, sub_1401BBDD0, sub_1401BB77C, sub_1402EE84C, sub_1401BBF80

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the current page of the launcher's guide pages.

## Behavior

- V: reads the LauncherGuide row of the current set and page: controls_page (+0xC) non-zero draws Launcher_DrawControlsPage; else start_page (+0xD) non-zero draws Launcher_DrawStartPage; else Launcher_DrawInfoPage.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
