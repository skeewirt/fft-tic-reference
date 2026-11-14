# g_ScreenFade

- **Kind:** global
- **Address:** `0x142FF9E08`
- **Area:** [Event system](../areas/event-system.md)
- **Type:** `uint64`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The fade and skip state: the low dword is the fade alpha, the high dword the skip state (0 none, 1 requested, 2 skipping).

## Behavior

- V: EventScript_SkipTick is the only writer of the value 1 in the high dword (C6).

## Referenced by

- Written by: [EventScript_SkipTick](../functions/EventScript_SkipTick.md)

## Open questions

None recorded.
