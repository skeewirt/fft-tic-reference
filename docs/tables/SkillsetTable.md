# SkillsetTable

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14067E210`
- **Rows:** 176 rows of 25 bytes
- **Keyed by:** skillset id 0..175
- **Read by:** [Skillset_GetAbility](../functions/Skillset_GetAbility.md)
- **Row layout:** [SkillsetRow](../structs/SkillsetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Ability slots of the stock skillsets. Skillset_GetAbility is the only reader: it returns 0 for a slot above 21 or a skillset above 226 and picks this table, the monster table or the special table by id.

## Behavior

- V: ability ids are 9 bits.
- V: 62 ids of the table are empty and no job row names them.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: which of the empty ids were used by the original game
