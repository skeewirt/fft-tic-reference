# GUIComponent_Ctor

- **Address:** `0x1404087A4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIComponent_Ctor(GUIComponent *c, int kind)`
- **Callers:** GUIComponentCustom_Create
- **Callees:** sub_1403EF3B4 (GUINode ctor), sub_1403EF6B4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Base constructor for UISystem GUIComponent (vtable 0x1407225F8); layer node embedded at +272, kind at +536.

## Behavior

- V: sets many default floats (0.5/1.0), name pointers to Str1, size 1920x1080 at +520/+524.

## Referenced by

- Called by: [GUIComponentCustom_Create](GUIComponentCustom_Create.md)

## Open questions

None recorded.
