# UITexturePath_Select4k

- **Address:** `0x1403DB0EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool UITexturePath_Select4k(GUIFontSlots *slots, char *out, __int64 a3, const char *path)`
- **Callers:** GUIFontSlots_AcquireTexturePart, sub_1403DA654, sub_1403DACD4, sub_1403DB140
- **Callees:** sub_14002620C (bounded copy)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a texture path into out (255 characters at most) and, when the path contains '_2k_', changes it to '_4k_'; returns true when the path contains _2k_ or _4k_.

## Behavior

- V: sub_14002620C(out, 256, path, 255) copies the string; strstr(out, '_2k_') found: byte [1] of the match is overwritten with '4' (52) and true is returned; otherwise returns strstr(out, '_4k_') != 0.
- V: unconditional - there is no resolution option read here, so every _2k_ path is promoted to _4k_ (the build only ships the high-resolution parts).

## State touched

- Calls: [sub_14002620C](sub_14002620C.md)

## Notes

The name is ours (IDB: sub_1403DB0EC). The caller keeps the returned flag in byte +35 of the 40-byte auxiliary record.

## Open questions

? what byte +35 of that auxiliary record is used for (probably a 'scale by 2' flag for 4k parts).
