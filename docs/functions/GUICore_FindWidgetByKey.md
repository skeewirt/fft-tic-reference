# GUICore_FindWidgetByKey

- **Address:** `0x1403D69FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_FindWidgetByKey(GUICore *core, void *key)`
- **Callers:** GUICore_GetFocus
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the top-level widget that a key (name string + hash) names, walking the widget list; returns 0 when none matches. The focus key at core+1968 goes through it to give the focused widget.

## Behavior

- V: iterates the widget pointer vector core+24 .. core+32.
- V: when the widget's dword at +24 is non-zero and the key's dword at +8 is non-zero, a widget matches when the two dwords are equal (the hash of the .uib name).
- V: otherwise it compares the widget's C string at +16 with the key's string pointer at +0 byte by byte, and matches on equality.
- V: returns the first match, so a duplicate name resolves to the earlier widget in the list.

## Referenced by

- Called by: [GUICore_GetFocus](GUICore_GetFocus.md)
- Observed behaviours: [BattleCommandMenuStates](../behaviors/BattleCommandMenuStates.md)

## Notes

Live use (planned, 2026-11-04): the debugger's `where` can read the key at g_GUICore+1968 (string at +0, hash at +8) and find the focused screen without calling game code; the screen name is the string at widget+16.

## Open questions

Not yet read on the live game: whether the string at widget+16 is the full .uib path as shown by `screens` (?).
