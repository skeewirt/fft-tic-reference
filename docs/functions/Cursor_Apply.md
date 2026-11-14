# Cursor_Apply

- **Address:** `0x14001DC14`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `HCURSOR Cursor_Apply(CursorObj *c)`
- **Callers:** Cursor_LoadTable, GUICore_OnInputState, GUICursor_UpdateIndex, the window subclass procedure (WM_SETCURSOR with the client hit-test code, sub_14001DB8C)
- **Callees:** SetCursor, LoadCursorA

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes the cursor table's current entry the OS cursor, or hides the cursor.

## Behavior

- V: when bit 0 of +148 is clear, SetCursor(NULL) (hidden); otherwise the HCURSOR at +8 + 8 * index (index = int at +144); an index of -1 or an empty slot falls back to the system arrow; SetCursor(handle).

## Referenced by

- Called by: [Cursor_LoadTable](Cursor_LoadTable.md), [GUICursor_UpdateIndex](GUICursor_UpdateIndex.md)

## Notes

The name is ours.

## Open questions

None recorded.
