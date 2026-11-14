# BattleForkDeterminism

- **Kind:** observed behaviour
- **Scope:** a battle resumed from one autosave and driven by the same scripted input in two runs
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SaveSlot_WriteFromLive](../functions/SaveSlot_WriteFromLive.md), [SaveSlot_LoadToLive](../functions/SaveSlot_LoadToLive.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [Time_GetTimestamp](../functions/Time_GetTimestamp.md), [BTurn_OnTurnStartStatus](../functions/BTurn_OnTurnStartStatus.md), [Battle_TurnEngine](../functions/Battle_TurnEngine.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle can be forked only at a save point: the autosave restores the world work copy and a battle image, but not the random stream, the frame counters, the input state or the thread/GPU state. The recipe forces the shared random state after the battle is up and then drives both runs with the same one-input-then-read-state script.

## Behavior

- V: `SaveSlot_WriteFromLive` packs the live state into `g_SaveWorkCurrent` (40164 bytes) and, when the situation byte is 1, queues a `resume_enma%02d_world.sav` entry; `SaveSlot_LoadToLive` loads that entry and flags a battle resume.
- V: the autosave PNG holds the resume entries, not a `fftsave.bin` slot image; the world entry embeds a work copy at +356.
- V: the random state is the four dwords at 0x1408E5FC8; `Rng_Percent` and many inlined copies step it with shifts 11 and 8.
- V: the state is written from a scaled `Time_GetTimestamp` value at 0x1401E72F9, inside the scene setup function `sub_1401E6E5C`.
- V: no save function references the state; the state is not in the 40164-byte work copy.
- I: therefore two cold loads of the same autosave start with different random streams; writing the same 16 bytes after the battle scene is up gives both runs the same stream for every draw that follows.
- I: the turn engine ticks CT once per `Battle_TurnEngine` call (phase 0), and that call happens per frame; a wall-clock input delay can therefore change the number of CT ticks between two otherwise identical presses.
- V: `Time_GetTimestamp` reads the clock provider at 0x143CD9BC8 and returns 1/300000-second units; `App_RunFrame` uses it for the 1/60-second frame limiter.
- I: the game samples input per frame, so the same input sequence does not guarantee the same frame alignment.
- V: event tasks run on their own OS threads (`EventThread_Yield`); the battle turn engine runs in the game thread.
- I: event scripts can interleave differently with the battle loop, but they do not own the battle random state.
- ?: whether the 1.07 MB main/attack/fturn images contain a copy of the random state, the camera record or the frame counters; the scene setup writes a fresh seed, so a stored copy would not be restored.
- ?: whether loading an autosave rewrites the autosave file; a byte copy of the PNG before branch A and a restore before branch B is the safe recipe.

## Open questions

? Which autosave descriptor is the battle save (the Load Game list order is the only offline clue); ? the lifetime of the seeded state when the battle scene is rebuilt; ? the effect of the UI frame generator on battle presentation traces.
