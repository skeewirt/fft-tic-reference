# Deflate_Init2

- **Address:** `0x14040E9B0`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `int Deflate_Init2(void *strm, int level, int method, int windowBits, int memLevel, int strategy, const char *version, int streamSize)`
- **Callers:** sub_140028074, sub_14040E970 and sub_1405C7A30
- **Callees:** the stream's allocate callback, sub_14040F940 (free on failure), sub_14040EF50 (reset)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises a deflate compression stream (the embedded zlib-style compressor): validates the arguments, allocates the 5920-byte state and its buffers, then resets the stream.

## Behavior

- V: returns -6 (version error) unless the version string starts with '1' and the stream struct size is 88.
- V: installs default allocate and free callbacks into the stream when it has none; a level of -1 becomes 6.
- V: window bits: negative = raw stream (wrapper 0), above 15 = gzip wrapper (2, bits - 16), else the zlib wrapper (1).
- V: argument check: memLevel 1..9, method 8, window bits 8..15, level 0..9, strategy 0..4; otherwise returns -2 (stream error). A window of 8 bits is raised to 9.
- V: allocates the state (5920 bytes), the window (2 x window size), the previous-chain and head arrays (hash size 2^(memLevel+7)) and the pending buffer (2^(memLevel+6) x 4 bytes).
- V: when any allocation fails sets the state mark to 666, stores the message 'insufficient memory' (entry 6 of DeflateErrorMessages) in the stream, frees what it has and returns -4.
- V: otherwise stores the level, strategy and method in the state and returns the result of the stream reset function sub_14040EF50.

## Referenced by

- Reads tables: [DeflateErrorMessages](../tables/DeflateErrorMessages.md)

## Notes

Name is ours; the routine is a standard compression library function, described only as far as the executable shows. The message table entry is read by address (entry 6). The calls to sub_14040F940 and sub_14040EF50 are direct calls in the failure and final branches (seen in the disassembly); the cross-check flags them because they lie outside its scanned range.

## Open questions

None recorded.
