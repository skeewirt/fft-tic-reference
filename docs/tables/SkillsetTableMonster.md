# SkillsetTableMonster

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14067F4C0`
- **Rows:** 48 rows of 5 bytes
- **Keyed by:** skillset id 176..223
- **Read by:** [Skillset_GetAbility](../functions/Skillset_GetAbility.md), [sub_140281A64](../functions/sub_140281A64.md), [sub_140282E38](../functions/sub_140282E38.md)
- **Row layout:** [MonsterSkillsetRow](../structs/MonsterSkillsetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Monster skillsets: four ability slots per set.

## Behavior

- V: two other readers address bytes at +0x14067F58A, inside this range.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: whether the bytes at 0x14067F58A belong to a flag table that overlaps the monster rows
