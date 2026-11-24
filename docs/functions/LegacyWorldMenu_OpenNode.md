# LegacyWorldMenu_OpenNode

- **Address:** `0x1402B4DCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyWorldMenu_OpenNode(int node)`
- **Callers:** LegacyWorldMenu_StepRosterRequest, LegacyWorldMenu_StepRow4Request, WorldMap_OpenLocationsList
- **Callees:** sub_14025FCDC, EventTask_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens a node of the old world menu as the root task: picks the node table of the text language and starts the node's task in event task slot 8.

## Behavior

- V: returns at once when slot 8's busy qword (the event task table's slot 8 block, qword 18) is set.
- V: stores the node number in word 0x143749F24 (the node the menu returns to after a request finishes, I: the request sequences reopen that word).
- V: text language 0 selects tbl_LegacyWorldMenuStateLang0 (0x14080CAB0), 3 selects Lang3 (0x14080D930), 2 selects Lang2 (0x14080E070), any other value or no language info selects Lang1 (0x14080D1F0); the choice goes to the active node table pointer qword 0x14184B230.
- V: for node 4 with a language other than 0 it first calls sub_14025FCDC with a fixed rectangle (I: a window placement fix for the wider texts).
- V: writes the record's word pair at +8 / +10 to -48 / -56 and, when the width word +12 or the height word +14 is above 176, moves +8 or +10 so the window ends at 120 or 112.
- V: node 6 also stores its record pointer at g_CharaRenderMgr +7488.
- V: starts the node's task (record +48) in slot 8 with EventTask_Start and clears the slot block's second and third qwords; the first qword gets a register value (I: the record pointer, as in LegacyMenu_ConfirmRow).

## State touched

- Calls: [EventTask_Start](EventTask_Start.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Referenced by

- Called by: [LegacyWorldMenu_StepRosterRequest](LegacyWorldMenu_StepRosterRequest.md), [LegacyWorldMenu_StepRow4Request](LegacyWorldMenu_StepRow4Request.md), [WorldMap_OpenLocationsList](WorldMap_OpenLocationsList.md)
- Resolves registries: [LegacyWorldMenuNodes](../registries/LegacyWorldMenuNodes.md)

## Open questions

None recorded.
