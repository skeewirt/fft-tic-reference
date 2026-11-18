# g_BattleMapWords

- **Kind:** global
- **Address:** `0x140D3F950`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint16[]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The runtime per-EVENT word table (887 words): one word per story event number, built by ScenarioSetup_ApplyRecord from the scenario setup records at every scene start; the battle message, skip and event code read it by scene variable 39. The battle capture keeps all 887 words.

## Behavior

- V: readers index it as g_BattleMapWords[SceneVar(39)] with no bound; the builder writes words[event number of the record] (not the row number).
- V: word = record byte +18 + (byte +19 << 10), OR byte +20 << 8; bits 0..7 and 10..11 = a 10-bit link to another record by event number, bits 8, 9, 12..15 = flags (tested with 0F300h, bit 15 also as the sign).
- V: after the records the builder sets words 401 = 0, 402 = 8000h, 403 = 0, and words 400 and 404 = 8000h when scene variable 510 is set, else 8200h; the battle message dispatch picks events 400..402 as its index.

## Referenced by

- Read by: [sub_14020261C](../functions/sub_14020261C.md), [sub_140204B78](../functions/sub_140204B78.md)

## Open questions

None recorded.
