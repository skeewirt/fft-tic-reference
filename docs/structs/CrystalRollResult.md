# CrystalRollResult

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 1393 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The block Unit_RollAbilityLearning fills at dword_1411A6AB0 (1393 bytes, the next data starts at 0x1411A7024) when a unit stops on a crystal or chest. It holds the roll's outcome for the 19 stock jobs and is read only by the crystal flow: the pickup resolver, the window that lists the abilities, and the function that ORs the learned slots into the picker's record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="outcome"></a>`0x0` | outcome | `int32` | V | -1 no unit on the tile (the other fields are not written), 4 chest, 2 rolled, 3 rolled with at least one slot learned (bit 0 set at the end). Read by sub_14020435C (chest test) and sub_140323D1C (window mode). |
| <a id="dead_unit_slot"></a>`0x5A` | dead_unit_slot | `uint8` | V | Slot of the Crystal / Chest unit on the tile (byte_1411A6B0A). Written by the roll; no reader found. |
| <a id="learned_slots"></a>`0x18` | learned_slots | `uint8[57]` | V | 19 jobs x 3 bytes, the job index i at +24 + 3 x i: bit (0x80 >> slot) of byte slot / 8 is set for each skillset slot 0..23 whose roll succeeded. Read by sub_1402722D8, which ORs the 57 bytes into the picker's learned bits at record +162. |
| <a id="chest_item"></a>`0x5C` | chest_item | `uint16` | V | Item id chosen for a chest (word_1411A6B0C, from sub_1402723EC; 255 while a battle is simulated). Read by sub_14020435C, sub_140323D1C and sub_1402722D8. |
| <a id="learned_ability_set"></a>`0x5E` | learned_ability_set | `uint8[64]` | V | 512-bit set: bit (ability & 7) of byte ability / 8 for every ability that rolled successfully, abilities 0..0x1FF only (an id above 0x1FF is dropped here although its slot is still marked in learned_slots). Cleared whole at the start. Read by sub_140323D1C to build the window's list. |
| <a id="job_id"></a>`0x9E` | job_id | `uint8[19]` | V | The job id the walk used for each index it entered (74 + index, or the character byte for index 0). Cleared at the start. Read by sub_140323D1C as the job of a listed ability. |
| <a id="per_job_ability_set"></a>`0xB1` | per_job_ability_set | `uint8[19][64]` | V | Per job index i, the same 512-bit set restricted to that job, at +177 + 64 x i. Only the first 8 bytes of each entry are cleared at the start, so bits for abilities 64 and above can be left from an earlier roll. Read by sub_140323D1C to find which job a listed ability came from. |
| <a id="unknown_04_23"></a>`0x4` | unknown_04_23 | `uint8[20]` | ? | Not written or read by any code found. |

## Behavior

- V: no code outside Unit_RollAbilityLearning, sub_14020435C, sub_1402722D8 and sub_140323D1C refers to any byte of the block (a scan of every cross reference from 0x1411A6AB0 to 0x1411A7040).
- V: sub_140243A60 (the battle state snapshot) copies only the pointer qword_140D40810 that points at this block, not the block, and zeroes the pointer when it restores.

## Notes

Written by sub_140271EFC; sheet of each reader linked from the CrystalAbilityLearning flow.

## Open questions

? what the unread bytes +4..+23, +81..+89 and +91 are (they are never written either); ? whether the stale per-job bits matter (the window picks the first index whose set holds the bit, so a stale bit could name the wrong job).
