# ClutBank

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 2450 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One of the 14 banks of the palette manager (g_ClutManager, from +8): 16 rows of 16 colours with a timer per row, the state of every colour and the bank's base rows.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="header"></a>`0x0` | header | `uint16` | V | Set to 1 when the manager is reset (sub_1402F79F8); not read in the code studied. |
| <a id="timers"></a>`0x2` | timers | `uint8[16][9]` | V | Per row: active (0 / 1), step counter, frame counter, duration, the duration kept for the ping-pong, ping-pong (0 none, 1 and 2 the two directions) and the three kept offsets (ClutFade_SetTarget writes them, ClutManager_Update steps them). |
| <a id="colours"></a>`0x92` | colours | `uint8[256][7]` | V | Per colour: red, green, blue (5 bits each, as they show), bit 15 of the word, and the three distances to the fade target + 31. |
| <a id="base"></a>`0x792` | base | `uint16[256]` | V | The bank's base rows as words: the row a fade of mode 8 returns to. UnitClut_TintRow writes the tinted row of a unit slot here for bank 3. |

## Behavior

- V: bank b starts at 0x140C6B328 + 2450 * b; its colours also stand as words in row b of g_ClutImage, which is what gets uploaded.
- V: bank 3 holds the battle units' colours by unit slot (UnitClut_TintRow); sub_1402F7594 copies a raw row into a bank chosen by its caller (SceneUnit_RunPlacement uses bank 10).

## Referenced by

- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The names are ours.

## Open questions

? what the other banks hold.
