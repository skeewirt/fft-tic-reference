# UIAddonFFTOConfig_Ctor

- **Address:** `0x14018853C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_Ctor(UIAddonFFTOConfig *addon)`
- **Callers:** UIAgentFFTOSystem_OpenConfig
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the General Options screen add-on (3416 bytes): sets its vtable and builds the gadgets.

## Behavior

- V: sets the vtable 0x14070DB30 and the gadgets at +1392 / +1568 (LB / RB icons), +1744 (row list), +2072 (value list), +2400 (confirm window) and +2848 (MainTab).
- V: the base `UIAddonMenuBase` part comes from `sub_1401D1970`.

## Referenced by

- Called by: [UIAgentFFTOSystem_OpenConfig](UIAgentFFTOSystem_OpenConfig.md)

## Notes

Struct: UIAddonFFTOConfig.

## Open questions

None recorded.
