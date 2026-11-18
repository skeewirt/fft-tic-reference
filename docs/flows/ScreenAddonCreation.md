# ScreenAddonCreation

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a screen (add-on) is made and shown: allocate, construct, attach to the agent, load its layout from the screen table, then show or hide it.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Mem_Alloc](../functions/Mem_Alloc.md) | V | `Mem_Alloc(size, heap qword_143CDAA80+8)` allocates the add-on, then its class constructor runs. |
| <a id="2"></a>2 | [UIAgent_AttachAddon](../functions/UIAgent_AttachAddon.md) | V | Sets add-on +16 = agent, joins the agent's list at agent +8 and gives the add-on a unique id at +32 (counter at `qword_143CD9DA8`+128, map at +48). |
| <a id="3"></a>3 | [UIAddon_LoadByRow](../functions/UIAddon_LoadByRow.md) | V | Looks up the row of UI table 24 (`uiaddon.nxd`); its `UiFilePath` is loaded by `sub_1401D1A3C`. |
| <a id="4"></a>4 | [sub_1401D1E30](../functions/sub_1401D1E30.md) | I | Shows the add-on (`sub_1401D1E30(addon, 0)`). |
| <a id="5"></a>5 | [sub_1401D1EAC](../functions/sub_1401D1EAC.md) | I | Hides the add-on (`sub_1401D1EAC(addon, 1)`); 0x1401C3CE0 hides the title menu and shows the play mode add-on this way. |

## Behavior

- V: read in UIAddonFFTOTitle_Create and UITitle_ShowMenu; EventEndSlate_ShowTask follows the same sequence.
- V: a confirm dialog is opened with `UIAddon_PauseSetup(*(root agent)+128, 3, 0, {callback, context, callback2}, 0, 0)`; Continue's save language check in 0x1401C2D60 passes 0x1401CCB40 and 0x1401C3494.

## Open questions

None recorded.
