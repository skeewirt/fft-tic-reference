# StringPointerRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of a string pointer table (ResumeKindNames, SoundPackPathPatterns, UiCoreNameKeys, DeflateErrorMessages).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="text"></a>`0x0` | text | `pointer` | V | pointer to a zero-terminated string |

## Referenced by

- Described by tables: [DeflateErrorMessages](../tables/DeflateErrorMessages.md), [ResumeKindNames](../tables/ResumeKindNames.md), [SoundPackPathPatterns](../tables/SoundPackPathPatterns.md), [UiCoreNameKeys](../tables/UiCoreNameKeys.md)

## Open questions

None recorded.
