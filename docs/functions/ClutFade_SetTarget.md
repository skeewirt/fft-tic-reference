# ClutFade_SetTarget

- **Address:** `0x1402F4944`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int64_t ClutFade_SetTarget(int mode, int duration, int64_t bank, int64_t slot, int all, int16_t dr, int16_t dg, int16_t db, int unused)`
- **Callers:** sub_1401EAAF8, sub_1401EABB0, sub_1401EABF8, sub_1401EAC44, sub_1401EAC98, sub_1401EACF8, sub_1401EAD60, sub_140268880, ClutManager_Update, sub_1402F7A90, sub_1402F7ACC
- **Callees:** SceneVar_Read, sub_1400C961C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives one row of a palette bank (or all 16 rows) a new colour to move to, at once or as a timed fade.

## Behavior

- V: works on the 16 colours of row `slot` of bank `bank`, or on all 256 colours of the bank when `all` is 1; a bank is 2450 bytes (the multiplier in the code) and the banks follow the two dirty dwords of g_ClutManager.
- V: a colour whose three state bytes (red, green, blue) are all 0 is left alone: its three distance bytes are set to 31 (distance 0).
- V: the target per colour: mode 8 the bank's base row word (word_140C6BABA + 2450 * bank); modes 4, 9 and 11 that word's channels plus dr, dg, db; mode 5 its channels halved to 4 bits plus the offsets; modes 6 and 7 (blue + 3 green + 2 red) / 6 and / 12 of it plus the offsets.
- V: modes 0 to 3 are the same four counted from the colour's state bytes instead of the base row (0 as they are, 1 halved, 2 the grey sum / 6, 3 the grey sum / 12).
- V: each target channel is limited to 31 and put to 0 below 1; when all three are 0 blue becomes 1.
- V: with a duration of 0 the state bytes and the final image word (word_140C73B70 + 512 * bank) take the target at once; else the three distance bytes get target - state + 31.
- V: after the colours, with a duration: each row's 9-byte timer gets active 1, step 0, frame counter 0, the duration twice, and for modes 9 and 11 the ping-pong byte 1 with the three offsets kept; with a duration of 0 the timers are cleared and the dirty dword is set.
- V: mode 10 clears the ping-pong byte of the row (or of all 16) and returns.
- V: when the dword at 0x142E80048 is non-zero and the bank is 0 or 1 it first reads scene variable 39 and calls sub_1400C961C with the mode, the duration and the offsets.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [ClutManager_Update](ClutManager_Update.md)
- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_1402F4944). Structure: ClutBank. Seen live 2026-11-11: the unit under the cursor at deployment pulses by a fade of this function (target = row + 8 on all channels, 8 steps, ping-pong).

## Open questions

? what the last argument is for; ? what sub_1400C961C does with the same request for banks 0 and 1.
