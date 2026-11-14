# UIDrawState_Copy

- **Address:** `0x1403C46A4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIDrawState_Copy(UIDrawState *dst, UIDrawState *src)`
- **Callers:** UICommand_Append, UICommand_ExecuteBatches
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the 48-byte draw state with the masks the command format keeps.

## Behavior

- V: dst[0] = src[0] & 0x7FFFFFFF; dst[1] = src[1] & 0x7FFFFFFF; +8 masked 0xFFFFFFFEFFFFE000; +16 texture; +24 flags (all bits); +28/+32/+36 floats; +40 qword.

## Referenced by

- Called by: [GUIRenderer_ResetFrame](GUIRenderer_ResetFrame.md), [UICommand_Append](UICommand_Append.md), [UICommand_ExecuteBatches](UICommand_ExecuteBatches.md)

## Open questions

None recorded.
