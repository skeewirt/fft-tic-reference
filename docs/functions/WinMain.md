# WinMain

- **Address:** `0x140010E70`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)`
- **Callers:** __scrt_common_main_seh (0x14041FF69)
- **Callees:** sub_1405CE110, sub_1405CE118, Game_Main

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The process entry the C runtime calls: it takes the Win32 startup arguments, fills in the system and game listener objects, and hands them to `Game_Main`. Its return value becomes the process exit code.

## Behavior

- V: called by the C runtime startup helper `__scrt_common_main_seh` (0x14041FF69).
- V: reads the process argument count and the narrow argv pointer that `_configure_narrow_argv` stored (`sub_1405CE110` returns the count, `sub_1405CE118` the pointer) and passes them as Game_Main's first two arguments.
- V: builds a `faith::System::Framework::SystemApplicationListener` block on the stack: its vtable, hInstance, hPrevInstance, lpCmdLine, nShowCmd and a 32-bit 135 word; the block also stores a pointer to the game listener block and a trailing zero.
- V: builds a `ffto::Game::GameApplicationListener` block with its vtable, the same four startup arguments and the same 135 word.
- V: passes the system listener block as Game_Main's third argument (`winMainParams`) and returns Game_Main's result unchanged.
- ?: what consumes the 135 word in either block, and where the listener vtables are registered.

## State touched

- Calls: [Game_Main](Game_Main.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md)

## Notes

Whole function read (215 bytes). The listener blocks are built inline; their constructors are not called here. The two argument helpers are the CRT accessors for the configured narrow argv.

## Open questions

The meaning of the 135 word at +0x24 of both blocks and which code reads the system listener's game-listener pointer.
