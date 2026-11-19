# BgmMode_SwitchTab

- **Address:** `0x1401C8308`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BgmMode_SwitchTab(void *screen)`
- **Callers:** UIAddonFFTOBGMMode_vfunc_12
- **Callees:** Input_IsActionMapped, sub_1400F0D98, sub_14040B128, sub_14040AEE8, sub_14028BDE4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the music player between its two lists on the tab input actions.

## Behavior

- V: input actions 43 and 44 move the current list index (screen +824) between 0 and 1 (tab nodes +128 and +136).

## Notes

Name is ours.

## Open questions

None recorded.
