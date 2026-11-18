# AudioCueLoadErrorNames

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x14077C218`
- **Rows:** 7 rows of 8 bytes
- **Keyed by:** error code 0..6 (I)
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Names of the error codes of the audio cue sheet loader: no error, failed to register file, failed to open, failed to load wave bank, invalid wave bank path, failed to calculate work size, failed to allocate memory. Verdict: text.

## Behavior

- V: no other instruction or pointer addresses any of the seven strings, and none has a reference inside it
- V: seven consecutive string pointers; the strings have no other reference
- I: indexed by a computed address inside the audio library, so no direct instruction reference exists

## Notes

Our names. Tags: V layout, I use.

## Open questions

None recorded.
