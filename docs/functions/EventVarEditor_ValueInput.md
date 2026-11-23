# EventVarEditor_ValueInput

- **Address:** `0x14036E064`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char EventVarEditor_ValueInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 48)
- **Callees:** EventVar_Write, EventVarEditor_DrawPage

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the number entry above the event variable list (table index 48): confirm writes the entered value to the variable.

## Behavior

- V: confirm calls EventVar_Write(variable, word_140D498D4), where the variable is record dword 1; cancel writes nothing.
- I: the word 0x140D498D4 is the number held by the number-entry widget.
- V: after the close it pops and, when a value was written, redraws the list page of the screen below.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md)

## Open questions

None recorded.
