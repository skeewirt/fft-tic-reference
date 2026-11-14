# LookPoolRecord

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 13014 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One of the 15 sprite records at 0x140D005A0 (stride 0x32D6) that hold the loaded graphics of a look; records are shared by every unit that has the same sprite number.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="claimed"></a>`0x0` | claimed | `uint8` | V | Non-zero while the record is in use (the low byte of the sprite number written by LookPool_ClaimForSprite). |
| <a id="sprite"></a>`0x1` | sprite | `uint8` | V | Low byte of the sprite number the record holds; LookPool_ClaimForSprite and CharaPalette_ReloadForShape compare against it to find an equal look. |
| <a id="data"></a>`0x2` | data | `uint8[13012]` | ? | Palette and frame data of the look (filled by sub_14026E838 and sub_14026947C; layout not decoded here). |

## Behavior

- V: there are exactly 15 records (the index loop stops at 15); a request for a 16th distinct sprite gets index 0xFFFF and the unit is not created.
- V: LookPool_ResetForBattleLoad clears the first byte of every record before a load; the whole pool (0x2FA8A bytes) is copied into and out of the battle snapshot.

## Open questions

None recorded.
