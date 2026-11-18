# UiEquipScreenNodeNames

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140671F20`
- **Rows:** 9 rows of 8 bytes
- **Keyed by:** name slot 0..8
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Names of the nodes and animations of the HD equipment screen. Verdict: text.

## Behavior

- V: none of the nine strings is addressed by any other instruction or pointer: the list is their only owner
- V: nine consecutive string pointers read by the equipment screen animation code

## Notes

Our names. Tags: V.

## Open questions

- ?: which animation each name starts
