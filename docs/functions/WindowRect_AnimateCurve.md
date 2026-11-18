# WindowRect_AnimateCurve

- **Address:** `0x1402DDFE8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int WindowRect_AnimateCurve(unsigned short *rect, short *primA, short *primB, int curve)`
- **Callers:** not recorded
- **Callees:** EventTask_WaitFrame, sub_140226880

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens or closes a window by moving two rectangles along one of the five animation step lists.

## Behavior

- V: takes the rectangle (x, y and extents from the window record) and, when the second primitive is used, a second rectangle.
- V: steps through the list chosen from the five-pointer table at 0x1406818C8 (values grow towards 4096, the list ends with 4096); each step waits (3 minus the speed setting) frames and calls the rectangle updater sub_140226880 for the first and, if used, the second primitive.
- V: curve 4 also writes a grey level from (4096 minus the step) / 32 into the primitive colour bytes.
- V: after the last step it waits one frame and draws the final rectangle.

## State touched

- Calls: [EventTask_WaitFrame](EventTask_WaitFrame.md)

## Referenced by

- Reads tables: [WindowCurvePointers](../tables/WindowCurvePointers.md)

## Notes

Read in full.

## Open questions

?: the meaning of the five curves.
