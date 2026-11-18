# UIAddon_CanTakeInput

- **Address:** `0x1401D21D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int UIAddon_CanTakeInput(UIAddon *addon)`
- **Callers:** UIAddon_OnEventBase
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 3: true unless the add-on is showing (+42) or hiding (+43).

## Behavior

- V: `!+42 && !+43`. `UIAddon_Hide` (0x1401D1EAC, a different function that sets +43) sets +43 while it hides; New Game hides the title menu this way while the play mode screen takes input.

## Referenced by

- Called by: [UIAddon_OnEventBase](UIAddon_OnEventBase.md)
- Observed behaviours: [UIAddonBaseEventRouting](../behaviors/UIAddonBaseEventRouting.md)

## Open questions

None recorded.
