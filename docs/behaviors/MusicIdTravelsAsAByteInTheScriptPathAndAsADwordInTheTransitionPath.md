# MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath

- **Kind:** observed behaviour
- **Scope:** engine (music requests)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [MusicSlot_FetchRecord](../functions/MusicSlot_FetchRecord.md), [EventMusic_LoadTrack](../functions/EventMusic_LoadTrack.md), [EventCmd_SetSlotRecord](../functions/EventCmd_SetSlotRecord.md), [EventCmd_ServiceRequests](../functions/EventCmd_ServiceRequests.md), [EventCmd_ActivateSlotParam](../functions/EventCmd_ActivateSlotParam.md), [EventCmd_ReleaseSlot](../functions/EventCmd_ReleaseSlot.md), [EventCmd_SetParamBlock](../functions/EventCmd_SetParamBlock.md), [sub_1402F2500](../functions/sub_1402F2500.md), [sub_14033FE00](../functions/sub_14033FE00.md), [sub_14034004C](../functions/sub_14034004C.md), [sub_1402BAB78](../functions/sub_1402BAB78.md), [sub_1401D9174](../functions/sub_1401D9174.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The music sound id (1-based; the file is `sound/music/music_%05u.sab` of id minus one) reaches the music player by four routes with different widths: a command byte, a 16-bit state word shared with the slot number, a 32-bit event variable and queue parameter, and a 32-bit field of a data table; the 101-row music slot table is read in two functions and its values are never used.

## Behavior

- V: the table at 0x14067FBB0 is read at six operands in two functions (MusicSlot_FetchRecord and a copy of its body inside a scene task); the index is 3 x a 64-bit sign extension of the id; the three dwords go to the request state and from there to a block at 0x140D3A8E4; nothing reads them (census of 39 operands of 0x140D3A8E0 to 0x140D3A91F).
- V: the track file is named from the id by a format string; the cache key is the id as a 32-bit hash; the stock packs hold music_00000 to music_00099 (ids 1 to 100); no id above 100 has a file.
- V: route 1, the class 32 command, passes byte 9 of its record; route 2, event variable 94 (a 32-bit cell), is passed whole but only while the word at +0x2C of the command context (0x14186246C) equals 1; route 3, the audio queue parameter, decodes the id as its low byte and the slot as bits 8 to 11; route 4, the BGMTransition and SoundEnhanced tables (nxd 306 and 280), passes the 32-bit field at row +16 of the SoundEnhanced row to slot 1.
- V: the 16-bit state word at 0x14186246A (a field at +0x2A of the 56-byte command context that the save keeps five times, not a standalone global) holds id | slot << 8; the only writers of its high byte store 2 (or zero), so the slot byte is 2 whenever the word is nonzero.
- V: the story event opcode 0x84 does not use this path: it plays file number operand plus 44 directly (operand a byte, I).

## Notes

An id of 256 or more written by route 1 or 2 would overwrite the slot byte; route 4 already carries ids above 255 into the table read.

## Open questions

? whether the sound engine opens a music file that is not in the stock pack index; ? which retail scripts write event variables 92 to 94 (none found by byte pattern).
