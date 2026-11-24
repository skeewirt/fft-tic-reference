# WorldMapAgent_CreateAddons

- **Address:** `0x1401570C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapAgent_CreateAddons(int64_t *agent)`
- **Callers:** ClassicMenu_RunScreenStack
- **Callees:** Mem_Alloc, sub_140159020, UIAgent_AttachAddon, UIAddon_LoadByRow, WorldMapBaseList_Construct, sub_140158C38, UIListGadget_Ctor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the five addons of the world map agent (UI agent 20) and loads each from its UI addon row.

## Behavior

- V: +64 the main map (3,504 bytes, row 139), +72 the frame menu (3,952 bytes, row 140), +80 the Locations list (1,856 bytes, WorldMapBaseList_Construct, row 133), +88 the location info (88 bytes, row 134), +96 the deep dungeon menu (632 bytes, row 136).
- V: each is attached to the agent (UIAgent_AttachAddon), loaded (UIAddon_LoadByRow) and appended to the agent's addon vector (+104..+128).
- I: the addons live as long as the agent; the Locations list is shown and hidden, not rebuilt (WorldMapAgent_SetState).

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [UIAgent_AttachAddon](UIAgent_AttachAddon.md), [UIAddon_LoadByRow](UIAddon_LoadByRow.md), [WorldMapBaseList_Construct](WorldMapBaseList_Construct.md), [UIListGadget_Ctor](UIListGadget_Ctor.md)

## Open questions

None recorded.
