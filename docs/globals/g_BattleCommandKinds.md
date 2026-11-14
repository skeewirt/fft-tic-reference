# g_BattleCommandKinds

- **Kind:** global
- **Address:** `0x14184A9A8`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[8]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The command kind of each entry of the byte list just built: g_CommandKind[command byte] & 0x0F.

## Behavior

- V: sub_14030E010 writes it (0x14030E105 in the loop, 0x14030E13F for a monster set) for the list it built, whichever of the two arrays that was; the byte array beside it, byte_14184A9A0, gets 1 per entry where sub_14030E174 answered 0 (the meaning of the flag was not read) and is read by sub_1402B2EB0, sub_1402B2FA4, sub_1402B32D4, sub_1402DEAF8 and sub_1402EC31C.

## Referenced by

- Observed behaviours: [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md)
- Written by: [sub_14030E010](../functions/sub_14030E010.md)

## Notes

Source: IDA reads of 2026-11-12.

## Open questions

? the readers of this array (two code references, both in sub_14030E010).
