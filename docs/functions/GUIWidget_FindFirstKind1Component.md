# GUIWidget_FindFirstKind1Component

- **Address:** `0x1403F9D6C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIWidget_FindFirstKind1Component(GUIWidget *w)`
- **Callers:** GUICore_DrawWidget, GUIWidget_HitTestPoint, GUIWidget_Tick, sub_1401389C4
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the first component of the widget whose type (comp+536) is 1 (index loop); sub_1403F9DA0 is the same search written with a pointer loop.

## Behavior

- V: n = (w+112 - w+104) / 8; for i in 0..n-1: when dword (comp_i + 536) = 1 returns comp_i; none returns 0.

## Notes

The name is ours (IDB: sub_1403F9D6C). 2575 hits per 4 s. Family with sub_1403F9DA0 (28 hits, 181 callers: the addon vfunc_4 methods find 'the' root component this way; same result, no index variable) and sub_1403F9D18.

## Open questions

? What type 1 is (I: the widget's root layer component).
