# UnitSaveRecord

- **Kind:** structure
- **Area:** [Unit data](../areas/unit-data.md)
- **Size:** 600 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit as the save keeps it (54 records at g_UnitSaveData; copied whole into the save slot at +1304 + 600 n). The per-job state lives in arrays indexed by the job index (0..19 generic jobs, 20..23 spare).

## Fields

| Offset | Field | Type | Conf | Meaning | Indexed by registries | Written by | Read by |
|---|---|---|---|---|---|---|---|
| <a id="marker"></a>`0x0` | marker | `uint8` | V | 1..3 Ramza, 0x80 / 0x81 generic unit, 0x82 special; Unit_ResolvePreviewShape turns it and the job into a sprite shape. |  |  |  |
| <a id="slot_id"></a>`0x1` | slot_id | `uint8` | V | The unit's slot id (copied to the work record +2). |  |  |  |
| <a id="job"></a>`0x2` | job | `uint8` | V | Job id. | [JobIdSpace](../registries/JobIdSpace.md) |  |  |
| <a id="unlock_mask"></a>`0x2F` | unlock_mask | `uint8[3]` | V | Job unlock bits, most significant bit = job index 0 (24 bits). |  |  |  |
| <a id="learned"></a>`0x32` | learned | `uint8[66]` | V | Learned-ability bits: 3 bytes per job index (22 groups). |  |  |  |
| <a id="job_levels"></a>`0x74` | job_levels | `uint8[12]` | V | Job level nibbles, two per byte: an even index in the high nibble, an odd index in the low nibble (24 levels). |  | [UnitWork_PackJobLevels](../functions/UnitWork_PackJobLevels.md) |  |
| <a id="jp"></a>`0x80` | jp | `uint16[23]` | V | Current JP per job index (capped at 9999). |  |  |  |
| <a id="total_jp"></a>`0xAE` | total_jp | `uint16[23]` | V | Total JP per job index (capped at 9999); the job level follows from it and the GeneralJob curve. |  |  | [UnitWork_PackJobLevels](../functions/UnitWork_PackJobLevels.md) |
| <a id="name"></a>`0xDC` | name | `char[64]` | V | Unit name (chr_name). |  |  |  |
| <a id="spare_a"></a>`0x22E` | spare_a | `uint8[2]` | V | Unused by the save schema and by the game (zero in all 108 records of the owner's saves). |  |  |  |
| <a id="spare_b"></a>`0x234` | spare_b | `uint8[36]` | V | Unused, as spare_a. |  |  |  |

## Behavior

- V: SaveWork_PackFromLive and SaveWork_UnpackToLive copy all 600 bytes of every record, so the spare bytes travel with the slot.

## Referenced by

- Global instances: [g_UnitSaveData](../globals/g_UnitSaveData.md)
- Indexed by registries: [NewUnitStartRows](../registries/NewUnitStartRows.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
