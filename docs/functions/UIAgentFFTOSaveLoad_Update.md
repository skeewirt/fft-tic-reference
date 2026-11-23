# UIAgentFFTOSaveLoad_Update

- **Address:** `0x140182EDC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall UIAgentFFTOSaveLoad_Update(UIAgentFFTOSaveLoad *agent, float dt)`
- **Callers:** none found as a direct call (installed at vtable slot 1)
- **Callees:** sub_14013EB34, sub_140182F68

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The agent's per-frame virtual (vtable slot 1): it advances the saving overlay, drains queued save errors, and delivers phase 1 to the current agent state handler unless a save-error prompt is up.

## Behavior

- V: when the saving-overlay pointer at +1584 is non-null, calls `sub_14013EB34(overlay, dt)`. That helper accumulates dt at overlay +64, shows the widget on a +69 request and marks +68 ready, and hides it after a +70 request once the accumulated time reaches 1.0 s.
- V: calls `sub_140182F68(agent)`, which pops one 24-byte message from the queue at +152/+160 under the +184 critical section and opens a pause-style error prompt through `sub_1401835E8`: prompt 6 for a formatted system message, prompt 7 for a game message.
- V: reads the pause manager's depth byte at +23 and the current pause id at +20+depth; when that id is 9 the function returns without delivering phase 1.
- V: otherwise calls the block-A handler at agent +80 with (owner at agent +72, phase 1, the qword stored at `g_Application` + 1160). The owner is the agent itself.
- V: it does not advance the dialog block at +104; only state 2's handler calls the dialog handler at +112.
- I: the pause-id 9 gate freezes the state machine while a save-error prompt is up, resting on `UIAddon_PauseSetup` pushing id 9 only when its fifth argument is non-zero and on the error pump passing 1 there.
- ?: what the three virtual tests on the pause/dialog agent gate inside `sub_140182F68`; ? what pause id 9's duration row does to the prompt.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Notes

Whole function read (84 bytes). Phase 1 reaches the handler through +80, not +112; the dialog block is ticked by the state-2 handler. The pause gate reads the top pause id, not a global pause flag. The overlay tick is the only place the show/hide requests are consumed. `UIAgent_SetState` covers the phase-0/phase-2 protocol.

## Open questions

? what the three virtual tests gate in the error pump; ? what pause id 9's duration row does; ? whether any frame delivers phase 1 to the dialog block directly.
