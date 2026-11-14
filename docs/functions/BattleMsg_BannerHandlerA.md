# BattleMsg_BannerHandlerA

- **Address:** `0x1400E8930`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BattleMsg_BannerHandlerA(...)`
- **Callers:** the handler table installed by BattleMsg_InitHandlerTable (I); the dispatcher that invokes it was not traced
- **Callees:** UIMessageBanner_Show

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Handler body that shows the centre banner after its agent's vfunc +16 returns true: it calls UIMessageBanner_Show with the battle banner object, the descriptor and the enable flag.

## Behavior

- V: calls UIMessageBanner_Show(banner, desc, enable) with the banner object at [[[qword_143CD9DA8+16]+72]+88].
- V: the call is made only after the agent's vfunc +16 returns true.
- V: the function is 89 bytes and is installed in the handler slots at +2752, +2760, +2768, ...
- I: the slots are part of the battle-message handler table that BattleMsg_InitHandlerTable fills.
- ?: what triggers the handler, and what the descriptor and enable values are when it runs.

## State touched

- Calls: [UIMessageBanner_Show](UIMessageBanner_Show.md)

## Referenced by

- Called by: [BattleMsg_InitHandlerTable](BattleMsg_InitHandlerTable.md)

## Notes

The name is ours (IDB: sub_1400E8930).

## Open questions

What triggers this handler; the descriptor and enable values it passes; how it differs from BattleMsg_BannerHandlerB.
