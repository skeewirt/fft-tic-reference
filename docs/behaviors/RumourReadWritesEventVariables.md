# RumourReadWritesEventVariables

- **Kind:** observed behaviour
- **Scope:** engine (tavern)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [TavernMenu_OnCommand](../functions/TavernMenu_OnCommand.md), [TavernRumourPage_Show](../functions/TavernRumourPage_Show.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Reading a rumour that has a counter raises the counter once and then writes the event variables listed in its row; the variable number 102 is a prefix, not a variable.

## Behavior

- V: only when counter and counter_value are both non-zero and the counter is below counter_value: UserSituation_SetValue(counter, counter_value).
- V: then for each pair (event_vars[i], event_var_values[i]) up to the count at +0x18: a variable 102 sets base = 10 * value; any other variable gets EventVar_Write(variable + base, value) and the base is reset to 0.
- V: stock data writes event variables 166 = 1 (key 20) and 170 = 1 (key 21).
- V: the rumour's picture is shown when counter and counter_value are both non-zero, and is marked while the counter is still below counter_value.

## Open questions

None recorded.
