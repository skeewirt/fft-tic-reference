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
| <a id="union_group"></a>`0x3` | union_group | `uint8` | I | Saved under the label union; a small group value of the unit (meaning not read here). |  |  |  |
| <a id="sex"></a>`0x4` | sex | `uint8` | V | Saved as sex; the unit gender (marker 0x80 and 0x81 also encode it). |  |  |  |
| <a id="birth_value_a"></a>`0x5` | birth_value_a | `uint8` | I | First of two birth values (saved as birth_1); with the second it gives the zodiac sign. |  |  |  |
| <a id="birth_value_b"></a>`0x6` | birth_value_b | `uint8` | I | Second birth value (saved as birth_2). |  |  |  |
| <a id="secondary_skillset"></a>`0x7` | secondary_skillset | `uint8` | V | Saved as sub_command: the unit secondary skillset id. |  |  |  |
| <a id="reaction_ability"></a>`0x8` | reaction_ability | `uint8[2]` | I | Two bytes (saved as reaction_ability_1 and _2) that hold the equipped reaction ability id, low byte first. |  |  |  |
| <a id="support_ability"></a>`0xA` | support_ability | `uint8[2]` | I | Equipped support ability id, two bytes as above. |  |  |  |
| <a id="movement_ability"></a>`0xC` | movement_ability | `uint8[2]` | I | Equipped movement ability id, two bytes as above. |  |  |  |
| <a id="equipped_items"></a>`0xE` | equipped_items | `int16[7]` | V | Seven equipped item ids (saved as equip_item, signed 16-bit each); slot order as the equipment screen rows. |  |  |  |
| <a id="exp"></a>`0x1C` | exp | `uint8` | V | Experience points of the current level (saved as exp). |  |  |  |
| <a id="level"></a>`0x1D` | level | `uint8` | V | Unit level. |  |  |  |
| <a id="start_brave"></a>`0x1E` | start_brave | `uint8` | V | Starting bravery (saved as start_bcp). |  |  |  |
| <a id="start_faith"></a>`0x1F` | start_faith | `uint8` | V | Starting faith. |  |  |  |
| <a id="base_hp_max"></a>`0x20` | base_hp_max | `uint8[3]` | V | Base maximum HP, three bytes (saved as hp_max_base); packing of the three bytes not read here. |  |  |  |
| <a id="base_mp_max"></a>`0x23` | base_mp_max | `uint8[3]` | V | Base maximum MP, three bytes. |  |  |  |
| <a id="base_speed"></a>`0x26` | base_speed | `uint8[3]` | V | Base speed (saved as wt_base), three bytes. |  |  |  |
| <a id="base_physical"></a>`0x29` | base_physical | `uint8[3]` | V | Base physical attack (saved as at_base), three bytes. |  |  |  |
| <a id="base_magic"></a>`0x2C` | base_magic | `uint8[3]` | V | Base magic attack (saved as mat_base), three bytes. |  |  |  |
| <a id="unlock_mask"></a>`0x2F` | unlock_mask | `uint8[3]` | V | Job unlock bits, most significant bit = job index 0 (24 bits). |  |  |  |
| <a id="learned"></a>`0x32` | learned | `uint8[66]` | V | Learned-ability bits: 3 bytes per job index (22 groups). |  |  |  |
| <a id="job_levels"></a>`0x74` | job_levels | `uint8[12]` | V | Job level nibbles, two per byte: an even index in the high nibble, an odd index in the low nibble (24 levels). |  | [UnitWork_PackJobLevels](../functions/UnitWork_PackJobLevels.md) |  |
| <a id="jp"></a>`0x80` | jp | `uint16[23]` | V | Current JP per job index (capped at 9999). |  |  |  |
| <a id="total_jp"></a>`0xAE` | total_jp | `uint16[23]` | V | Total JP per job index (capped at 9999); the job level follows from it and the GeneralJob curve. |  |  | [UnitWork_PackJobLevels](../functions/UnitWork_PackJobLevels.md) |
| <a id="name"></a>`0xDC` | name | `char[64]` | V | Unit name (chr_name). |  |  |  |
| <a id="name_number"></a>`0x11C` | name_number | `uint8[2]` | V | Saved as name_no: the number that picks a generated name. |  |  |  |
| <a id="in_trip"></a>`0x11E` | in_trip | `uint8` | V | Saved as in_trip: set while the unit is away on an errand. |  |  |  |
| <a id="parasite"></a>`0x11F` | parasite | `uint8` | V | Saved as parasite (meaning of the values not read here). |  |  |  |
| <a id="egg_color"></a>`0x120` | egg_color | `uint8` | V | Saved as egg_color (monster egg look). |  |  |  |
| <a id="kill_count"></a>`0x121` | kill_count | `uint8` | V | Saved as pspKilledNum: a per-unit kill counter. |  |  |  |
| <a id="order_id"></a>`0x122` | order_id | `uint8` | V | Saved as unit_order_id. |  |  |  |
| <a id="starting_team"></a>`0x123` | starting_team | `uint8` | V | Saved as unit_starting_team. |  |  |  |
| <a id="join_id"></a>`0x124` | join_id | `uint8` | V | Saved as unit_join_id. |  |  |  |
| <a id="current_equip_set"></a>`0x125` | current_equip_set | `uint8` | V | Saved as current_equip_set_number: which of the three equipment sets is active. |  |  |  |
| <a id="equip_sets"></a>`0x126` | equip_sets | `SaveEquipSet[3]` | V | Three saved equipment sets of 88 bytes each at +0x126, +0x17E and +0x1D6 (see SaveEquipSet). |  |  |  |
| <a id="name_key"></a>`0x230` | name_key | `int32` | V | Saved as charaNameKey: the text key of the unit name (32-bit). |  |  |  |
| <a id="spare_a"></a>`0x22E` | spare_a | `uint8[2]` | V | Unused by the save schema and by the game (zero in all 108 records of the owner's saves). |  |  |  |
| <a id="spare_b"></a>`0x234` | spare_b | `uint8[36]` | V | Unused, as spare_a. |  |  |  |

## Behavior

- V: SaveWork_PackFromLive and SaveWork_UnpackToLive copy all 600 bytes of every record, so the spare bytes travel with the slot.

## Referenced by

- Described by tables: [UnitSaveSlots](../tables/UnitSaveSlots.md)
- Global instances: [g_UnitSaveData](../globals/g_UnitSaveData.md)
- Indexed by registries: [NewUnitStartRows](../registries/NewUnitStartRows.md), [UnitIdentityIds](../registries/UnitIdentityIds.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
