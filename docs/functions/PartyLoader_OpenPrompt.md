# PartyLoader_OpenPrompt

- **Address:** `0x14034637C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t PartyLoader_OpenPrompt(void)`
- **Callers:** ClassicMenu_HubStep (state mask 0x1000000, set from the party loader request)
- **Callees:** Input_ActionBit, ClassicMenu_OpenNumberEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the party loader of the old world menu: a number entry 0..999 with caption text 47142, and the kind 52 screen that applies it.

## Behavior

- V: stores the confirm and cancel action bits in dword 0x140D498D0 and sets dword 0x140D49ABC = 3.
- V: clears the value word 0x140D498D4 and calls ClassicMenu_OpenNumberEntry(_, 0x03E70000 = range 0..999, 47142, position (-60 or -40 by language, -22)).
- V: pushes kind 52 on the classic screen stack (depth 0x140D8DBA0, kind array 0x140D4C948) with record dword 0 = 0; its step is MenuCtl_Entry52.

## State touched

- Calls: [ClassicMenu_OpenNumberEntry](ClassicMenu_OpenNumberEntry.md)

## Open questions

None recorded.
