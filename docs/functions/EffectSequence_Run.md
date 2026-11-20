# EffectSequence_Run

- **Address:** `0x14031A3DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_Run(void)`
- **Callers:** the battle frame loop
- **Callees:** Effect_RunStateMachine, the sequence kind handlers

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per frame driver of the effect sequence entries: runs the handler of every active entry and retires finished ones.

## Behavior

- V: runs the effect state machine first, then walks the linked list of active sequence entries (96 bytes each, at most 17 per frame).
- V: the handler comes from the effect sequence handler table (0x140682F30) by the kind byte at +3 of the entry (kinds above 22 end the walk); a non-zero result keeps the entry.
- V: a zero result retires the entry: frees an attached object, unlinks it from the active list and appends it to the free list.
- V: it also sets the stepping flags (1 or 2) from the frame counter against a frame skip count, and returns whether any entry or the state machine still runs.

## State touched

- Calls: [Effect_RunStateMachine](Effect_RunStateMachine.md)

## Notes

Name is ours.

## Open questions

?: what frame skip counts 0, 1 and 2 correspond to in play.
