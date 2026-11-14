# MoveTileFlags

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (filled at run time)
- **Rows:** 512 entries of 1 byte
- **Held in:** [g_MoveTileFlags](../globals/g_MoveTileFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per-tile flag byte of the move-range builder: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked.

## Open questions

None recorded.
