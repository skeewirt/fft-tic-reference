# Game_MainLoopReset

- **Address:** `0x1402D4A2C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __fastcall __noreturn Game_MainLoopReset(__int64 unused)`
- **Callers:** Game_ThreadMain (0x14034867E)
- **Callees:** Game_LoopReset, Game_MainLoop

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The 15-byte pre-loop wrapper: it calls the reset helper `sub_140283FCC` and then enters `Game_MainLoop`. The reset body is paged separately as `Game_LoopReset`.

## Behavior

- V: calls `Game_LoopReset` (IDB `sub_140283FCC`), the reset helper; it returns normally.
- V: calls `Game_MainLoop`; that loop never returns, so this wrapper never returns.
- I: the wrapper exists only to sequence the reset and the loop; `Game_ThreadMain` is its only caller.

## State touched

- Calls: [Game_LoopReset](Game_LoopReset.md), [Game_MainLoop](Game_MainLoop.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md)
- Called by: [Game_ThreadMain](Game_ThreadMain.md)

## Notes

Whole wrapper read (15 bytes). The reset is `sub_140283FCC` (201 bytes), paged as `Game_LoopReset`; this wrapper does not perform the reset itself.

## Open questions

Whether the reset helper has any caller other than this wrapper (none found).
