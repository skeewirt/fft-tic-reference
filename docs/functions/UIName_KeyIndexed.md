# UIName_KeyIndexed

- **Address:** `0x1403D8E5C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIName *UIName_KeyIndexed(__int64 unused, UIName *out, const char *base, int index)`
- **Callers:** sub_140297FF8, sub_1403FA344, sub_1403FB340, sub_14040C1DC, sub_14040C37C
- **Callees:** Str_Format, UIName_Key

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the name key for base, or 'base#index' when index is non-zero, via UIName_Key.

## Behavior

- V: index != 0: Str_Format(buf[256], '%s#%d', base, index) and UIName_Key(out, buf); index == 0: UIName_Key(out, base). Returns out.

## State touched

- Calls: [Str_Format](Str_Format.md), [UIName_Key](UIName_Key.md)

## Notes

The name is ours (IDB: sub_1403D8E5C). The '#n' suffix is how repeated child names are keyed.

## Open questions

-
