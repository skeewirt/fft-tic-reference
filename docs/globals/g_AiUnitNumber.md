# g_AiUnitNumber

- **Kind:** global
- **Address:** `0x141873038`
- **Type:** `battle ai`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

byte[21], one per battle unit record: the AI's running number of the unit (0, 1, 2... over the records whose +0x01 is not 0xFF; 0xFF = not present), written by sub_1403166C0; the index of the AI's per-number tables (g_AiCommandTable, g_AiUnitTraits, g_AiLookAheadSave20, g_AiLookAheadSave8, g_AiLookAheadBuffer). The AI acts only while every number is below 16 (Ai_UnitTurnStep).

## Referenced by

- Observed behaviours: [TheAiHandlesSixteenUnitsOnTheField](../behaviors/TheAiHandlesSixteenUnitsOnTheField.md)

## Open questions

None recorded.
