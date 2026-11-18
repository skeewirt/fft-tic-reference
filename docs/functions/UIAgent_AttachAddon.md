# UIAgent_AttachAddon

- **Address:** `0x1401D16C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgent_AttachAddon(UIAgent *agent, UIAddon *addon)`
- **Callers:** every screen creator (the title add-ons, EventEndSlate_ShowTask, UIAddonFFTOEvent_Ctor and others)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Links a screen (add-on) to its agent and gives it an id.

## Behavior

- V: add-on +16 = agent; the add-on joins the agent's list at agent +8.
- V: it gets a unique id at +32 from the counter at `qword_143CD9DA8`+128 (set to 1 when it is -1), kept in the map at `qword_143CD9DA8`+48.

## Referenced by

- Appears in flows: [ScreenAddonCreation](../flows/ScreenAddonCreation.md)
- Called by: [UIAgentFFTOSystem_OpenConfig](UIAgentFFTOSystem_OpenConfig.md)

## Notes

Flow: ScreenAddonCreation.

## Open questions

None recorded.
