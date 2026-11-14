# g_ZeroPair

- **Kind:** global
- **Address:** `0x143D12018`
- **Type:** `int32[2]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A pair of zeros in uninitialised data (no writer; the database shows -1 for it because the bytes are not stored in the file, but the running game reads 0, live 2026-10-30). The UI renderer constructor and UIRender_PrepareLayers copy it into the two layer atlas shelves as the starting cursor (x, y) = (0, 0); AtlasShelf_Alloc copies it again when it opens a new page. Other code reads it as a zero vector.

## Open questions

None recorded.
