# GUIComponent_ResetEffects

- **Address:** `0x140408B40`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponent_ResetEffects(GUIComponent *comp)`
- **Callers:** GUIComponent_Ctor path, sub_140408C4C
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets a component to defaults: clears the effect enable bytes and frees its child list.

## Behavior

- V: zeroes blend (+16), the enable bytes +60, +88, +96, +120, +172, +186, +192, +216, +244, +265 and word +268; sets +20 to 1.0f (opacity), +520 = 1920 and +524 = 1080 (design size).

## Open questions

None recorded.
