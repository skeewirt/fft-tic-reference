# g_BattleContextGate

- **Kind:** global
- **Address:** `0x14186AF80`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle context gate: while it is non-zero the reaction and secondary-action paths refuse to run, which is how those actions avoid refunding or repeating.

## Behavior

- V: set to 2 around reaction and secondary actions (Inventory_ReturnItem); both branches of sub_14030AFEC test it before and after their calls.
- V: IDA names the same dword g_BattleSimulating: non-zero while a forecast (the preview, the AI's look-ahead) runs a formula. The formula blocks read it: Battle_Rand15 returns 0x4000, Formula_ChanceRoll (unless the chance is 0), Formula_EvadeByteRoll and Formula_BardDancerGate skip their rolls, Formula_StatusChance19 returns false at the value 2 and Formula_56_StatusOnlyApplication drops every listed status at 2.
- V: BTurn_PreviewAction and Battle_ExecuteSecondaryAction write it; sub_140281488, BattlePreview_BuildAction and the reaction builders read it.

## Referenced by

- Read by: [Inventory_ReturnItem](../functions/Inventory_ReturnItem.md), [sub_14030AFEC](../functions/sub_14030AFEC.md)

## Notes

The same address carries two names: g_BattleContextGate here and g_BattleSimulating in the IDA database. The values are 0 (a real action), 1 and 2 (forecast levels, 2 set around reaction and secondary actions).

## Open questions

None recorded.
