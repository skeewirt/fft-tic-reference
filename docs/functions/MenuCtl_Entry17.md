# MenuCtl_Entry17

- **Address:** `0x14036FFE8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MenuCtl_Entry17(int64_t record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 17)
- **Callees:** sub_140370D58

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Table index 17: a jump to sub_140370D58, a step with a state in record dword 4.

## Behavior

- V: a single jump instruction.
- V: sub_140370D58 reads record dword 4 as a state: 0 reads a result code from the widget (23 starts the next state) and plays cues 0x4C and 0x4D when a countdown in dword 10 ends; 1 waits for two global counters (0x140D49558, 0x140D49550) to be 0 and sets state 2; 2 waits for the same counters and a widget flag, then pops and calls sub_14036F874.
- I: it follows the errand report (kind 16) in the screen order; the callee touches no errand global, so the errand link rests on that order only.

## Notes

Only the transitions of sub_140370D58 were read; the cues and the counters named here are in that callee.

## Open questions

None recorded.
