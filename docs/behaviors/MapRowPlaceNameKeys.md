# MapRowPlaceNameKeys

- **Kind:** observed behaviour
- **Scope:** engine (Map row, PlaceName table 85)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [PlaceName_GetText](../functions/PlaceName_GetText.md), [MapTitle_SetFromMapId](../functions/MapTitle_SetFromMapId.md), [MapTitleLabel_SetText](../functions/MapTitleLabel_SetText.md), [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A Map row holds three keys of the PlaceName table: the full place name of the map, a shorter area name and a part name; the title uses the first, the save list prefers the second and adds the third.

## Behavior

- V: place_name (+0x8) is the key of the full name: the map title (MapTitle_SetFromMapId), the title text node and the sortie confirm window read it through PlaceName_GetText.
- V: place_name_2 (+0xC): when non-zero it is the text the save list shows for the map, otherwise place_name is used (SaveLoadList_FillItem).
- V: place_name_3 (+0x10): when non-zero the save list adds it as a second text argument with a flag set to 1 (a formatted two-part label); otherwise the flag is 0.
- V: title_ja_state (+0x1C) is the last argument of MapTitleLabel_SetText; 0 keeps the 'En' state of the title label in every language, non-zero lets language ids 0, 4, 5 and 6 play the 'Ja' state.
- M: place_name holds 0 on 12 rows and a key with no PlaceName row (10100) on five (empty text); place_name_2 and place_name_3 are non-zero on 26 rows each and always hold PlaceName keys; title_ja_state is 0 on ten rows (the closing titles) and 1 on 119.

## Open questions

? which language names ids 0, 4, 5 and 6 are.
