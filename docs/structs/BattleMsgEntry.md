# BattleMsgEntry

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 524 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One slot of the battle message store: the kind, the kind-dependent argument, a message id and a 512-byte text buffer. The store is 40 entries at 0x20C stride after the message object's +8 (20,960 bytes); the dispatcher fills a slot and the resolver reads it back.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>`0x0` | kind | `uint32` | V | Message kind (1, 2, 3, 4, 5, 6, 7, 9 and above were read). Kinds 4 and 9 resolve an item name; kind 6 an ability name. |
| <a id="arg"></a>`0x4` | arg | `uint32` | V | Kind-dependent argument: a number (kind 1), a unit record or battle unit index (2, 3), an item id (4, masked with 0x7FF; 9), an ability id (6), or an id + 0xB7C4 (7). |
| <a id="message_id"></a>`0x8` | message_id | `uint32` | V | The kind-6 resolver stores id + 10000 here, a table-172 message id; no other writer was read. |
| <a id="text"></a>`0xC` | text | `char[512]` | V | The resolved text buffer: the resolver copies a name or a message into it (cap 511) and returns this address. |

## Behavior

- V: an entry is 0x20C bytes from the message object's +8; a slot above 0x27 returns null, so the store is 40 entries (20,960 bytes).
- V: the dispatcher writes the kind and the argument; the kind setters (kinds 1, 3, 6, 9) write +0 and +4; the resolver writes +0xC and, for kind 6, +8.
- V: Battle_Init clears 0x51E0 bytes at the object's +8, the whole store.
- V: the argument filler reads the same storage as one flat record (struct BattleMsgRecord), so its dword offsets run across entry boundaries; this per-entry view is the one the setters and the resolver use.

## Notes

V: the store sits at g_BattleMsgObject + 8. The text buffer is the entry's exact remainder (0x20C - 0xC = 0x200 = 512 bytes).

## Open questions

? the use of +8 outside kind 6; ? whether every kind uses +4 the same way.
