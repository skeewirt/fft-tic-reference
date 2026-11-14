# Cursor_LoadTable

- **Address:** `0x1400103E4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `HCURSOR Cursor_LoadTable(void)`
- **Callers:** startup (not traced)
- **Callees:** LoadCursorA, LoadImageA, GetModuleHandleA, Cursor_Apply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the game's mouse cursors into the cursor object's table (index -> HCURSOR) and applies the current one.

## Behavior

- V: entry 0 = LoadCursorA(NULL, IDC_ARROW 0x7F00); entries 1..5 = LoadImageA(exe, resource id, IMAGE_CURSOR, 0, 0, 0) with the ids 0x89 (137), 0x88 (136), 0x8A (138), 0x8B (139), 0x8D (141), in that order (each id is an immediate passed as the second argument of LoadImageA, set at 0x140010455 / 0x140010482 / 0x1400104A8 / 0x1400104D2 / 0x1400104FC). 17 slots exist in the table (indices 0..16); only these six are filled here.
- V: after the table is filled the current index (+144) is set to 0 and Cursor_Apply is called; bit 0 of +148 is then set and Cursor_Apply runs again.
- V (LoadImageW on this exe, 100 % scaling): a requested size of 0 x 0 loads the largest entry of each group: 128 x 128 for all five, hotspots (61,63) for 137 / 138 / 139 / 141 and (64,63) for 136.

## State touched

- Calls: [Cursor_Apply](Cursor_Apply.md)

## Notes

The name is ours. The art (extracted by the studio's panel extractor as quill_<index>.png): 1 = golden quill (the default), 2 = a mouse with a check mark, 3 = a brighter glowing quill, 4 = a white glove hand, 5 = an orange quill. These are OS cursors: the game's own render and a window capture (PrintWindow) never contain them.

## Open questions

Which index the Job Tree shows in each state (see GUICursor_UpdateIndex); who uses 2, 4 and 5.
