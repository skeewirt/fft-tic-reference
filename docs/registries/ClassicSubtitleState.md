# ClassicSubtitleState

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The state names of the classic-movie subtitle window and the UIClassicSubtitles line_layout value that picks each.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="hide"></a>0 | `Hide` | `no line` | V | After a line's ends_at: plays 'Hide' unless the line's keep_shown byte is set. |
| <a id="line01"></a>1 | `Line01` | `line_layout 0 (or any other value)` | V | Layout 1. |
| <a id="line02"></a>2 | `Line02` | `line_layout 1` | V | Layout 2. |
| <a id="line03"></a>3 | `Line03` | `line_layout 2` | V | Layout 3. |
| <a id="line04"></a>4 | `Line04` | `line_layout 3` | V | Layout 4. |
| <a id="line05"></a>5 | `Line05` | `line_layout 4` | V | Layout 5. |

## Behavior

- M: the stock rows hold line_layout 0 (16 rows), 2 (39) and 4 (38): only Line01, Line03 and Line05 occur.

## Notes

What each layout looks like is in the window's layout file, not in the code.

## Open questions

?
