# GUICore_TickWidget

- **Address:** `0x1403D7670`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUICore_TickWidget(GUICore *core, GUIWidget *w)`
- **Callers:** GUICore_UpdateWidgets, sub_1403D79C4
- **Callees:** GUIWidget_Tick

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives one widget its frame time and calls its tick (vtable slot 7, GUIWidget_Tick).

## Behavior

- V: nothing happens unless the widget is active (w+74) or pending (w+75).
- V: block = (~(word w+88)) AND core+2132 (the low 16 bits). When block != 0 the widget is still ticked, with dt = 0 (its clocks stand still). Otherwise dt = core+2100 when w+48 == 0, dt = core+2104 when w+48 == 1, and for any other value of w+48 the widget is not ticked at all.
- V: for a widget made by an addon, w+48 and the bits of w+88 come from the addon's row of the addon table (UITable 24): w+48 = byte 31 != 0, bit i of w+88 = byte 12 + i != 0 for i = 0..11 (sub_1401D1C6C).

## State touched

- Calls: [GUIWidget_Tick](GUIWidget_Tick.md)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Observed behaviours: [UIStateClock](../behaviors/UIStateClock.md)

## Notes

The name is ours (IDB: sub_1403D7670). A set bit in core+2132 that the widget's own mask lacks freezes the widget (for instance behind a modal screen).

## Open questions

? The table row of the finger cursor: whether its widget uses selector 0 or 1 and which block bits it is exempt from (it bobs while the Job Tree is open, so it is exempt from whatever the Job Tree sets).
