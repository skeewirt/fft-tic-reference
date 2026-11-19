# Movie_Start

- **Address:** `0x1400D8304`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int Movie_Start(void *movieController, int movieId, ...)`
- **Callers:** Boot_UpdateVideo
- **Callees:** sub_14027A2B0, sub_1401D6F9C, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_140026D3C, sub_1401D7608, sub_1400EBA64, sub_1400EB90C, sub_1400EBB44, sub_1400EBC38, UIAgent_DetachAddon

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the playback of a movie from its MovieData row: picks the file, the sound banks, the subtitle window and the controller flags.

## Behavior

- V: reads the MovieData row of the movie id (table 65, the only reader of the table).
- V: path = classic_path (+0x18) when non-empty; the language track (+0x20) is then not used and the classic subtitle style is set. Otherwise path (+8), plus the localized_path (+0x20) as a second track when the language is not language 0.
- V: sound_bank (+0x1C) is passed to MovieSound_LoadBank for slots 20, 21 and 22 (bgm, voice, se); a negative value loads nothing.
- V: the link at +0x10 (table id as a 16-bit value, key at +0x14): 192 opens the classic subtitles window (UIClassicSubtitles key), 209 the subtitles window with a half-size flag.
- V: sets the controller flags: 0x20 from pausable (+0x24), 0x10 from skippable (+0x25), 0x08 from skip_on_press (+0x26).
- V: the listeners called at the end get the listener and the movie id only.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UIAgent_DetachAddon](UIAgent_DetachAddon.md)

## Referenced by

- Appears in flows: [MovieStart](../flows/MovieStart.md)
- Called by: [sub_1402561D0](sub_1402561D0.md)
- Observed behaviours: [MovieSkipKinds](../behaviors/MovieSkipKinds.md)

## Notes

Name is ours (it is the name the database carries). The controller flags live at MovieController +24 (GameUIManager +0xE0); Boot_UpdateVideo passes GameUIManager +200 to Movie_Start.

## Open questions

? which screen plays the movies that end on one press.
