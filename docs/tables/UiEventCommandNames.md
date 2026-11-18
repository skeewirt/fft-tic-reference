# UiEventCommandNames

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140671FD0`
- **Rows:** 8 rows of 8 bytes
- **Keyed by:** command slot 0..7
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Command words of the event window markup (forced, wait, cursor, cursor end, no set, value set, time, branch). Verdict: text.

## Behavior

- V: seven of the eight strings are also pointed to by a second list of 16-byte {name pointer, 1} records in the same data area (0x14066F720..0x14066F9F0); the list is not recorded as a table of its own yet; the word in slot 6 is also addressed by two instructions
- V: eight string pointers read by the event window code that parses markup

## Notes

Our names. Tags: V.

## Open questions

- ?: exact meaning of each word
