# PoachNewFlags

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable memory (saved with the game)
- **Rows:** 97 entries of 2 bytes
- **Held in:** [g_PoachNewFlags](../globals/g_PoachNewFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two new-flag bytes per poach type at the badge block plus 813; a new game fills them with 0x0101 and the badge routine clears the high byte.

## Open questions

None recorded.
