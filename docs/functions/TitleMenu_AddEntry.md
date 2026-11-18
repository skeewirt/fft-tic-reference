# TitleMenu_AddEntry

- **Address:** `0x1401C43B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_AddEntry(UIAddonFFTOTitle *addon, uint8 kind)`
- **Callers:** TitleMenu_Build (6 sites)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends one row to the title menu: sets the row's label by kind and stores the kind.

## Behavior

- V: appends at index `count` (+216): sets the row's text node text id (+248, dirty byte +316) by kind, stores the kind byte, count + 1.
- V: does not check the count against 6.
- V: text ids (UI table, nxd id 19): kind 0 gives 2215 New Game, 1 gives 2226 New Game +, 2 gives 2223 Continue, 3 gives 2218 Load Game, 4 gives 2224 Music Player, 5 gives 2217 Select Version; any other kind gives text id 0. The strings were read in the stock English UI table.
- V: writes the text id to `*(a1 + 24 * (count + 3) + 8)` (when non-null) and the kind to `a1 + 24 * (count + 3) + 16`. With six rows taken, row index 6 would put its text node at +224 (the last input tick), its button node at +216 (the count) and its kind byte at +232 (inside the 240 bytes, past the last field).

## Referenced by

- Called by: [TitleMenu_Build](TitleMenu_Build.md)
- Observed behaviours: [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md), [TitleMenuRows](../behaviors/TitleMenuRows.md)

## Notes

Registry: TitleMenuEntryKinds.

## Open questions

None recorded.
