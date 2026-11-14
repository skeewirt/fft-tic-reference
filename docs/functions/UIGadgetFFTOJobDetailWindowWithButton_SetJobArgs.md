# UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs

- **Address:** `0x1402A7C38`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `__int64 UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs(UIGadgetFFTOJobDetailWindowWithButton *w, JobDetailRec *rec)`
- **Callers:** vtable only: vftable_ffto::Game::UI::UIGadgetFFTOJobDetailWindowWithButton_140716F20 slot 8
- **Callees:** FormatArgs_Push, sub_14028F754, sub_1402AB174 (scroll refit)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 8 of the 'with button' job detail window (called from UIGadgetFFTOJobDetailWindow_SetJob through virtual +64): resets the text argument list at w+1168, pushes the job id and a flag, refreshes the text and refits the scroll area.

## Behavior

- V: clears the argument vector at w+1168 (end = begin: *(w+1184) = *(w+1176)).
- V: pushes two 264-byte argument records through FormatArgs_Push (vector push_back): record 1 has dword +0 = rec+72 (job id) and a type dword (+256) = 1; record 2 has dword +0 = (rec+100 & 0x40) != 0 and type 1.
- V: sub_14028F754(w+1104, 1) re-applies the text binding at w+1104 (the text binding layout of UIGadgetFFTOJobDetailWindow_SetJob: node +16, id at +96 etc.); then sub_1402AB174(w+760, *(w+1096)) refits the scroll text gadget at w+760 to the viewport height stored at w+1096.

## State touched

- Calls: [FormatArgs_Push](FormatArgs_Push.md)

## Notes

Name proposed (IDB: sub_1402A7C38). The two arguments feed a '{0}' / '{1}' text template of the button window (a description of the job with a flag; rec+100 bit 0x40 is the flag). I: it is the job's help text region of the window.

## Open questions

? what text id the binding at w+1104 holds and what rec+100 bit 0x40 means (a unit / Job flag copied from addon+19032).
