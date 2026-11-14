# Pack_MountList

- **Address:** `0x140092928`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int Pack_MountList(void *manager)`
- **Callers:** sub_14002BA44 (the startup path)
- **Callees:** Pack_MountOne

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Mounts the game's twelve stock data packs, by leaf name, through the one-pack mount call.

## Behavior

- V: builds twelve leaf names, 0000.pac through 0011.pac, and calls the single-pack mount for each.
- V: stops at the first negative result and returns that result; returns zero when all twelve mount.
- V: has one direct call site, in the startup function that also sets up the data directory.
- I: the twelve packs are the game's base data set; the numbering matches the retail pack folder.

## State touched

- Calls: [Pack_MountOne](Pack_MountOne.md)

## Notes

- V: whole body read (220 bytes).
- V: the name is the research name; the database label is the plain sub_ form.

## Open questions

- ?: what the manager's negative result means at startup beyond a failed mount.
