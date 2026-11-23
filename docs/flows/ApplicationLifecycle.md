# ApplicationLifecycle

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The order from process entry to the first scene. The main thread runs the application loop and the Win32 message pump while the boot state machine starts the task threads. The game task thread resets and enters the outer loop, which clears and scans the save images, runs a scene, and either starts the title/opening path or takes the alternate transition loop. The message pump is the only normal exit; the game loop never returns.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0 process entry"></a>0 process entry | [WinMain](../functions/WinMain.md) | V | The CRT calls WinMain. It reads argc and argv, builds the system and game listener blocks, and calls Game_Main with the system block. |
| <a id="1 application start"></a>1 application start | [Game_Main](../functions/Game_Main.md) | V | The debugger gate, data directory, window/application creation and then the loop `while (App_RunFrame(...) && App_ProcessMessages(...))`. |
| <a id="2 main-thread frame"></a>2 main-thread frame | [App_RunFrame](../functions/App_RunFrame.md) | V | Frame pacing and the update chain. The application frame chain drives the boot state machine; its state 2 calls the thread factory, which creates 17 task threads and installs Game_ThreadMain in task slot 0. |
| <a id="3 message pump"></a>3 message pump | [App_ProcessMessages](../functions/App_ProcessMessages.md) | V | Drains up to ten Win32 messages per call. WM_QUIT ends the application loop, after which Game_Main tears the application down and WinMain returns to the CRT. |
| <a id="4 game thread entry"></a>4 game thread entry | [Game_ThreadMain](../functions/Game_ThreadMain.md) | V | Runs on the game task thread: first-use 4 MB arena setup, 512x272 display state, the effect base reset, then the pre-loop reset and the outer loop. |
| <a id="5 pre-loop reset"></a>5 pre-loop reset | [Game_MainLoopReset](../functions/Game_MainLoopReset.md) | V | The 15-byte wrapper calls Game_LoopReset, the reset body, and then Game_MainLoop. |
| <a id="5a reset body"></a>5a reset body | [Game_LoopReset](../functions/Game_LoopReset.md) | V | Sets the 374x240 screen mode, clears the fade, battle and event state and the event counters, resets the scene/UI helpers and seeds the constant block. |
| <a id="6 outer loop"></a>6 outer loop | [Game_MainLoop](../functions/Game_MainLoop.md) | V | Clears both save images, scans the save data, resets the scene task set, runs SceneLoop_Run and converts the returned code into the next step. It re-enters the scene phase after every transition and never returns. |
| <a id="7 normal scene"></a>7 normal scene | [SceneLoop_Run](../functions/SceneLoop_Run.md) | V | Caller of Scene_Init. Runs one scene task per frame while scene flag bit 0 is set, then returns the hand-over code in dword_141876F94. |
| <a id="8 scene start"></a>8 scene start | [Scene_Init](../functions/Scene_Init.md) | V | Resets the scene flags, page buffer and task stack. A non-zero mode calls TitleScene_Start; mode 0 clears the page index and calls OpeningScene_Start. |
| <a id="9 title or opening"></a>9 title or opening | [Scene_Init](../functions/Scene_Init.md) | V | Mode 0 pushes opening task 0; task 0 starts the title scene when no movie is requested, and otherwise returns without changing the stack. A non-zero mode pushes the title task directly. The title task's exit writes the hand-over code that Game_MainLoop reads next. |
| <a id="10 alternate loop"></a>10 alternate loop | [SceneLoop_RunAlt](../functions/SceneLoop_RunAlt.md) | V | Used when `dword_140D3A848` is 3 (not SceneLoop_Run's return code 3). It resets the scene inline, reads 0x8800 bytes of data kind 877 from sector 101, pushes task 9 (which moves to task 10, the fade/movie task) and runs the same per-frame dispatch without a hand-over code. |

## Behavior

- V: the message pump and the game loop are separate threads: WinMain, Game_Main, App_RunFrame and App_ProcessMessages run on the process's first thread, while the thread factory creates the 17 task threads with `beginthreadex` and stores Game_ThreadMain in task slot 0.
- I: the boot state machine runs on the main thread before the game thread exists (rests on the factory creating the game thread during boot state 2 and on Game_Main's loop being the only frame loop at that point).
- I: the slot-0 task thread is the one that reaches Game_MainLoop (rests on the task loop `sub_1402F3698` calling the entry stored in the slot).
- V: the outer loop clears both save images before the first scan and again before the second scan; a completed scan enters the scene phase, and an error becomes a message panel that, once it closes, enters the scene phase.
- V: the scene tasks write 0, 1, 2 or 3 into dword_141876F94; Game_MainLoop branches on those values (0 sets `byte_1407829FA` to 1 and clears `g_BattleModeFlag`, 2 clears event variable 85, 3 sets `xmmword_142FF9E14` to 1 and arms the countdown dword, 1 only clears `byte_1407829FA`).
- I: the two title-menu starts (new game versus continue) are the likely owners of codes 0 and 1 (rests on the branch bodies and the title task's writes); the exact mapping is not decoded.
- V: the alternate loop runs only when the battle/scene result dword_140D3A848 is 3; the other handled result codes skip it.
- V: no path returns from Game_MainLoop. The process is ended from the message thread when WM_QUIT makes App_ProcessMessages return 0.
- ?: the menu-level meaning of the four hand-over codes and the timing of the countdown state in the outer loop.

## Notes

Earlier versions of this reference documented a fragment of Game_MainLoop (the entry fill and part of the save-scan state machine) as a separate function, Save_BootClear. The save/load menu is the `sub_140245C84` + `off_1408F9570` state machine inside Game_MainLoop; SceneLoop_RunAlt is the battle-result transition loop, not the save/load screen. The boot hand-over is described in text here so this flow does not depend on the boot flow record.

## Open questions

? the menu-level meaning of hand-over codes 0 and 1; ? the gameplay meaning of result codes 2, 5, 6, 7, 8 and 10; ? missing global records for dword_141876F94, dword_141876EE8, dword_142FF9EFC and dword_140D3A848.
