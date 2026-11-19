# IconGroup4kPaths

- **Kind:** observed behaviour
- **Scope:** engine (icon paths)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [IconPath_FromIconId](../functions/IconPath_FromIconId.md), [UITexturePath_Select4k](../functions/UITexturePath_Select4k.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Icons in a group with select_4k set load their '_4k_' file instead of a '_2k_' one; the stock data names no '_2k_' path.

## Behavior

- V: the group of an icon is the last IconGroup row whose first_icon is not above the icon id.
- M: 598 icons with a path fall in groups with select_4k = 1 and 2 in groups with 0; no stock path contains '_2k_', so the rewrite changes nothing in the shipped data.

## Open questions

None recorded.
