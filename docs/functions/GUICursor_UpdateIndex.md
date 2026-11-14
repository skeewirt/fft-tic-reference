# GUICursor_UpdateIndex

- **Address:** `0x1400FE194`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICursor_UpdateIndex(bool *padMode)`
- **Callers:** the input update (not traced)
- **Callees:** sub_1403D7008, Cursor_Apply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the cursor index the UI wants (g_GUICore + 1904) and shows or hides the OS cursor.

## Behavior

- V: the wanted index starts from a field of the input state (+16); when that is 0 it is 3 if the top actor's byte +575 is set (the actor comes from sub_1403D7008 = the actor table entry for g_GUICore+2064) and 1 otherwise. The index is stored in g_GUICore+1904 when it changed, or 0 (the system arrow) when the pointer is not in use.
- V: the cursor is shown (bit 0 of the cursor object's +148) when the UI is not in pad mode and the mouse flags allow it, and hidden otherwise; a change calls Cursor_Apply.
- V: GUICore_OnInputState copies g_GUICore+1904 into the cursor object (+144, range -1..16) and calls Cursor_Apply when it differs.

## State touched

- Calls: [Cursor_Apply](Cursor_Apply.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Called by: [UI_FrameUpdate](UI_FrameUpdate.md)

## Notes

The name is ours.

- V (2026-11-02): the byte +575 is a component flag, set to 1 by the screen builders that wire a component's `Collision00` hit area (13 write sites in 12 functions, each a one-byte write of 1 next to the hit-area lookup: `sub_140116914`, `sub_140118438`, `sub_140127174`, `sub_14013C804`, `sub_14015F730`, `sub_14017BF70`, the SaveLoad and BGMMode addons' `vfunc_4`, `sub_14018E6CC`, `sub_140293FD0`, `sub_1402AECA0`, `sub_1402AFEA0`; `sub_14042867C` also stores 0x20 at +575 of a different kind of object, not a flag). `sub_14018E6CC` is the Settings screen's tab-bar builder: it loops over `TabButton%02d` and flags every tab button. The Settings rows, switches and picklists are built elsewhere and not flagged.
- V: the component under the pointer is the actor `GUICore_UpdateFrame` hands to `sub_1403D6F70` (stored as the key at g_GUICore+2064; byte +416 must be set for it to count, +576 redirects to a parent; hover enter / leave are vfuncs 5 and 6). `sub_1403D7008` turns that key back into the actor, so over a flagged component the index is 3 and elsewhere 1.
- V (live, 2026-11-02, Settings > Gameplay, polling g_GUICore+1904 and the hovered-actor key at +2064 while the owner moved over the tab bar): over an unselected tab the index is 3 with a key of 6826, 6828 or 6830 (three different tab actors, 2 apart); off the tabs the key is 0 and the index 1. The selected tab never gave 3 (owner's observation: only unselected tabs react). Rows were not polled in this run.
- V (live, pointer x read from g_GUICore+1880 next to the index while the owner swept across a tab divider): between two unselected tabs the index drops back to 1 (hovered key 0) for about 4 layout px, x = 958..961 around the boundary at 960 (strip x 810 = 3 tabs of 270); x = 957 is the left tab (key 6828) and x = 962 the right one (6826). So the tab hit areas stop short of the 4 px divider (`TabSepalete`) on both sides; the gap is the divider's own width.
- V (pixels, the two quill captures of the index 1 and index 3 states): index 3 is the same quill turned about 11 degrees counter-clockwise (art axis 24.2 to 35.0 degrees above horizontal) and about 32 % lighter (luma 129 to 170; mean opaque colour (169,128,27) to (204,169,85)), same 128 px size and hotspot (61, 63). This is the "tilts left and lightens over a tab" look. The launcher mock uses it over its tabs.

## Open questions

Whether the Job Tree flags any component (read g_GUICore+1904 live while hovering a unit panel; no Job Tree builder is among the 14 writers, so index 1 is expected). The other flagged screens (the writers above) have not been named one by one.
