# g_BattleCasterUnit

- **Kind:** global
- **Address:** `0x14186AF78`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8 *`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the unit record of the one who does the action, as the formula handlers read it: the entry of g_PreviewUnitTable chosen by byte 0 of the request. IDA names it qword_14186AF78; g_BattleActingUnit next to it is the unit hit.

## Behavior

- V: Battle_ResolveAction stores it (0x140309A0F) as g_PreviewUnitTable + 512 * (byte 0 of the 20-byte request copy).
- V: read by about 40 formula helpers for the caster's stats (+0x3E PA, +0x3F MA, +0x40 Speed, +0x2B Brave, +0x29 level), passive bits (+0x99, +0x9A, +0x9B), statuses (+0x63, +0x65), zodiac (+8) and element mask (+0x7A).

## Referenced by

- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)
- Written by: [Battle_ResolveAction](../functions/Battle_ResolveAction.md)

## Notes

The name is proposed; the IDA label is qword_14186AF78.

## Open questions

None recorded.
