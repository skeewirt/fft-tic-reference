# Boot_CloseUI

- **Address:** `0x1401DE0C4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall Boot_CloseUI(void)`
- **Callers:** Boot_SetState (0x1401E79FE), UIAddonFFTOConfig_OnClose (0x140188FEB), sub_1401DD9E0 (0x1401DDA03)
- **Callees:** UIAgent_DetachAddon, UITitleCushion_Close, UIAgentFFTOLauncher_Close, sub_1401BC1FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Removes the boot UI when the boot launcher is left: the startup add-on, the title cushion, the launcher and the second system agent's add-on.

## Behavior

- V: takes the UI service object at `qword_143CD9DA8+16` and detaches the add-on at its +24 agent (+64), which `Boot_Update` fills with `UIAddonFFTOStartup`.
- V: calls `UITitleCushion_Close` on the +32 agent.
- V: calls `UIAgentFFTOLauncher_Close` on the +40 agent.
- V: detaches the add-on at the +400 agent (+64).
- V: when the launcher agent's add-on is non-null, calls `sub_1401BC1FC(...,1)` to show the UI state.
- V: `Boot_SetState` calls it as the exit action of state 4; `UIAddonFFTOConfig_OnClose` calls it before restarting the boot sequence; `sub_1401DD9E0` calls it when that object is released.
- I: the four slots match the add-ons `Boot_Update` attaches: startup (+24), cushion (+32), launcher (+40) and the +400 add-on created on the load route; this is their teardown counterpart (rests on the same agent offsets).

## State touched

- Calls: [UIAgent_DetachAddon](UIAgent_DetachAddon.md)

## Referenced by

- Called by: [Boot_SetState](Boot_SetState.md)

## Notes

Whole body read; the agent offsets are the same ones `Boot_Update` uses to attach the add-ons.

## Open questions

What `sub_1401BC1FC(...,1)` changes when the launcher add-on is already detached, and whether the +400 add-on is the load screen.
