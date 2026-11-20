# UnitWork_FindJobBySkillset

- **Address:** `0x14028AC50`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int UnitWork_FindJobBySkillset(UnitWork *c, int skillset)`
- **Callers:** sub_14022F868 (2), BattleCommand_BuildScreen (2), sub_140335140
- **Callees:** sub_14028668C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The first job of a work record's job list whose JobTable row holds `skillset`; the record's own job (+3) when none does.

## Behavior

- V: the list is sub_14028668C(c, list) (JobList_Build from the record's unlock bits at +159, mode 1).
- V: row guard per entry: job < 0xAE (stock); returns the matching job id or c +3.
- V: sub_14022F868 and BattleCommand_BuildScreen call it with the acting unit's record and the skillset byte of the battle command list being opened (a byte array indexed by the command kind 1..7; a 0 byte skips the call and keeps the record's job byte). The answer is the job id of the job record they build for that list (JobRecord_FromJobId), whose name heads the list: the job that owns the command, for the unit's own command and for a secondary one alike.
- V: sub_140335140 calls it for a named command (its second argument not 1) of list kinds 5 and 6, for the job record of the command header.
- V (seen live 2026-11-19): asked for a skillset that no job of the unit's list holds, it answered the record's job byte (76), and the list was headed by that job's name.
- V: its fallback is the unit's job byte +3 at 0x14028ACB5; 0x14028ACB9 is a branch target; the loop before it walks the unit's job list.

## State touched

- Calls: [sub_14028668C](sub_14028668C.md)

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [sub_14022F868](sub_14022F868.md)
- Observed behaviours: [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md)

## Open questions

None recorded.
