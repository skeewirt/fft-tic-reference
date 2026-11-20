# AbilityAuxRow

- **Kind:** structure
- **Area:** [Ability data](../areas/ability-data.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One auxiliary ability record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="jp_classic"></a>`0x0` | jp_classic | `uint16` | V | JP cost of the classic game. Equals the NXD cost for 502 of 512 abilities; the remaster rebalanced ten. The cost the game uses is the NXD one. |
| <a id="learn_percent"></a>`0x2` | learn_percent | `uint8` | V | Percent chance the learn routine grants the ability when not forced: success when rand(100) < value. Most abilities hold 100. |
| <a id="flags3"></a>`0x3` | flags3 | `uint8` | V | Flag byte. 0x80 = cannot be learned with JP: JobAbilityList_Build leaves an unlearned ability with the bit out of the Learn list, and a learned one gets token flag 0x6000 instead of 0x4000. 0x20 = can be learned by being hit: after an action with the bit set, a unit hit whose job skillset lists the ability learns it with chance learn_percent (sub_14030CD08). 0x40 is tested by the action name banner (sub_140238444: when clear, the kind-7 battle message is sent with its fifth argument 0; what that changes is not known). No reader of the other bits was found; the most common value is 0x41. |
| <a id="flags4"></a>`0x4` | flags4 | `uint32` | ? | Flag dword read by the target resolver (bits 0, 1, 3; byte 1 compared with a distance counter), the action resolver (bits 0..1 and 24) and a sign test; two functions copy the whole dword into the current action. Probably the classic range / area / flag word (I). |

## Referenced by

- Described by tables: [AbilityAux](../tables/AbilityAux.md)

## Open questions

None recorded.
