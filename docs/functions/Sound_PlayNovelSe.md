# Sound_PlayNovelSe

- **Address:** `0x1402BA7C4`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int Sound_PlayNovelSe(uint16_t sound_id)`
- **Callers:** sub_1402F1868
- **Callees:** sub_1401D7808, sub_1401D5F34, memcpy, sub_1401D5E2C, sub_1401D7760, sub_14041EF2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays one of the common novel sound effects by id: it finds a free channel, loads the sound from the shared novel sound bank and starts it.

## Behavior

- V: the argument is the sound id; 0xE0FFFF is an invalid id that returns at once.
- V: it probes seven channels with sub_1401D7808 and takes the first free one.
- V: an occupied channel is released through sub_1401D5F34 before it is reused.
- V: the sound bank path is the string sound/common/novel.sab at 0x1407132F8.
- V: Mem_Alloc obtains the 0x38-byte sound object and sub_1401D5E2C loads the bank entry into it.
- V: sub_1401D7760 starts the sound with a zero volume ramp; a failed load returns without playing.
- V: the string list too long at 0x1406FA1C8 is the error path when no channel is free.
- I: the seven channels are the shared sound-effect slots, because the same probe loop appears in the other sound helpers.
- ?: the volume and pan values; only the zero ramp is passed here.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md)

## Notes

Whole function read (290 bytes). The bank path and the channel loop are the identifying facts.

## Open questions

None recorded.
