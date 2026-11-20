# EntryRowMarksEventSkipOnce

- **Kind:** observed behaviour
- **Scope:** engine (event skip)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventScript_Run](../functions/EventScript_Run.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An entry override row can mark its battle's events as skippable only once: the interpreter checks bytes +0x93, +0x94 and +0x95 of the battle's first row along with the EventId skip-once byte.

## Behavior

- V: EventScript_Run first tests byte +36 (skip_once) of the EventId row; when that is 0 it reads the OverrideEntryData row for g_BattleEntrySource and tests bytes +0x93, +0x94 and +0x95 (the guest-join, withdrawal and betrayal flags).
- I: a non-zero byte there sets g_EventSkipOnce to 1, the same effect as the EventId byte: the event may be skipped only once (the notes of the reading give the value 2 after the first skip).

## Open questions

? the exact value flow of g_EventSkipOnce after a skip.
