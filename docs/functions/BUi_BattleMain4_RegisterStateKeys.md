# BUi_BattleMain4_RegisterStateKeys

- **Address:** `0x14010E1FC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BUi_BattleMain4_RegisterStateKeys(void *window)`
- **Callers:** the battle main window constructor
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Registers the battle main window's state-name keys.

## Behavior

- V: sets the window's state-name keys, among them +57528 = 'Hide', +57544 = 'HideAT', +58248 = 'Show' and +58264 = 'ShowAT'.

## Open questions

? the other keys it registers.
