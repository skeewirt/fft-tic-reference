# Tavern_RumorTextWait

- **Address:** `0x14036F398`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t Tavern_RumorTextWait(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 8)
- **Callees:** PagedText_Step, TavernRumours_BuildList

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the rumor text screen (table index 8): runs the paged text widget, then returns to the rumor list.

## Behavior

- V: runs PagedText_Step on the widget block at 0x140D49580 until it returns 0.
- V: then plays cue 2, pops, toggles (xor) mask 0x10 of two window entries of 0x140D4C4B0 (stride 9 dwords) named by record dwords 2 and 3, and of one window record of 0x140D4B9B0 (stride 14 dwords) named by dword 4, which then also gets mask 0x100; it calls TavernRumours_BuildList.

## State touched

- Calls: [PagedText_Step](PagedText_Step.md), [TavernRumours_BuildList](TavernRumours_BuildList.md)

## Open questions

None recorded.
