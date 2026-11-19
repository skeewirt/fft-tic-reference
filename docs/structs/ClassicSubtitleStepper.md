# ClassicSubtitleStepper

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The stepper of the classic-movie subtitle window (ClassicSubtitles_Step): the current layout state and the keep-shown byte.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by |
|---|---|---|---|---|---|
| <a id="state"></a>`0x18` | state | `uint8` | V | Current state 0..5: 0 = no line, 1..5 = Line01..Line05 (registry ClassicSubtitleState). | [ClassicSubtitles_Step](../functions/ClassicSubtitles_Step.md) |
| <a id="keep_shown"></a>`0x19` | keep_shown | `uint8` | V | keep_shown byte of the current line (UIClassicSubtitles +0x18). | [ClassicSubtitles_Step](../functions/ClassicSubtitles_Step.md) |

## Behavior

- V: the window nodes the state plays on are at addon +48 and +56.

## Notes

Name is ours.

## Open questions

? the other fields.
