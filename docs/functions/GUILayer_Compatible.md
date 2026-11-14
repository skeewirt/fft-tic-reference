# GUILayer_Compatible

- **Address:** `0x1403E7ADC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUILayer_Compatible(UIRenderer *r, float *ctx, __int64 record)`
- **Callers:** GUILayer_Select
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests whether a draw context can share an existing layer: the blend type, colour transform, every effect group and their values must be equal (within 1.2e-7).

## Behavior

- V: compares blend type (+0) and, for types 14..16 or 17, their parameters, then each enabled group (+76 colour transform, +104, +112, +136, +156 glow, +178, +184) by flag and floats; any clip rectangle (+296), +384 or +409 flag makes the layers incompatible; +412 / +413 must match.

## Referenced by

- Called by: [GUILayer_Select](GUILayer_Select.md)

## Notes

Two components with the same glow settings can share one layer; different settings never do.

## Open questions

None recorded.
