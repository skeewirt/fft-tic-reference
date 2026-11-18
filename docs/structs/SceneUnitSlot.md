# SceneUnitSlot

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 1352 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One of the 16 scene-unit records at 0x140D30038 (stride 0x548) that SceneUnit_BuildFromQueueEntry builds for a queued unit; the code addresses it by the pointer it returns, the in-use dword sits 8 bytes before that pointer (0x140D30030 + 1352 * slot).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="slot"></a>`0x8` | slot | `uint8` | V | The record's own slot number (0 to 15). |
| <a id="pool_index"></a>`0x9` | pool_index | `uint8` | V | Index of the look pool record the unit uses (0 to 14); the look slot that already exists. |
| <a id="sprite"></a>`0xA` | sprite | `uint8` | V | Low byte of the sprite number (the 'actor +0xA'). Readers compare it against 0xAA (four places) and use it to index the HD sheet table; SceneUnit_SyncSpriteFromPool copies it from the pool record's +1. |
| <a id="palette_index"></a>`0xB` | palette_index | `uint8` | I | Palette row 0 to 15 of the unit (taken from the CharShape row or the queue palette; stays 0 when the value is 16 or more). |
| <a id="sheet_slot"></a>`0x14` | sheet_slot | `uint16` | V | HD sheet slot: pool index + 20 for pool 0 to 8, else 17. |
| <a id="unit"></a>`0x148` | unit | `pointer` | V | The unit record (g_PreviewUnitTable entry); its byte +444 is the unit's index 0 to 20. |

## Behavior

- V: the sprite stays a byte here; a number of 256 or more reaches this record as its low byte.

## Open questions

None recorded.
