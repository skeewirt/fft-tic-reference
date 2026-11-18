# ClassicUi_OpIfElse

- **Address:** `0x1403900D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpIfElse(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 2: as opcode 1 with an else branch.

## Behavior

- V: bytes +4 and +5 are the counts of the then and the else records that follow in that order; only the branch matching the condition (function +3, argument +6 or the list row) is run, the other is skipped.

## Open questions

None recorded.
