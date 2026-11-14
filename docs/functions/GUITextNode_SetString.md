# GUITextNode_SetString

- **Address:** `0x1403F0F8C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUITextNode_SetString(GUITextNode *t, const char *s)`
- **Callers:** JobTreePanel_SetTextKey, sub_1403F106C/sub_1403F109C/sub_1403F1004 (the formatting variants) and about 60 addon functions
- **Callees:** sub_140025C74 (std::string assign)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a text node's string; marks the layout dirty only when it differs. Always stamps the change time.

## Behavior

- V: when s != 0: the node's std::string at t+208 (inline buffer t+216, capacity t+240 >= 16 means heap pointer) is compared byte-wise with s; if different the string is assigned (sub_140025C74, strlen computed first) and byte t+316 (text dirty) = 1.
- V: always t+296 = dword g_GUICore+2096 (the GUI tick counter, the same value GUILayer text scrolling uses).

## State touched

- Reads: [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Called by: [GUITextNode_SetTextExpanded](GUITextNode_SetTextExpanded.md), [GUITextNode_SetTextFormat](GUITextNode_SetTextFormat.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [sub_14013D844](sub_14013D844.md), [sub_1401560D0](sub_1401560D0.md)

## Notes

The name is ours (IDB: sub_1403F0F8C). 1595 hits per 4 s. Family: sub_1403F106C (SetTextById) -> sub_1403F109C (SetTextExpanded) -> sub_1403F0B10 (format expander) -> SetString; sub_1403F1004 (printf form) -> SetString. Text layout reruns only when +316 is set, so calling this with unchanged text costs no re-layout.

## Open questions

? What +296 is read for (I: text start time for reveal / scroll effects).
