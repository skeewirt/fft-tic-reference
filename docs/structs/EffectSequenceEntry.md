# EffectSequenceEntry

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 96 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of the battle effect sequence list (an array at 0x1437A5C40, 96 bytes each). EffectSequence_Run makes one entry current (global pointer qword_14186D768) and calls the handler its kind byte selects. Fields below are those the sequence handlers read or write.

## Fields

| Offset | Field | Type | Conf | Meaning | Indexed by registries |
|---|---|---|---|---|---|
| <a id="index"></a>`0x2` | index | `uint8` | V | Index used by EffectSequence_SpawnGroup4PerUnit to select its 8-byte state record. |  |
| <a id="kind"></a>`0x3` | kind | `uint8` | V | Index into the effect sequence handler table; EffectSequence_ProjectileFlight writes 5 here in a new entry. | [EffectSequenceHandlers](../registries/EffectSequenceHandlers.md) |
| <a id="effect_kind"></a>`0x4` | effect_kind | `uint16` | V | The effect kind: read by EffectFlash_Start, passed to the sprite animation check, and written (21) in the entry the flight handler queues. |  |
| <a id="selector"></a>`0x6` | selector | `uint16` | V | Read by EffectFlash_Start as the element mask and by EffectSequence_SpawnGroup3Cluster as an index into EffectBlendWeights, and by EffectSequence_HitFlashSprites as the value added to 31424 for its first-set sprites. |  |
| <a id="state"></a>`0x8` | state | `uint32` | V | 1 set-up, 2 running, 3 running without new spawns (the generic sprite handlers). |  |
| <a id="frame"></a>`0xC` | frame | `uint16` | V | Frame counter, cleared at set-up and incremented per frame. |  |
| <a id="unit_slot_a"></a>`0x14` | unit_slot_a | `uint8` | V | Unit slot looked up with SceneObject_FindBySlot by EffectSequence_ProjectileFlight. |  |
| <a id="unit_slot_b"></a>`0x20` | unit_slot_b | `uint8` | V | Unit slot looked up by the flight, hit-flash and tile handlers. |  |
| <a id="sub_kind"></a>`0x21` | sub_kind | `uint8` | V | A variant byte read by EffectSequence_HitFlashSprites (1, 3, 4 change its work) and by the flight handler. |  |
| <a id="flag_44"></a>`0x2C` | flag_44 | `uint32` | ? | Tested non-zero by the flight handler before it looks up the two scene objects. |  |
| <a id="live_sprites"></a>`0x30` | live_sprites | `uint16` | V | Count of the entry's live sprites (generic sprite handlers). |  |
| <a id="end_counter"></a>`0x32` | end_counter | `uint16` | V | Counts up once the sprites are gone; the entry ends the frame after it reaches 1. The ring handler uses it as a fade counter instead. |  |
| <a id="sprite_slots"></a>`0x34` | sprite_slots | `uint8[]` | V | Sprite slot ids of the entry (up to the group's live limit; 30 in the ring handler). |  |
| <a id="buffer"></a>`0x58` | buffer | `pointer` | V | Heap buffer owned by the entry (allocated by the flight and hit-flash handlers). I: EffectSequence_Run frees an attached object here; that was not read for this field. |  |

## Open questions

? the fields between the ones listed; how an entry is created for a given ability.
