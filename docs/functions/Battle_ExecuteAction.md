# Battle_ExecuteAction

- **Address:** `0x140206A0C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t Battle_ExecuteAction(void)`
- **Callers:** `sub_14020CFEC` (`0x14020D0B1`, action kickoff), `sub_140210AF0` (`0x1402129D4`, `0x140212A70`, battle state machine)
- **Callees:** `sub_14026079C`, `Battle_ResolveTargets` (`0x140206A55`), `sub_14020CABC`, `sub_140204FF0`, `BattleAct_SetupEffect` (`0x140206BDF`), `Battle_ApplyActionResults` (`0x140206BE6`), `ItemSprite_LoadPalettes`, `sub_140319D74`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Executes the acting unit's pending action: resolves it against every target, selects the visual effect,
and hands off to the result-apply loop or to the "no effect" branch.

## Behavior

- V: gets the acting scene object with `sub_14026079C`; the unit record is `[obj+0x148]`, its slot is
  `[record+0x1BC]`.
- V: calls `Battle_ResolveTargets(slot, obj+0x1A8)` at `0x140206A55`; the request is the unit's
  `+0x1A0`, and the summary is written at the acting scene object's `+0x1A8`.
- V: calls `BattleAct_SetupEffect` at `0x140206BDF` (effect number for the ability).
- V: when the action has no visual effect (effect id 0 or 512, or `sub_140319D74` says the ability has
  none), calls `Battle_ApplyActionResults` at `0x140206BE6` immediately; otherwise sets the battle
  state `dword_140C6B1CC = 43` at `0x140206BD3` (effect-then-apply state).
- V: writes the acting unit's animation/state fields and item palettes (`ItemSprite_LoadPalettes`).
- I: the effect is chosen before the apply loop so the hit/miss result can select the impact animation.

## State touched

- Calls: [Battle_ResolveTargets](Battle_ResolveTargets.md), [BattleAct_SetupEffect](BattleAct_SetupEffect.md), [Battle_ApplyActionResults](Battle_ApplyActionResults.md), [ItemSprite_LoadPalettes](ItemSprite_LoadPalettes.md)

## Referenced by

- Called by: [sub_140210AF0](sub_140210AF0.md)

## Notes

Called on the frame after the command state machine reaches state 47 (`sub_14020CFEC`). The result is
not applied here except through the `Battle_ApplyActionResults` tail.

## Open questions

- Exact condition for the early `return sub_140206758()` versus the data-load state 43.
