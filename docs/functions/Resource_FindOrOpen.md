# Resource_FindOrOpen

- **Address:** `0x140091124`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void *Resource_FindOrOpen(void *manager, const char *path, unsigned hash, char flag, void *out)`
- **Callers:** 36 direct sites in about 27 functions, including GUIFontSlots_AcquireTexturePart, GUIFontSlots_AcquireImage,
- **Callees:** Resource_AcquireHandle (reader open)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens a game resource by path through the mounted packs, after normalising the path, and returns a handle or null.

## Behavior

- V: normalises the path: a backslash becomes a forward slash and an upper-case ASCII letter becomes lower-case.
- V: an already-normalised path is used in place; otherwise a copy is built in a 256-byte stack buffer.
- V: a normalised path of 256 bytes or more hits a runtime check and aborts.
- V: finds the last dot in the path and passes the base name, the hash, the flag, the extension and a 32-byte state block to the
  reader open.
- V: the caller's fifth stack argument is read as a pointer to that 32-byte state block.
- V: returns whatever the reader open returns.
- I: a missing file yields null, because the UI callers treat a null result as a failed load.
- I: lookup is case-insensitive because of the lower-casing; the readers' callers rely on it.
- I: the extension is passed separately so compressed or localised entries can be resolved by suffix.
- V: 36 call sites, from UI texture parts and nxd tables to shaders and the startup icon check.

## State touched

- Calls: [Resource_AcquireHandle](Resource_AcquireHandle.md)

## Notes

- V: head and the whole normalisation loop were read; the reader open is Resource_AcquireHandle (0x1400912B4).

## Open questions

- ?: what the 32-byte state block holds beyond the hash and flags.
