# SaveFile_StaticInitDescriptor

- **Address:** `0x14000E16C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int SaveFile_StaticInitDescriptor(void)`
- **Callers:** No direct callers; two data references (a constructor-table entry and a data slot).
- **Callees:** sub_14039DA00, sub_14039DA2C, memset, atexit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Static initialiser of a save-file descriptor object: fills in its product-code string, file name, a mode value and the object's vtable, then registers its own exit-time cleanup.

## Behavior

- V: copies a 9-character product-code string into the object and formats the file name string with a fixed name through a printf-style helper (`sub_14039DA00`).
- V: stores 3 in one dword, zeroes four other dwords, installs a vtable pointer, formats a second string with the pattern `FFT%04d` and a zero argument (`sub_14039DA2C`), and clears 0x70 bytes with memset.
- V: returns the result of `atexit` for the cleanup routine `sub_14060F7F8`.
- I: it is a C++ static constructor, because nothing calls it directly and the only references are two data entries (the CRT initialiser table among them).
- ?: what the object is used for at run time.

## Notes

Whole body read (164 bytes).

## Open questions

What reads the descriptor's strings and the mode value 3.
