# BattleMsgRecord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The record the message object holds at +8: the values the argument filler reads for a message. Only the fields the filler touches are known; the names and roles below are inferred from that use.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>`0x0` | kind | `uint32` | I | Selector matched against 4 and 9 when the message needs an item name (argument filler). |
| <a id="actor_index"></a>`0x4` | actor_index | `uint32` | I | Index into g_BattleUnitTable (512-byte stride); the filler reads the unit's data through it. Its low 11 bits are the item id when kind is 4. |
| <a id="name"></a>`0xC` | name | `char[]` | I | Actor or record name used as a string argument. Length and encoding not established. |
| <a id="field_214"></a>`0x214` | field_214 | `uint32` | I | Read for some message ids; meaning not established. |
| <a id="fields_218"></a>`0x218` | fields_218 | `uint32[]` | I | A run of dwords read from here for some message ids; count and meaning not established. |
| <a id="field_41c"></a>`0x41C` | field_41C | `uint32` | I | Read for some message ids; meaning not established. |
| <a id="field_4184"></a>`0x4184` | field_4184 | `uint32` | I | Read for some message ids; meaning not established. |

## Behavior

- I: the offsets are the dword indices the filler uses (0, 1, 3, 133, 134.., 263, 4193) times 4; the fields the filler does not read are not listed.

## Notes

V: Battle_Init clears 0x51E0 bytes at the message object's +8. I: that block is the record storage, so the record is at most 20960 bytes. ?: the record's exact size and the fields between the listed offsets.

## Open questions

? the meaning of +0x214, +0x218, +0x41C and +0x4184; ? the name string's length and encoding.
