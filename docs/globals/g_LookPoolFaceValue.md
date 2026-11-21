# g_LookPoolFaceValue

- **Kind:** global
- **Address:** `0x1437A59E0`
- **Area:** [Graphics](../areas/graphics.md)
- **Type:** `int32[10]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle face value per look pool record 0..9: sub_14026E838 stores the scene unit's sprite byte; cleared to -1 by sub_140210AF0, saved and restored by sub_140304BEC; ten readers use it as a face number behind the 0xCD cap (turn panels, unit status, deployment icons, dialogue face slots).

## Referenced by

- Described by tables: [LookPoolFaceValue](../tables/LookPoolFaceValue.md)
- Observed behaviours: [BattleFaceIsThePoolSpriteByte](../behaviors/BattleFaceIsThePoolSpriteByte.md), [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md), [LooksPastTenShowThePoolNumbersFace](../behaviors/LooksPastTenShowThePoolNumbersFace.md), [OnlyTenDistinctLooksDrawCorrectly](../behaviors/OnlyTenDistinctLooksDrawCorrectly.md)
- Read by: [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md), [sub_1401F3858](../functions/sub_1401F3858.md), [sub_140214134](../functions/sub_140214134.md), [sub_140221798](../functions/sub_140221798.md), [sub_1402DF374](../functions/sub_1402DF374.md), [sub_140338A28](../functions/sub_140338A28.md), [sub_1403980AC](../functions/sub_1403980AC.md)
- Written by: [sub_140210AF0](../functions/sub_140210AF0.md), [sub_14026E838](../functions/sub_14026E838.md)

## Open questions

None recorded.
