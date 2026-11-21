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
- V: sub_14025CDCC decodes the texture word: (word >> 12) & 7 is the buffer, and sub_14025ED60 returns g_PoolFrameBuffers[n] only for n = 1..7; 0 means the video page. So 7 buffers can be named, not 8.
- V (seen live 2026-11-20, random battle at Mandalia Plain with 11 enemy looks, HD on): a tracepoint on the buffer return (0x14025EDBC) hit every frame for buffers 2 and 3 (pools 9 and 10), so the classic path runs with HD on.
- V (seen live, same battle): pool 9's unit was identified on screen by pointing its HD sheet entry (g_HdSheetEntryBySlot slot 29) at pool 8's for a moment (that unit changed look); with buffers 2 and 3 filled with one colour index, that unit drew exactly as before: what the classic buffers hold does not reach the screen while HD is on.
- V (seen live, same battle): g_GraphicsLevel written from 2.0 to 1.0 in battle made every unit vanish (no classic sprite drawn in their place); written back to 2.0 they drew again. So a live switch is not a classic mode.
- I: so with HD on, pools past 15 need no classic buffer to be seen; what they need is that their upload (sub_14026E838, SceneUnit_LoadExtraPage) never writes past the 8 buffers and 8 blocks.
- V (code): sub_14026E838's 32 KB copy (0x14026E946) runs when g_GraphicsLevel is below 2.0 or the dword at xmmword_142E7FC80 + 8 is not 2; its pointer store g_PoolFrameBuffers[pool - 7] (0x14026E95E) runs always, so a pool 15 would store a pointer over dword_1411A37C8 (a count that sub_140259DC0 uses to index the array at xmmword_1411A37CC) and copy 32 KB to 0x1437EDF4C; its 4 KB copy goes to block pool & 7 (block 7 for pool 15, which pools 9..14 do not use).
- V (seen live 2026-11-21, Enhanced, HD sprites drawn): the dword at xmmword_142E7FC80 + 8 read 1, so the 32 KB copy runs in play.
- V (code): for a pool past 14, sub_140260CF0 gives the quad no buffer (0xFFFF: the video page) and SceneUnit_LoadExtraPage takes its video memory branch (x = 64 x (pool / 8 + 13), y = 32 x (pool % 8 + 8): x 896, y 480 for pool 15), so the classic path reads a place that holds no data of that pool.

## Open questions

? what the classic fetch is used for while HD is on (nothing visible found).
