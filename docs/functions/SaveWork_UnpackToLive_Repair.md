# SaveWork_UnpackToLive_Repair

- **Address:** `0x14021DE98`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveWork_UnpackToLive_Repair(void)`
- **Callers:** sub_1402FB7C8 (call at 0x1402FB9EE, one caller)
- **Callees:** EventVar_Write, Skillset_GetAbility, sub_1400FF6B8, sub_1401009E8, sub_1401E8C9C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

(I) A second unpack variant that copies the work copy to the live arrays and re-derives the ability flags from the JobTable and the skillset table.

## Behavior

- I (decompile): reads `g_JobTable[49 * job]` and calls Skillset_GetAbility while copying.
- V: one caller; Skillset_GetAbility is in the callee list, which supports the skillset-based ability repair. The load path that needs it is not established.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [Skillset_GetAbility](Skillset_GetAbility.md)

## Referenced by

- Called by: [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md)
- Reads tables: [JobTable](../tables/JobTable.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

Which load path uses it (a load-time repair of old saves is the guess, I).
