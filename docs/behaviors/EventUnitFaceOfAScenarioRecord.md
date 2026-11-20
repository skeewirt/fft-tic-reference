# EventUnitFaceOfAScenarioRecord

- **Kind:** observed behaviour
- **Scope:** engine (turn panel portrait)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A scenario setup record can name one event unit and a portrait code: the turn panel shows that unit's small face with the code instead of the face of its look.

## Behavior

- V: ScenarioSetup_ApplyRecord stores record byte +13 at 0x140C6AD7A (face code) and byte +14 at 0x140C6AD76 (event unit number); the mid-event refresh copies them again from the linked record.
- V: the turn panel small-face code (sub_14022AA88) gives a unit whose +401 equals the unit number the face code and fixed rectangle values; the portrait cache builder (sub_140300768, 55 entries) takes the code of entry 54 from the face byte.
- M: stock: 76 rows use it, 11 codes (91..95, 113, 151, 154..156), unit numbers 75, 128..134, 137 and 240.

## Open questions

None recorded.
