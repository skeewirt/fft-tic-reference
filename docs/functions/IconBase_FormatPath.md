# IconBase_FormatPath

- **Address:** `0x1400FC1C0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void IconBase_FormatPath(int number, char *out, int size)`
- **Callers:** not recorded
- **Callees:** Icon_FormatPath, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the path of a numbered 'base' picture.

## Behavior

- V: Icon_FormatPath(21, tmp, texture-parts form, 260), then Str_Format(out, size, tmp, number): the 'base_%02d' picture path for the number.
- V: used for the Gossip picture and the Town picture columns (the latter through sub_140158CB0).

## State touched

- Calls: [Icon_FormatPath](Icon_FormatPath.md), [Str_Format](Str_Format.md)

## Open questions

None recorded.
