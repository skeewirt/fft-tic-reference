# Unit_SetChargeStateBits

- **Address:** `0x140279370`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Unit_SetChargeStateBits(UnitWorkRecord *unit, char state)`
- **Callers:** sub_14020A7F0 (2), sub_14020AD64 (2), sub_140271C50, BattleAction_ApplyRequest, sub_140281488 (2), sub_1402828E4, Battle_AITurnRun
- **Callees:** AbilityAction_GetRecord, sub_1401FB064

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets which of the four action states Readying, Jumping, Evading, Performing (statuses 4..7) a unit is in, and the charge counter that goes with it.

## Behavior

- V: state -1 is replaced by 8 when Performing (status 7, +0x61 byte 0 bit 0x01) is effective, else 0.
- V: state 5 / 6 / 7 / 8 selects the bit 0x08 / 0x04 / 0x02 / 0x01 (status 4 Readying, 5 Jumping, 6 Evading, 7 Performing); state 8 also sets +0x1BD and the charge counter +0x18D from byte +12 & 0x7F of the action record of the word at +0x1A2 (AbilityAction_GetRecord); state 0 sets the charge counter to 0xFF.
- V: byte 0 of the applied set +0x1EF keeps its high nibble, its low nibble becomes the selected bit only; byte 0 of the effective set +0x61 becomes byte 0 of +0x57 OR that byte.
- V: for the statuses 4..7 whose effective bit changed it calls sub_1401FB064(id + 1, 0 or 1, slot) (off when it was set before), unless g_BattleSimulating is set.

## State touched

- Calls: [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [sub_1401FB064](sub_1401FB064.md)
- Reads: [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.innate_status_a](../structs/UnitWorkRecord.md#innate_status_a)
- Writes: [UnitWorkRecord.applied_status](../structs/UnitWorkRecord.md#applied_status), [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.charge_counter](../structs/UnitWorkRecord.md#charge_counter)

## Referenced by

- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md)

## Notes

Name is ours. Whole function read. It rewrites byte 0 of +0x61.

## Open questions

? what +0x1BD holds besides the charge time copy.
