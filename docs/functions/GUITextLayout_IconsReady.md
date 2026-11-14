# GUITextLayout_IconsReady

- **Address:** `0x1403DCE74`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUITextLayout_IconsReady(GUITextLayout *layout)`
- **Callers:** GUITextNode_Layout, GUITextNode_UpdateLayout (sub_1403F1234, for nodes whose mode dword +416 is 3)
- **Callees:** GUIFontSlots_IsLoaded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when every inline-icon texture requested by the layout is loaded; caches the answer in layout+100 / +101.

## Behavior

- V: byte layout+100 == 0 returns byte +101 (the cached 'ready' flag). Otherwise each 16-byte entry of the icon reference vector (+72 / +80, built by GUITextNode_PlaceIcon: dword +4 slot, dword +12 second slot) is tested with GUIFontSlots_IsLoaded on g_GUIFontSlots: entry+4 always, entry+12 only when non-zero; the first not-loaded returns 0.
- V: when all are loaded (or the vector is empty) word +100 = 0x0100 (pending = 0, ready = 1) and +101 is returned.

## State touched

- Calls: [GUIFontSlots_IsLoaded](GUIFontSlots_IsLoaded.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [GUITextNode_UpdateLayout](GUITextNode_UpdateLayout.md)

## Notes

The name is ours (IDB: sub_1403DCE74). Called with node+320 = the layout. A layout containing icons is not re-laid-out until its icons are loaded (see GUITextNode_UpdateLayout).

## Open questions

? who sets +100 = 1 (probably GUITextNode_Layout when it records an icon).
