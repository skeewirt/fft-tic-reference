# EventMusic_LoadTrack

- **Address:** `0x1401D7450`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventMusic_LoadTrack(int64_t obj, uint32_t channel, int32_t track)`
- **Callers:** EventScript_Run, at 0x14023D6D7, in the default branch of the switch that also has the cases 0x7F, 0x80 to 0x83 and 0x85; that branch is reached for opcode 0x84 and the call passes channel 9 and the operand plus 44. Also sub_1402BAB78 (at 0x1402BAC2B). One data reference at 0x143D35B6C.
- **Callees:** `sub_1401D964C`, `sub_1401D5F34`, Str_Format, `sub_140011750`, `sub_1401D5E2C` (which calls `sub_1401D5EB0`), `sub_1401D7760` (which calls sub_14009B550 and, for channel 8 only, `sub_1401D9784`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts background music track number `track` on channel `channel` of the global sound object, which is the body of opcode 0x84 with channel 9: a cache hit is handed to a replay helper, and a miss replaces that channel's resource with a new 56-byte resource for the track.

## Behavior

- V: forms the key `track + 1` (for opcode 0x84, operand + 45) and hashes its four bytes with 64-bit FNV-1a (offset basis 0xCBF29CE484222325, prime 0x100000001B3).
- V: looks the key up in the hash table at `obj + 1432`. The bucket is the hash AND the qword at `obj + 1456`; the chain is walked from the node at bucket +8 by following the qword at node +8 until the bucket's stop pointer. A node holds the key as a dword at +16 and a value as a dword at +20. The table's sentinel is `obj + 1408`; a chain that ends there, or at null, is a miss.
- V: on a hit it calls `sub_1401D964C(obj + 1384, node + 20)` and returns 0. Nothing else in this routine runs on a hit: the channel slot and the entry list are not changed.
- V: on a miss it reads the pointer at `obj + 8 * channel + 480`, which is `obj + 552` for channel 9. When that pointer is not null it releases it with `sub_1401D5F34` and writes 0 to that slot.
- V: formats the text 'sound/music/music_%05u.sab' with the track number into a 260-byte stack buffer using Str_Format. That buffer is not an argument of any later call in this routine.
- V: allocates 56 bytes with `sub_140011750` (heap at qword_140C696D0 + 32, alignment 8) and constructs the resource with `sub_1401D5E2C`. The constructor sets the vtable to GameSoundResource_140713440, zeroes the qwords at +8 and +16, the qword at +24, the dword at +32 and the word at +37, sets the floats at +44 and +48 to -1.0, and calls `sub_1401D5EB0` without any argument visible in this routine.
- V: if the constructor returns a non-null pointer, calls `sub_1401D7760(obj, channel)`. That helper goes over five pointers at `obj + 296 + 8 * channel + 184 * k` for k from 0 to 4 (for channel 9 these are obj+368, obj+552, obj+736, obj+920 and obj+1104). For each non-null pointer it calls `sub_14009B550` on the sound manager qword_143CD9B60 when the entry's +16 handle and the manager are both non-null, and then sets the entry's state byte at +36 to 4.
- V: appends a 24-byte node at the tail of the entry list whose sentinel is `obj + 280` (count at `obj + 288`; the node is allocated through the vtable of the allocator at `obj + 272`). The node's +16 is the new resource. It then stores the resource in the channel slot `obj + 8 * channel + 480`.
- V: returns 0 on every path. A null allocation or a null constructor result leaves the object unchanged.
- I: the new resource is meant to carry the music track. The file name built by Str_Format is not passed to any visible loader, so the file load itself is not proven by this routine (see open_q).

## State touched

- Calls: [Str_Format](Str_Format.md)

## Notes

The hash table at obj+1432 is only read here; no code in this routine inserts into it. The Str_Format result has no visible consumer in this routine.

## Open questions

Which code inserts into the cache table at obj+1432. Why the track file name built by Str_Format is not passed to a loader here, and what `sub_1401D5EB0` receives as its path, since `sub_1401D5E2C` calls it with no visible arguments. What channel 9 means in the sound object.
