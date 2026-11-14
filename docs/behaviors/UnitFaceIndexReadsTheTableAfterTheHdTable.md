# UnitFaceIndexReadsTheTableAfterTheHdTable

- **Kind:** observed behaviour
- **Scope:** engine (party faces)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_GetFaceIndex](../functions/Unit_GetFaceIndex.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit_GetFaceIndex reads the face index of a monster job from the table right after the HD sheet entry table, through a virtual base that falls inside the HD table, so an address-range census counts it as an HD reader by mistake.

## Behavior

- V: for a job word at +0x24 between 94 and 141 the function returns dword_140715378[job]; 0x140715378 is 392 bytes into the HD table, and the lowest address read (job 94) is 0x1407154F0, past the HD table's 680 bytes.
- V: 0x1407154F0 holds 48 dwords, 62 to 77, three jobs per monster family (g_MonsterFaceIndexByJob).

## Open questions

None recorded.
