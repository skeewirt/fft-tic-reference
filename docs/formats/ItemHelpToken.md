# ItemHelpToken

- **Kind:** file format
- **Area:** [Data access](../areas/data.md)
- **Read by:** [sub_140226208](../functions/sub_140226208.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 0x6800-tagged text id that asks for an item's help string: kind 13, index = item id. Five functions build it at six sites, with three index masks (0x3FF, 0x7FF, a runtime register) or none, and store it in the shared help slot 0x1418736B4; a sixth function only bounds a script operand at 0x105. It is a pool id, not the Item-en description the equipment detail panel uses.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="token"></a>+0 | token | `uint16` | V | 0x6800 + item id: the tag is added at the builder and the id becomes the low 11 bits. |
| <a id="kind"></a>+0 (kind) | kind | `5 bits` | V | 13 (0x6800 >> 11): the item help pool. |
| <a id="index"></a>+0 (index) | index | `11 bits` | V | The item id. The builders mask it with 0x3FF (two sites), 0x7FF (one), a runtime register (one) or not at all (two). |
| <a id="help_slot"></a>store | help_slot | `uint32` | V | The shared help slot 0x1418736B4; 32 dword stores exist in the code. Its three readers are a compare, a sign-extended render command and the adder of 0x7800 / 0x9800. The u16 at +4 is a separate field. |

## Behavior

- V: the token is built at six sites in five functions: sub_1402D58EC, sub_1402D5FE4, sub_140301ED8, sub_140333974 (two sites) and sub_1403343E4. A seventh 0x6800 site, in sub_1403015A4, only bounds a script operand.
- V: the event-script builder sub_140301ED8 passes 0x6800 + (operand & 0x7FF) to the generic decoder; the script builder sub_1403015A4 only compares an operand with 0x6800 and bounds its index at 0x105.
- V: ids from 0x800 up do not stay item help: 0x6800 + N becomes 0x7000, the ability kind, and the decoder answers it from the ability name source.
- V: the equipment detail panel does not use this token: EquipDetail_SetHelpText reads the Item-en row's description field (column +16) directly.
- I: the pool 13 strings are the item help entries; the pool content was not read.

## Notes

V: the help slot is shared with the job and command help paths, which load it with 0x7800 or 0x9800 ids (sub_140366FE0 adds those tags to a stored index), so a reader cannot take kind 13 from the slot alone.

## Open questions

? the exact string a token names versus the Item-en description; ? which screens show the token rather than the row description.
