# EffectSequence_HoldTwoFrames

- **Address:** `0x140314A40`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_HoldTwoFrames(void)`
- **Callers:** EffectSequence_Run (slot 5 of the effect sequence handler table (0x140682F30))
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 5 handler: a placeholder entry that only counts its state up and ends on the third frame.

## Behavior

- V: state 1 sets the state (+8) to 2 and returns 1; state 2 sets it to 3 and returns 1; every other state returns 0.
- V: it reads and writes nothing else.
- I: its use is as a short timer entry: the flight handler (EffectSequence_ProjectileFlight) queues one as kind 5.

## Notes

Name is ours.

## Open questions

None recorded.
