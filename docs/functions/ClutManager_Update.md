# ClutManager_Update

- **Address:** `0x1402F5F78`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int64_t ClutManager_Update(void)`
- **Callers:** sub_140210AF0
- **Callees:** ClutFade_SetTarget, sub_1400C98C4, sub_14024A528, sub_1402F5428, sub_1402F57D0, sub_1402F5C20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The palette manager's step, once a frame from the battle loop: colour cycles, three screen-colour fades and the timed fades of the 14 palette banks.

## Behavior

- V: returns at once while the pause manager's byte +24 has bit 4.
- V: first runs the colour-cycle records (10 bytes each, walked from 0x140C739AD, the byte after each record's active flag): when a record's counter reaches its period it rotates the colours between two indices of a bank by one place (state bytes, base row words and final image words).
- V: then steps three colour fades kept as 16.16 fixed-point values with their own counters (blocks at 0x140C73924, 0x140C73964 and 0x140C73988); two of them hand their colour to sub_14024A528 with the ids 90 and 99.
- V: then, per bank (14 banks) and per row with an active timer: a duration below 4 moves every colour by one entry of the 8-step table (byte_140681FE0[8 * distance byte + step]) each frame; a duration of 4 or more moves it by one entry of the 32-step table (byte_1406821F0[32 * distance byte + step]) once every duration / 4 frames.
- V: a colour whose three state bytes are all 0 is not moved; a colour that comes out all 0 gets blue 1; the moved colour is written to the state bytes and to the final image word, and the dirty dword is set.
- V: when the step counter reaches 8 (or 32): a row with ping-pong byte 1 is given mode 8 through ClutFade_SetTarget and the byte becomes 2; with byte 2 it is given mode 9 with its kept offsets and the byte becomes 1; any other value ends the fade (the active byte is cleared).
- V: the same stepping exists for a whole bank at once (256 colours, the bank's first timer).

## State touched

- Calls: [ClutFade_SetTarget](ClutFade_SetTarget.md)

## Referenced by

- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_1402F5F78). Structure: ClutBank. The running sums of both step tables, for every distance -31..31, are floor(d * k / n) for d >= 0 and max(d, floor((d * k - 1) / n)) for d < 0 (compared with all 63 x 40 table entries in the database).

## Open questions

? what the three screen-colour fades colour (ids 90 and 99 of sub_14024A528); ? the last block after the banks (a float at +6070652 of the object at g_CharaRenderer +148080).
