# GUIWidget_OnEvent

- **Address:** `0x1403FC3B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIWidget_OnEvent(GUIWidget *w, void *source, UIEvent *ev)`
- **Callers:** vtable 0x140721E10 slot 2, sub_1400F4D38 (addon OnEvent base)
- **Callees:** virtual +144 / +152 of the widget

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Widget's own event handler (vtable slot 2 of the GUIWidget vtable at 0x140721E10): maps the widget load / unload events onto two virtual methods.

## Behavior

- V: ev type (dword ev+0) 43: calls virtual +144 of the widget with ev+16; type 44: virtual +152 with ev+16; any other type does nothing (result is stale).
- V: the addon base handler sub_1400F4D38 calls this first and then plays the hover (event 12) / click (event 16) sounds, so every UI addon passes its events through here.

## Notes

The name is ours (IDB: sub_1403FC3B4). Event numbers 43 / 44 are the 'widget load / unload' of GUIOwners_PostEvent's notes. Naming of the two virtuals (OnLoaded / OnUnloaded) is not established.

## Open questions

? what virtual +144 / +152 do for the Job Tree widget (not traced).
