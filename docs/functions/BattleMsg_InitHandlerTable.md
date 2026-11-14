# BattleMsg_InitHandlerTable

- **Address:** `0x1400E28D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BattleMsg_InitHandlerTable(void *a1, ...)`
- **Callers:** not enumerated (no xref list was read for this address)
- **Callees:** the handler bodies it installs (BattleMsg_BannerHandlerA among them)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills an object's battle-message handler slots from the table based at a1+2528.

## Behavior

- V: fills handler slots from the table based at a1+2528.
- V: the slots at +2752, +2760, +2768, ... receive BattleMsg_BannerHandlerA, one of the banner handlers.
- I: the function is the battle-message handler-table initializer; the name and the battle scope rest on the slot filling and the banner handler it installs, not on a read of every slot.
- ?: the full slot list and the meaning of each handler were not read.

## State touched

- Calls: [BattleMsg_BannerHandlerA](BattleMsg_BannerHandlerA.md)

## Notes

The name is ours (IDB: sub_1400E28D0). The function is 4503 bytes; only the slot filling and the banner handler were read.

## Open questions

Who calls it and when; the full slot map from a1+2528; what the object at a1 is.
