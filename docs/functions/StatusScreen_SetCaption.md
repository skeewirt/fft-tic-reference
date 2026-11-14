# StatusScreen_SetCaption

- **Address:** `0x140113388`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char StatusScreen_SetCaption(int64 screen, int status)`
- **Callers:** sub_140112B48, sub_1401130F8
- **Callees:** sub_1400F5828, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_14028F728, sub_14028F6AC, sub_14028F754, UIGadgetFFTOVScrollText_Refit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows the caption (the help text) of the selected status on the Status screen.

## Behavior

- V: a negative status shows a blank text.
- V: otherwise the key is status + 1; above 40 (a signed compare of the key with 40) the text pointer stays null; else the Caption string of that UIStatusEffect row.
- V: the text goes into the scroll text at screen +0x1B0 and the scroll gadget at +0x218 is refitted.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UIGadgetFFTOVScrollText_Refit](UIGadgetFFTOVScrollText_Refit.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours.

## Open questions

None recorded.
