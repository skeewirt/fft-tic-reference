# UI_FrameUpdate

- **Address:** `0x1400E3B20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UI_FrameUpdate(UIModule *ui, float dt)`
- **Callers:** sub_1400B3770, sub_1400B57FC, sub_140246078, TitleScene_Start
- **Callees:** UIAgentCursor_Show, UIAddonFingerCursor_FreezePose, GUICore_BeginFrame, GUICursor_UpdateIndex, sub_1401D1148, sub_1403D6098

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of the UI: sets the UI frame time, runs a pending cursor restart, updates the agents (the hand's glide) and hands the frame time to the GUI core.

## Behavior

- V: when ui+13488 != 0: ui+13480 = dt * g_UIDataModule+28 (the UI time scale), ui+13484 = a second time value computed from sub_1401E8AC4 (not traced).
- V: g_UIDataModule+28 is 1.0 in the table the module is created with.
- I: it never changes (no other writer was found).
- V: after housekeeping loops (not read) sub_1401D1148(addon manager qword_143CD9DA8) runs the addon load / show / hide bookkeeping.
- V: agent = element 1 of the manager's agent vector (UIAgentCursor). When agent+128 == 2: UIAgentCursor_Show(agent) (which now takes the PlayLoop branch) and, when agent+132 != 0, UIAddonFingerCursor_FreezePose(agent+64). Then agent+128 = 0.
- V: virtual +8 of every agent is called (for the cursor agent: GUICursorHand_Update through a thunk that first requires an active cursor widget); then agent+128 = 1.
- V: sub_1403D6098(g_GUICore), then GUICore_BeginFrame(g_GUICore, ui+13480, ui+13484) stores the frame times the widgets read.
- V (disassembly): sub_1400B3770 and sub_1400B57FC compute dt as (float)((double)ticks * scale / 300000.0) from an object whose +8 holds the tick count and +32 a double scale; sub_140246078 passes a float it computed earlier (not read); the title scene start passes 0.
- I: that object is the application's frame timer (app+1160 in App_RunFrame): App_RunFrame forms the identical expression from the same two fields.

## State touched

- Calls: [UIAgentCursor_Show](UIAgentCursor_Show.md), [UIAddonFingerCursor_FreezePose](UIAddonFingerCursor_FreezePose.md), [GUICore_BeginFrame](GUICore_BeginFrame.md), [GUICursor_UpdateIndex](GUICursor_UpdateIndex.md)
- Reads: [UIAgentCursor.show_state](../structs/UIAgentCursor.md#show_state), [UIAgentCursor.static_mode](../structs/UIAgentCursor.md#static_mode)
- Writes: [UIAgentCursor.show_state](../structs/UIAgentCursor.md#show_state)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md), [UIAgentLifecycle](../flows/UIAgentLifecycle.md)
- Called by: [TitleScene_Start](TitleScene_Start.md)
- Observed behaviours: [UIStateClock](../behaviors/UIStateClock.md)

## Notes

The name is ours (IDB: sub_1400E3B20). The database calls the first argument g_CharaRenderMgr at the call sites; its +13480 .. +13489 fields are the UI frame state, so the name is probably wrong (I).

## Open questions

? The frame timer's maximum step (timer+16) that clamps dt; the second time value at ui+13484.
