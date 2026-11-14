# g_SkipRequestSource

- **Kind:** global
- **Address:** `0x142FF9EF4`
- **Area:** [Event system](../areas/event-system.md)
- **Type:** `uint64`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The skip-request source: its high dword is copied into the fade/skip state by the event runner. It is part of how a held skip action becomes a skip state.

## Behavior

- V: EventScript_Run copies its high dword into g_ScreenFade's skip state.

## Referenced by

- Read by: [EventScript_SkipTick](../functions/EventScript_SkipTick.md), [sub_1402059AC](../functions/sub_1402059AC.md)

## Open questions

None recorded.
