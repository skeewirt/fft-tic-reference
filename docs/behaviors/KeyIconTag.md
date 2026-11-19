# KeyIconTag

- **Kind:** observed behaviour
- **Scope:** engine (UI text)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [TextTag_ExpandKeyIcon](../functions/TextTag_ExpandKeyIcon.md), [InputGlyph_AppendPadButton](../functions/InputGlyph_AppendPadButton.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A 'keyicon' text tag names an input action and the text engine inserts that action's current button glyph.

## Behavior

- V: the tag argument is compared with the name string of UIKeyAssign rows 1..255; the first match gives the action.
- V: the glyph is the pad glyph in pad mode (UIPadDefine row of the bound button) or the modifier and key glyphs in keyboard mode; action 57 asks for the alternate pad glyph.
- M: 88 UIKeyAssign rows carry a name; 168 are empty.

## Open questions

None recorded.
