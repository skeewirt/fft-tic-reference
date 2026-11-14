# GUILayer_BoundsAdd32

- **Address:** `0x1403E9560`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUILayer_BoundsAdd32(UIRenderer *r, int a, int b)`
- **Callers:** GUILayer_ExpandBounds
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Saturating signed 32-bit addition (a + b clamped to INT_MIN .. INT_MAX).

## Behavior

- V: a >= 0 and b >= 0: when 0x7FFFFFFF - a < b returns 0x7FFFFFFF else a + b. a < 0 and b < 0: when (int)(0x80000000 - b) > a returns 0x80000000 else a + b. Mixed signs: a + b.

## Referenced by

- Called by: [GUILayer_ExpandBounds](GUILayer_ExpandBounds.md)

## Notes

The name is ours (IDB: sub_1403E9560). 1044 hits per 4 s. The first argument (renderer) is unused. A simulator can use plain int addition unless coordinates reach about 2^31.

## Open questions

None recorded.
