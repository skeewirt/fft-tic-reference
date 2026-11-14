# BattleMsg_BannerHandlerB

- **Address:** `0x1400E8A84`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BattleMsg_BannerHandlerB(...)`
- **Callers:** the handler table installed by BattleMsg_InitHandlerTable (I); the dispatcher that invokes it was not traced
- **Callees:** UIMessageBanner_Show

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Second handler body on the banner path: like BattleMsg_BannerHandlerA it calls UIMessageBanner_Show with the battle banner object, the descriptor and the enable flag after its agent's vfunc +16 test.

## Behavior

- V: calls UIMessageBanner_Show(banner, desc, enable) with the banner object at [[[qword_143CD9DA8+16]+72]+88].
- V: the call is made only after the agent's vfunc +16 returns true.
- V: the function is 89 bytes, the same size as BattleMsg_BannerHandlerA.
- I: the two bodies are separate entries of the battle-message handler table that BattleMsg_InitHandlerTable fills.
- ?: how the two bodies differ; the difference was not read.

## State touched

- Calls: [UIMessageBanner_Show](UIMessageBanner_Show.md)

## Notes

The name is ours (IDB: sub_1400E8A84).

## Open questions

What triggers this handler; the descriptor and enable values it passes; how it differs from BattleMsg_BannerHandlerA.
