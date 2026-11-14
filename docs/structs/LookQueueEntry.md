# LookQueueEntry

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of the 16-entry load queue that Battle_BuildRosterTeam, Battle_AddJoinedUnit and the scene preview code fill (LookQueue_Add) and CharaPalette_ReloadForShape consumes; entry n starts at 0x141856728 + 32 * n, the entry count is the dword at 0x141856720.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="arg_a"></a>`0x0` | arg_a | `uint8` | V | First argument of LookQueue_Add (for a roster unit: the unit's byte at +79). |
| <a id="arg_b"></a>`0x1` | arg_b | `uint8` | V | Second argument (unit byte +80). |
| <a id="arg_c"></a>`0x2` | arg_c | `uint8` | V | Third argument (the sex bit of unit byte +81). |
| <a id="arg_d"></a>`0x4` | arg_d | `uint16` | V | Fourth argument (low nibble of unit byte +81); passed on as the scene-unit creation argument a4. |
| <a id="sprite"></a>`0x6` | sprite | `uint16` | V | The sprite number. LookQueue_Add replaces a value of 170 or more (signed compare) by 1. Read by all three passes of CharaPalette_ReloadForShape. |
| <a id="palette"></a>`0x8` | palette | `uint16` | V | The palette byte of the unit (outPalette of Unit_ResolvePreviewShape). |
| <a id="slot_request"></a>`0xA` | slot_request | `uint16` | V | Requested scene-unit slot; the roster builders pass 255, meaning any free slot (sub_14026EB74 takes a request below 16 as a fixed slot). |
| <a id="unit"></a>`0x10` | unit | `pointer` | V | The unit record the entry belongs to (an entry of g_PreviewUnitTable), or null. |
| <a id="flag"></a>`0x18` | flag | `uint32` | V | Last argument of LookQueue_Add; sub_14026EB74 takes it as its a9 argument (it sets the words at scene unit +0xE and +0x3F0 to 1 when it is zero). |

## Behavior

- V: the count stops at 16: LookQueue_Add writes the entry at the current count first and only then adds one while the count is below 16, so a 17th call writes entry 16, which starts at 0x141856928 and so overlaps the 16 bytes at 0x141856930 (the variable the load steps set from scene variable 50).
- V: the battle snapshot (Battle_SaveCapture) copies the queue and Battle_RestoreSceneVars puts it back.

## Open questions

? whether any scene queues more than 16 entries (the roster builder queues at most 5 per call).
