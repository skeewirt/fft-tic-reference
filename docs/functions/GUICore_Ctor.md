# GUICore_Ctor

- **Address:** `0x1403D5348`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_Ctor(GUICore *core)`
- **Callers:** GUI startup
- **Callees:** sub_1403E5B84, sub_1403F89B8, sub_14008EFA0, CreateEventA, sub_1400288E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructs the GUI core: widget lists, the UI renderer, the focus key strings, the screen size and the per-frame worker slots.

## Behavior

- V: sets the two vftables; the widget list is a vector at +16 / +24 (sorted by the word at widget+62 each frame); four small vectors at +88 and two 144-byte entries at +216 (sub_1403F89B8) are initialised.
- V: allocates the 606720-byte UI renderer object (sub_1403E5B84) and stores it at core+208 (the same object whose 592-byte layer records start at renderer + 303504); sets the design screen size 1920 x 1080 at +512 / +516 and +520 / +524.
- V: the focus key strings at +1968 / +1984 / +2000 (and the other string slots up to +2048) start as the shared empty string; ten 264-byte slots start at +2144; an event handle (CreateEventA) is stored at +4784 and the frame callback sub_1403D7E9C is registered with the language info.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Notes

g_GUICore + 208 is the UI renderer used throughout the glow / layer notes.

## Open questions

None recorded.
