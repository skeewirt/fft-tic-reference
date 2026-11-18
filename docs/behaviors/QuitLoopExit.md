# QuitLoopExit

- **Kind:** observed behaviour
- **Scope:** how the quit request ends the main loop
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [Game_Main](../functions/Game_Main.md), [App_RunFrame](../functions/App_RunFrame.md), [g_Application](../globals/g_Application.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Game_Main runs App_RunFrame in a loop and leaves it when it returns 0; App_RunFrame returns whether the quit request byte is 0.

## Behavior

- V: Game_Main (0x14002BD50) tests App_RunFrame's result right after the call (0x14002BE57) and leaves the loop on 0; App_RunFrame returns whether byte +0x5F0 of the application object is 0 (the compare at 0x14002A872). So the quit request `g_Application` +0x5F0 = 1 ends the loop after the current frame.

## Open questions

None recorded.
