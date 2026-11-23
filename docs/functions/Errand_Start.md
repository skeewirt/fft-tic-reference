# Errand_Start

- **Address:** `0x14036A7D8`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Errand_Start(void)`
- **Callers:** `sub_14036A650`, `sub_14036CC50`
- **Callees:** EventVar_Read, EventVar_Write, `sub_1400DF354`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts an errand from the prepared board selection: pays the fee, creates the active record and marks the errand started.

## Behavior

- V: subtracts the fee global from gil (event variable 44) and refreshes the displayed gil.
- V: sets bit 8 (attempted) in event variable 863 + errand number.
- V: appends a 9-byte active record: flag 1, errand index, days elapsed 0, chosen days, town, unit count and the unit ids; the active count is incremented.
- V: each party unit's busy byte in its save record is set to 1.
- V: then sets bit 2 (started) in the errand's event variable and sends the start notification to the achievement system.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md)

## Referenced by

- Called by: [ErrandUnitPick_Input](ErrandUnitPick_Input.md), [Errand_StartConfirmInput](Errand_StartConfirmInput.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

Errand flags are event variables 864..959: 2 started, 4 succeeded, 8 attempted. The slot's errand byte is stored as number - 1.

## Open questions

None recorded.
