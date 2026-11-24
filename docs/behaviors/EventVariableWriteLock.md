# EventVariableWriteLock

- **Kind:** observed behaviour
- **Scope:** event variables
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventVar_Alu](../functions/EventVar_Alu.md), [EventVar_Write](../functions/EventVar_Write.md), [EventViewer_StartReplay](../functions/EventViewer_StartReplay.md), [EventVariables](../registries/EventVariables.md), [EventVariableRanges](../registries/EventVariableRanges.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The rule that decides whether a store into the event variable space is kept. While variable 508 is non-zero the event viewer's replays cannot change the story: only a fixed set of ids is stored. Ids of 960 and above have a second rule that holds whatever the lock says.

## Behavior

- V: while variable 508 is non-zero, EventVar_Alu stores only into ids 0..43, 48, 50..57, 83, 86..90, 102, 112..143 and 508..511; every other store is dropped.
- V: the whole lock check is skipped while the reentrancy guard byte at 0x142FEC547 is set.
- V: ids of 960 and above are stored only while their current value is below 12, whatever the lock says; a value of 12 or more freezes the person entry.
- V: the replay of an event from the event viewer sets 508 to 1 together with the event number, so the replayed script cannot change story flags.
- I: the lock exists to protect the story state during a replay or a preview.
- ?: variable 88 is in the exempt set, but no reader or writer of it was found.

## Notes

Our names. Tags: V from the store function and its callers, I for the purpose. The accessor sheet is EventVar_Alu.

## Open questions

None recorded.
