# TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage

- **Kind:** observed behaviour
- **Scope:** engine (calendar counters, second tavern list)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [sub_1402CCEE0](../functions/sub_1402CCEE0.md), [sub_14039DA58](../functions/sub_14039DA58.md), [sub_140375AD0](../functions/sub_140375AD0.md), [sub_140375CD0](../functions/sub_140375CD0.md), [sub_140375E7C](../functions/sub_140375E7C.md), [sub_140376040](../functions/sub_140376040.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md), [sub_1402CF768](../functions/sub_1402CF768.md), [sub_14033FB84](../functions/sub_14033FB84.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Each of 64 tracked date slots owns one counter byte (cap 99) in a 64-byte block; the daily calendar tick and the jump by N days count a slot when its date is reached; the page of the second tavern list prints the counter of the selected position; the block is saved and copied in seven places.

## Behavior

- V: slot 0 compares event variables 95 and 96 with the current month and day, slots 1 to 63 compare the {month, day} byte pairs at 0x1407B8130; the daily tick adds 1 up to 99 on a match; the jump by N days adds the whole years passed and one for each date crossed, capped at 99.
- V: a census of the whole image finds 41 operands of the counter block in 12 functions: the tick, the jump, the page of the second tavern list (the only reader, two read sites), and seven functions that copy or reset the 64 bytes (save pack and unpack at +0x48C of the save work block, the errand state copy twice, the checkpoint writer and reader, the reset).
- V: the page reads counter[(selected entry) >> 4], where the entry is `level + 16 x position` built by sub_140375AD0 from the four-bit event variables 960 + position (positions 0 to 63 except 18, 21, 52 and 53); the entry is a bank 30 text reference; the page text is bank 17 message (low byte of the entry), where bank 17 is the loaded block `position / 16 + 6` of packed file 767 (a table of 114 sector offsets).
- V: the three loop bounds over the 64 slots are imm8 compares (cmp reg, 40h) at 0x1402CD10E, 0x14039DBCE and 0x140375B7B.
- V: for a slot whose pair is {0, 0} the jump function's day arithmetic gives -1 and increments the counter, so an unfilled slot would count.
- I: a scan of the functions that take the address of the live block and index into it found no other reader (the scan cannot see a base held in a struct field).

## Notes

The earlier statement that no reader exists was wrong: the cross-reference list misses operands that use an image base register with a 32-bit displacement.

## Open questions

? the name of the screen that shows the level list; ? the file that holds packed file 767's blocks.
