# ClassicLookDataHasEightBufferPlaces

- **Kind:** observed behaviour
- **Scope:** engine (battle unit looks, low-resolution path)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_14026E838](../functions/sub_14026E838.md), [sub_140260CF0](../functions/sub_140260CF0.md), [SceneUnit_LoadExtraPage](../functions/SceneUnit_LoadExtraPage.md), [g_PoolFrameBuffers](../globals/g_PoolFrameBuffers.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The low-resolution (classic) image of a look goes to one of three kinds of place by its pool number, and each kind is full at 15 looks: video memory for pools 0..8, eight 32 KB buffers (2..7 used) for pools 9..14, and eight 4 KB blocks for the second sheet of pools 9..14. A classic quad names its buffer in 3 bits.

## Behavior

- V: sub_14026E838 uploads pools 0..8 to video memory at x = 64 x (pool / 8 + 13), y = 32 x (pool % 8 + 8) (the same rule in SceneUnit_LoadExtraPage), and copies pools 9 and up (test pool >= 9) to the 32 KB buffer 0x1437ADF4C + 0x8000 x (pool - 7), storing its pointer at g_PoolFrameBuffers[pool - 7], and the second 4 KB to byte_1437B5F4C + 4096 x (pool % 8).
- V: g_PoolFrameBuffers has 8 pointers (0x1411A3788; dword_1411A37C8 follows); entry 1 is the 4 KB block area (0x1437B5F4C, itself buffer 1's place), entries 2..7 pools 9..14; buffer 8 would start at 0x1437EDF4C, where event script state lives (EventScript_SkipTick, Battle_SaveCapture and others).
- V: sub_140260CF0 gives a quad of pools 9..14 the buffer number pool - 7 through an explicit list of the six pools (0x140260E5C), and writes it as (n | 0xFFF8) << 12 into the quad's texture word (+0x1E, 0x140261628): only 3 bits carry the buffer, so a buffer 8 or above aliases buffers 0..7; sub_14025ED60 reads the pointer back by that number.
- V: SceneUnit_LoadExtraPage has its own explicit list of pools 9..14 (0x14026C3CF) that sends a second sheet to the 4 KB block pool % 8; with pools past 15 the block index wraps onto pool 9's (pool 17 -> 1).
- I: so a look past 15 has no classic place: it needs a new buffer, a new pointer slot and a texture word that can name it (a hook where the quad is built and where sub_14025ED60 reads it), or the classic path left unused for those pools while HD is on.

## Open questions

? whether the classic quad of a unit is drawn at all while the HD layer is on (g_GraphicsLevel >= 2); ? what buffer 0 holds.
