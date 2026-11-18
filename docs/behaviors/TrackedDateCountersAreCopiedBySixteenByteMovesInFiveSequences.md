# TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences

- **Kind:** observed behaviour
- **Scope:** engine (calendar counters)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md), [sub_1402CF768](../functions/sub_1402CF768.md), [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [sub_14033FB84](../functions/sub_14033FB84.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Outside the two counting loops, the 64 counter bytes are moved only by sequences of four 16-byte moves: the save pack and unpack, the checkpoint writer and reader, the battle capture's errand-state copy in both directions, and the new-game reset; all use aligned moves on the live block.

## Behavior

- V: each sequence has four 16-byte moves of the live counters (movaps, so the live address is 16-byte aligned) interleaved with moves of other state; the checkpoint buffer holds its copy at 0x142E808DC and the battle capture buffer (0x1408B8588) at +0x2D4.
- V: SaveWork_CopyErrandState has one body for both directions (its second argument 0 = live to capture, nonzero = capture to live); Battle_SaveCapture calls it with 0 and Battle_RestoreCapture with the restore flag; the capture buffer is one fixed global, so a restore reads whatever the buffer holds, including a buffer filled from a saved file.
- V: the new-game reset (sub_14033FB84) writes the 64 bytes from a constant block of starting values at 0x1407BAC30 (not zero: it begins 16, 16, 15, 15, 28, 37, 37, 56) with four aligned stores; seen live: after the reset ran, all 64 counters equalled that block.
- V: seen live, the reset runs when the game returns to the title (the counters read the starting values at the title); starting a New Game from the title does not run it again before the first battle.
- V: the save pack stores the 64 bytes at +0x48C of the save copy (followed by the errand count at +0x4CC); the unpack reads them back.

## Open questions

? whether the checkpoint buffer is ever filled by a path other than the writer.
