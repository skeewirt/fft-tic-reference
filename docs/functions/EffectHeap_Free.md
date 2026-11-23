# EffectHeap_Free

- **Address:** `0x14038DC58`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `unsigned __int64 *__fastcall EffectHeap_Free(__int64 block)`
- **Callers:** EffectSprite_StepAnimation, sub_14031A840, and the effect callbacks sub_140348924, sub_14034B9F0, sub_14034CC14, sub_14034DE90, sub_14034FB4C, sub_140350250, sub_140350DE4, sub_1403523D4, sub_1403554C4, sub_1403569A8, sub_1403585D4, sub_140358CCC, sub_14035C330, sub_14035D5F0, sub_14035DDAC, sub_14035E3A8 and others
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a block to the effect heap: removes it from its class's list of live blocks and puts it back into the address-sorted free list, merging with free neighbours.

## Behavior

- V: the block header sits 16 bytes before `block`: the header's first qword is a link, the u16 at header+8 is the size in 16-byte units and the signed 16-bit value at header+10 is a class index.
- V: the block is unlinked from the singly linked list whose head is `qword_143C51DA0[2 * class]`.
- V: the free list is circular and sorted by address with its rover in `qword_143C51D90`; the function walks it to find the neighbours of the header, merges the block with the following free block when they touch and with the preceding one when they touch, and leaves the rover at the preceding block.
- V: the return value is a computed pointer that the callers do not use.
- I: this is the free half of the effect heap whose allocator is `sub_14038DBDC` (rests on the allocator being called with a size and a class; not read).

## Referenced by

- Called by: [EffectSprite_StepAnimation](EffectSprite_StepAnimation.md)

## Notes

V: whole body read (168 bytes); a first-fit free-list release with coalescing. The name is ours.

## Open questions

?: the meaning of the class index and the heap's size.
