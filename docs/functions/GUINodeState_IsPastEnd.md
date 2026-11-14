# GUINodeState_IsPastEnd

- **Address:** `0x140400118`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUINodeState_IsPastEnd(NodeState *s)`
- **Callers:** GUINode_UpdateStates, sub_14028F8A4, sub_140293560
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rule used by GUINode_UpdateStates to decide whether a running state is to be advanced: false when restarted, true when held, otherwise frame >= end frame.

## Behavior

- V: byte s+106 (dirty / restarted) != 0 -> false. Byte s+110 (hold) != 0 -> true.
- V: end = (s+92 >= s+96) ? (float)(int s+88) (frame count) : (float)(int s+96) (loop end); result = (float s+80 (current frame)) >= end.

## Notes

The name is ours (IDB: sub_140400118; earlier sheets call it the 'accept rule'). 338 hits per 4 s. The comparison is single-precision float >= on an int converted to float. Caution: the polarity (true = frame reached the end) conflicts with GUINode_UpdateStates' wording 'accepts it ... Advance'; see open question.

## Open questions

? Whether UpdateStates advances on true or on false (re-read the branch polarity in GUINode_UpdateStates before building the simulator's state loop).
