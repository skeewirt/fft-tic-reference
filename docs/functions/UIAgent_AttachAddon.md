# UIAgent_AttachAddon

- **Address:** `0x1401D16C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIAgent_AttachAddon(UIAgent *agent, UIAddon *addon)`
- **Callers:** every screen creator (the title add-ons, EventEndSlate_ShowTask, UIAddonFFTOEvent_Ctor and others)
- **Callees:** sub_140031D7C (vector grow), the std ordered-map node insert (_Insert_node), __security_check_cookie

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Links a screen (add-on) to its agent and gives it an id.

## Behavior

- V: add-on +16 = agent; the add-on joins the agent's add-on vector at agent +0x10 (begin +0x10, end +0x18, capacity +0x20). The field at agent +8 is the vector's allocator, not a list head.
- V: it gets a unique id at +32 from the counter at `qword_143CD9DA8`+128 (set to 1 when it is -1), kept in the map at `qword_143CD9DA8`+48.

## State touched

- Reads: [UIAgentBase.addons_end](../structs/UIAgentBase.md#addons_end), [UIAgentBase.addons_capacity](../structs/UIAgentBase.md#addons_capacity)
- Writes: [UIAgentBase.addons_end](../structs/UIAgentBase.md#addons_end)

## Referenced by

- Appears in flows: [ScreenAddonCreation](../flows/ScreenAddonCreation.md), [UIAgentLifecycle](../flows/UIAgentLifecycle.md)
- Called by: [Boot_Update](Boot_Update.md), [TitleScene_Update](TitleScene_Update.md), [UIAgentFFTOSystem_OpenConfig](UIAgentFFTOSystem_OpenConfig.md)

## Notes

Flow: ScreenAddonCreation.

## Open questions

None recorded.
