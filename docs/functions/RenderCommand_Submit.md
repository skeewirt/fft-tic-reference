# RenderCommand_Submit

- **Address:** `0x140069980`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `_QWORD *__fastcall RenderCommand_Submit(RenderContext *rc, void *cmd)`
- **Callers:** 116 call sites (every site that allocates a command with RenderCommand_Allocate)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a finished command to the context's list as a {sort key, command pointer} pair; the list is later executed in key order (the sort itself was not read here).

## Behavior

- V: the pair is written at the list write pointer rc+40: the first qword is the context's current sort key (rc+8) at this moment, the second the command pointer; the pointer then advances by 16 and the remaining-entries counter rc+56 is decremented.
- V: when the counter reaches zero a new 1 KB group is taken from the device pool (g_RenderDevice + 5120 + 5108 - (the dword at +5152 + 1024)); the pool counter at +5144 is advanced by 0xC00 and +5152 by 0x400, and a failure sets g_RenderDevice + 5106 and returns null; the previous group's last link is set to the new group, the group count rc+60 is incremented and the counter is reloaded with 63.
- V: the sort key stored is therefore the value the caller put in rc+8 before this call, not the one it sets afterwards; the layer passes set rc+8 before packing each command (GUILayer_Composite, GUILayer_BlurShadowPass, GUILayer_BlitFinal's caller).

## Referenced by

- Called by: [GUILayer_BlitFinal](GUILayer_BlitFinal.md), [GUILayer_Composite](GUILayer_Composite.md)

## Notes

The name is ours (IDB: sub_140069980). These render-context lists are not the lists UIContext_SortCommands sorts (those hold the UI draw records of UIRender_AppendCommand); the sort and execution of the {key, command} lists belong to the render device's frame submission, which was not read here.

## Open questions

None recorded.
