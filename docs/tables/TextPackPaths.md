# TextPackPaths

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140680550`
- **Rows:** 45 rows of 8 bytes
- **Keyed by:** resource slot 0..44
- **Read by:** [Resource_GetSlotObject](../functions/Resource_GetSlotObject.md)
- **Row layout:** [TextPackPathsRow](../structs/TextPackPathsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointers to the file paths of 45 text resources (event help, spell, sample, world, opening, join text, the system text sets, battle and menu tutorials, scenario pages). Verdict: pointer-table.

## Behavior

- V: the strings are separate and no other instruction or pointer addresses them; the string lengths run from 32 to 39 bytes
- V: Resource_GetSlotObject builds a file object from the path, reads the whole file into a new buffer and records its size

## Notes

Our names. Tags: V.

## Open questions

None recorded.
