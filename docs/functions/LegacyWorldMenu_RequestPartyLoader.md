# LegacyWorldMenu_RequestPartyLoader

- **Address:** `0x1402B3CB8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t LegacyWorldMenu_RequestPartyLoader(void)`
- **Callers:** the task entry of node 17 of the old world menu node table (LegacyWorldMenuNodes)
- **Callees:** EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of node 17 (row 9 of the old main world menu): sets the party loader request word and ends.

## Behavior

- V: sets word 0x143749F3C = 1, clears and copies the input words and ends with EventTask_Terminate.
- V (read in LegacyWorldMenu_FrameStep and ClassicMenu_HubStep): LegacyWorldMenu_FrameStep turns the word into mask 0x1000000 of the state dword; ClassicMenu_HubStep then calls PartyLoader_OpenPrompt (number entry 0..999), and MenuCtl_Entry52 rebuilds the party from that battle entry.

## State touched

- Calls: [EventTask_Terminate](EventTask_Terminate.md)

## Open questions

None recorded.
