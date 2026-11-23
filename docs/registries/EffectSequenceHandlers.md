# EffectSequenceHandlers

- **Kind:** registry
- **Area:** [Battle](../areas/battle.md)
- **Resolved by:** [EffectSequence_Run](../functions/EffectSequence_Run.md)
- **Values stored in:** [EffectSequenceEntry.kind](../structs/EffectSequenceEntry.md#kind)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 23 sequence kind handlers of the battle effect sequence: the kind byte at +3 of an effect sequence entry indexes this pointer table, and EffectSequence_Run calls the handler once per frame with the entry as the current one. Slot 0 and five others point at one stub that returns 0. Kinds above 22 end the walk.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="no-op stub 0"></a>0 | `no-op stub 0` | `stub at 0x140010FA4 (returns 0)` | V | Returns 0 at once, so an entry of this kind is retired on its first frame. |
| <a id="effectsequence_projectileflight"></a>1 | `EffectSequence_ProjectileFlight` | `0x14031342C` | V | Flies a model along a heading over the ground height and queues a short kind 5 entry when it ends. |
| <a id="effectsequence_hitflashsprites"></a>2 | `EffectSequence_HitFlashSprites` | `0x1403138DC` | V | Flashes the unit palette and spawns sprite groups 0 and 1 (9 for sub-kind 3). |
| <a id="effectsequence_spawngroup16"></a>3 | `EffectSequence_SpawnGroup16` | `0x140313E10` | V | Plays the sprites of effect sprite group 16. |
| <a id="effectflash_start"></a>4 | `EffectFlash_Start` | `0x140313F34` | V | The screen flash tinted by an element colour. |
| <a id="effectsequence_holdtwoframes"></a>5 | `EffectSequence_HoldTwoFrames` | `0x140314A40` | V | Counts its state up and ends on the third frame. |
| <a id="effectsequence_spawngroup10withcue"></a>6 | `EffectSequence_SpawnGroup10WithCue` | `0x140314A74` | V | Plays group 10 and sound cue 7. |
| <a id="no-op stub 7"></a>7 | `no-op stub 7` | `stub at 0x140010FA4 (returns 0)` | V | Same stub as slot 0. |
| <a id="effectsequence_spawngroup6"></a>8 | `EffectSequence_SpawnGroup6` | `0x140314BA4` | V | Plays the sprites of group 6. |
| <a id="effectsequence_spawngroup7attile"></a>9 | `EffectSequence_SpawnGroup7AtTile` | `0x140314CC8` | V | Plays group 7 after a terrain offset from the unit's tile. |
| <a id="no-op stub 10"></a>10 | `no-op stub 10` | `stub at 0x140010FA4 (returns 0)` | V | Same stub as slot 0. |
| <a id="no-op stub 11"></a>11 | `no-op stub 11` | `stub at 0x140010FA4 (returns 0)` | V | Same stub as slot 0. |
| <a id="effectsequence_spawngroup8withcue"></a>12 | `EffectSequence_SpawnGroup8WithCue` | `0x140314EA4` | V | Plays group 8 and sound cue 0x21. |
| <a id="effectsequence_spawngroup5rising"></a>13 | `EffectSequence_SpawnGroup5Rising` | `0x140314FD4` | V | Plays group 5 with a start offset that moves each frame. |
| <a id="no-op stub 14"></a>14 | `no-op stub 14` | `stub at 0x140010FA4 (returns 0)` | V | Same stub as slot 0. |
| <a id="effectsequence_spawngroup4perunit"></a>15 | `EffectSequence_SpawnGroup4PerUnit` | `0x14031510C` | V | Plays up to two sprites of group 4 with state indexed by the entry's byte +2. |
| <a id="no-op stub 16"></a>16 | `no-op stub 16` | `stub at 0x140010FA4 (returns 0)` | V | Same stub as slot 0. |
| <a id="effectsequence_spawngroup3cluster"></a>17 | `EffectSequence_SpawnGroup3Cluster` | `0x14031536C` | V | Plays up to 24 sprites of group 3 from a shared pool. |
| <a id="effectpalette_step"></a>18 | `EffectPalette_Step` | `0x140315620` | V | The full-screen palette effect from six seed colours. |
| <a id="effectsequence_spawngroup15"></a>19 | `EffectSequence_SpawnGroup15` | `0x1403159EC` | V | Plays the sprites of group 15. |
| <a id="handler at 0x140315b10 (no sheet yet)"></a>20 | `handler at 0x140315B10 (no sheet yet)` | `0x140315B10` | V | The pointer is read from the table; the function is about 1.6 KB and was not read here. |
| <a id="effectsequence_spawngroup11"></a>21 | `EffectSequence_SpawnGroup11` | `0x140316160` | V | Plays the sprites of group 11. |
| <a id="effectsequence_spawngroup14ring"></a>22 | `EffectSequence_SpawnGroup14Ring` | `0x140316284` | V | Thirty group 14 sprites circling a point, then fading. |

## Behavior

- V: Table at 0x140682F30, 23 pointers of 8 bytes; a table of 4-byte rows of per-effect-kind words follows at 0x140682FF0.
- V: The sprite handlers share one state convention in the entry's dword +8: 1 set-up, 2 running, 3 running without new spawns; a handler returns 0 to retire the entry.

## Open questions

None recorded.
