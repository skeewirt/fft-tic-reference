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
| <a id="flags3"></a>`0x3` | flags3 | `uint8` | ? | Flag byte: bit 5 is tested before the learn roll; bit 7 is read as a sign and adds 0x2000 to the ability token in three functions. No bit has an established meaning; the most common value is 0x41. |
| <a id="flags4"></a>`0x4` | flags4 | `uint32` | ? | Flag dword read by the target resolver (bits 0, 1, 3; byte 1 compared with a distance counter), the action resolver (bits 0..1 and 24) and a sign test; two functions copy the whole dword into the current action. Probably the classic range / area / flag word (I). |

## Referenced by

- Described by tables: [AbilityAux](../tables/AbilityAux.md)

## Open questions

None recorded.
