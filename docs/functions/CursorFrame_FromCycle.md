# CursorFrame_FromCycle

- **Address:** `0x1402E30A4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int CursorFrame_FromCycle(int which)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the animation frame of the screen cursor for the current tick.

## Behavior

- V: which = 0 takes the tick counter modulo the cycle length byte at 0x1408E5C78 (46) and walks the threshold list at 0x1408E5C7A; which = 1 walks the list at 0x1408E6492 without a modulo.
- V: the list is pairs (threshold, frame); the first pair whose threshold is above the tick gives the frame; a zero threshold ends the list (frame 0 is returned then).

## Notes

Read in full (small function).

## Open questions

?: the callers' use of the frame.
