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
- V (EventVar_Write and EventVar_Alu, read): the write is not raw: a negative value keeps only its low byte, variable 44 is capped at 99,999,999, an id of 1024 or more traps, a destination of 960 or more is stored only while its value is below 12, and while variable 508 is nonzero only 0..43, 112..143, 508..511 and a fixed set within 48..102 change.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md)

## Open questions

None recorded.
