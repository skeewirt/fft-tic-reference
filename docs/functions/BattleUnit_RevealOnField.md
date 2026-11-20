# BattleUnit_RevealOnField

- **Address:** `0x1402718CC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleUnit_RevealOnField(int record)`
- **Callers:** ScenePreview_ShowEntry, ScenePreview_ClaimForUnit
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Puts a battle unit record that is off the field onto it, without building anything: the record must already exist.

## Behavior

- V: when the record's slot byte (+1) is 0xFF: returns -1 if its on-field byte (+0x1B5) is not 0 (a dropped entry, 0xFF); otherwise sets +1 = the record index and +0x1B5 = 1 and, when the record's +5 has bits 0x30, adds its level (+0x29) to word_14114B0B4 and raises byte_140D405A2 to it when larger (a level sum and a level maximum). When +1 is not 0xFF it does nothing. Returns 0.
- V: its two callers are ScenePreview_ShowEntry (for a parked entry: also queues its look, so a scene unit is built for it) and ScenePreview_ClaimForUnit (for a unit already drawn but not placed). Both are reached from the event interpreter (opcodes 0x44 and 0x45 among others), EventUnitBlock_RunTask, EventSubScript_RunTask, Battle_TurnStep and sub_140269DC4.
- V: no code path found adds a battle record after load and deployment: the writers of the on-field byte are Battle_PlaceEntryUnits, Battle_BuildRosterTeam, Battle_AddJoinedUnit, Battle_RebuildUnitTable, the deployment steps, this function and one event-interpreter case that takes a unit off (slot byte 0xFF).

## Referenced by

- Called by: [ScenePreview_ClaimForUnit](ScenePreview_ClaimForUnit.md), [ScenePreview_ShowEntry](ScenePreview_ShowEntry.md)
- Observed behaviours: [BattleUnitsAreFixedAtLoadAndRevealedLater](../behaviors/BattleUnitsAreFixedAtLoadAndRevealedLater.md)

## Notes

So every unit a battle can show is one of its entry records (built at load) or a deployed party unit; event scripts reveal and hide them. Behavior: BattleUnitsAreFixedAtLoadAndRevealedLater. Cross-check notes: 0x29 and 0x30 are the `[..+29h]` read and the `test 30h` on +5; 0x44 and 0x45 are opcode numbers of the callers' paths, not constants of this body.

## Open questions

None recorded.
