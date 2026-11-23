# Input_RepeatDirection

- **Address:** `0x1402CC9F0`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `__int64 __fastcall Input_RepeatDirection(unsigned int enabledMask)`
- **Callers:** Errand_ConfirmDialogInput, MenuCtl_Entry43, Errand_StartConfirmInput, EventVarEditor_ListInput, StatusGlossary_Input and others
- **Callees:** Input_ActionBit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Menu auto-repeat for six directional actions: returns an action bit on a fresh press and again at the repeat rate while it stays held.

## Behavior

- V: it collects the bits of actions 0x21, 0x22, 0x24, 0x23, 0x2D and 0x2E through `Input_ActionBit`, keeping only those whose enable bit in the argument is set (0x1000, 0x4000, 0x2000, 0x8000, 8 and 4 in that order).
- V: when any enabled action is in `dword_140D4CC18` it zeroes the first four repeat counters (`qword_140D49AD4` and `qword_140D49ADC`; the pair at `qword_140D49AE4` is not zeroed) and returns that intersection at once.
- V: otherwise for each enabled action that is also in `dword_140D4CC1C`, it adds 1 to the action's counter; above the delay `dword_140D49AC8` it subtracts an interval (`dword_140D49ACC`; `dword_140D49AD0` for the last two) and returns that action's bit; a released action resets its counter.
- I: `dword_140D4CC18` is the set of actions pressed this frame and `dword_140D4CC1C` the held set (rests on the code's use and on `Input_TestAction` taking the first as an argument).
- V: returns 0 when no repeat fires.

## Referenced by

- Called by: [Errand_ConfirmDialogInput](Errand_ConfirmDialogInput.md), [PagedText_Step](PagedText_Step.md), [UiPage_ChoicePromptInput](UiPage_ChoicePromptInput.md)

## Notes

Mask argument read from the disassembly (the decompile lost it): the 0x1000 test is a bit-12 test there.

## Open questions

What the six actions are called.
