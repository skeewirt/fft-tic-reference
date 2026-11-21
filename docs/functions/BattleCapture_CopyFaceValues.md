# BattleCapture_CopyFaceValues

- **Address:** `0x140304BEC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void BattleCapture_CopyFaceValues(void *capture, int restore)`
- **Callers:** Battle_SaveCapture, Battle_RestoreCapture
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the 10 battle face values of the look pool and the globals after them to (mode 0) or from (mode 1) the battle capture.

## Behavior

- V: copies g_LookPoolFaceValue (10 dwords, capture +0), the globals from 0x1437A5A10 to 0x1437A5A73 (capture +136..+235) and 40 bytes at 0x1437A1348 (capture +336..+375); any other mode copies nothing.
- V: Battle_SaveCapture calls it last of the three per-scene copies (after SceneUnits_SaveRestore and the AI block copy), Battle_RestoreCapture likewise (0x1402CE4B8, 0x1402CEDA1).

## Referenced by

- Called by: [Battle_RestoreCapture](Battle_RestoreCapture.md), [Battle_SaveCapture](Battle_SaveCapture.md)
- Observed behaviours: [TheBattleCaptureCopiesFixedCounts](../behaviors/TheBattleCaptureCopiesFixedCounts.md)

## Open questions

None recorded.
