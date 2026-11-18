# UIAddon_LoadByPath

- **Address:** `0x1401D1A3C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddon_LoadByPath(UIAddon *addon, int row, const char *path)`
- **Callers:** UIAddon_LoadByRow
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads an add-on's layout from a path: a path starting with '#' names a widget, any other path is a layout file.

## Behavior

- V: '#' -> 0x1401D40C8 by name, hidden, the add-on id among its listeners; otherwise 0x1401D1BA0 loads the layout file.

## Open questions

None recorded.
