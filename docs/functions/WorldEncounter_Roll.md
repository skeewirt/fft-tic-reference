# WorldEncounter_Roll

- **Address:** `0x140248BE4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int WorldEncounter_Roll(int location, int arrivalRoad, bool fixedRoll)`
- **Callers:** sub_1402482F8, sub_1402D0EE0
- **Callees:** EventVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether a random battle starts at a battleground and which formation it uses.

## Behavior

- V: only locations 24..42 have rows; the row is the one of the three whose first byte is the road the party arrived on.
- V: the story variable named in the row picks the first of four tiers whose limit it does not exceed; a tier with chance 0 gives no battle.
- V: rolls 0..99 against the chance; a game option forces the roll to always or never pass.
- V: picks one of the formations allowed by the tier's bit mask at random and stores it, the battle number 0x200 + row byte 1 and row byte 22.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md)

## Referenced by

- Observed behaviours: [RandomEncounterRowByte22IsTheBattleMapId](../behaviors/RandomEncounterRowByte22IsTheBattleMapId.md)
- Reads tables: [RandomEncounters](../tables/RandomEncounters.md)

## Open questions

?: the meaning of row byte 22; which option value forces which way.
