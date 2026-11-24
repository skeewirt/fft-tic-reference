# WorldMap_OpenLocationsList

- **Address:** `0x14036D21C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int WorldMap_OpenLocationsList(void)`
- **Callers:** WorldMap_ScreenInput, MenuCtl_Entry43, MenuCtl_Entry28
- **Callees:** LegacyWorldMenu_OpenNode, WorldMapAgent_IsMapShown, sub_1400EDCB4, sub_14036E5DC, EventVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the world map's Locations list: starts the old location node (or the old main menu node when a roster request waits), has the world map agent show the list, and pushes the hub controller.

## Behavior

- V: clears dword 0x140D498D0 to -1.
- V: with a roster request code in g_CharaRenderMgr +13448 or dword 0x142FF9F1C set it opens node 4 (LegacyWorldMenu_OpenNode(4)); otherwise node 6 (LegacyMenu_BuildLocationList) and, when the world map is shown (WorldMapAgent_IsMapShown), calls sub_1400EDCB4(3) and sub_14036E5DC (which builds the records).
- V: stores gil (event variable 44) in dword 0x140D40A98, writes the new stack level's record dword 0 = 3, clears mask 0x4000000 of the state dword (bit-clear of bit 26) and with mask 0x8 set sets 0x8000000 (bit 27), pushes kind 1 (ClassicMenu_HubStep) and sets mask 0x1 of dword 0x1437FC2C0.
- I: sub_1400EDCB4(3) moves the world map agent to state 3, the Locations list (WorldMapAgentStates).

## State touched

- Calls: [LegacyWorldMenu_OpenNode](LegacyWorldMenu_OpenNode.md), [WorldMapAgent_IsMapShown](WorldMapAgent_IsMapShown.md), [sub_14036E5DC](sub_14036E5DC.md), [EventVar_Read](EventVar_Read.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Open questions

None recorded.
