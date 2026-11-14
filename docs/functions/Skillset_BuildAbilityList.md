# Skillset_BuildAbilityList

- **Address:** `0x140275980`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `uint16_t *Skillset_BuildAbilityList(int setId, uint8_t classMask)`
- **Callers:** Unit_BuildJobUnlockMask, Job_LearnAbilityByMenu, PartyUnit_FillFromWork, sub_140226E44, sub_1402867BC, sub_14028A370, sub_1402C4D1C, sub_1402DE564, sub_1402FE1D0, sub_140316D24, sub_14033B420, sub_140348828, sub_140360048, sub_1403783F0, sub_140388EB4, sub_14038BF34, sub_140392620
- **Callees:** Skillset_GetAbility

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 24-entry ability list of a skillset into a shared static buffer, keeping only the ability classes the caller's mask allows. Used by the job menu, learning, battle lists and the unlock mask.

## Behavior

- V: a set id above 255 is treated as set 0; entries 0..23 are filled from Skillset_GetAbility (slots 22 and 23 are always 0).
- V: classification by id: below 0x1A6 needs mask bit 1; 0x1A6..0x1C5 needs bit 2; 0x1C6..0x1E6 needs bit 8; above 0x1E6 needs bit 4. A class the mask lacks is replaced by 0.
- V: only for set 224: id 488 is kept only when mask bit 0x20 is set, and id 491 only when bit 0x10 is set.
- V: returns the address of the static buffer, so a later call overwrites an earlier result.
- V: callers pass 31 (0x1F) or 47 (0x2F) depending on bit 0x40 of party-record byte +112, which swaps which of the two set-224 abilities is offered (I: a unit flag, meaning not traced). The unlock check uses 15.

## State touched

- Calls: [Skillset_GetAbility](Skillset_GetAbility.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [JobAbilityList_Build](JobAbilityList_Build.md), [Job_LearnAbilityByMenu](Job_LearnAbilityByMenu.md), [Party_CountMasteredJobs](Party_CountMasteredJobs.md), [Skillset_BuildTabAbilityList](Skillset_BuildTabAbilityList.md), [sub_140226E44](sub_140226E44.md), [sub_1402C4D1C](sub_1402C4D1C.md), [sub_1402DE564](sub_1402DE564.md), [sub_1402FE1D0](sub_1402FE1D0.md), [sub_140316D24](sub_140316D24.md), [sub_14033B420](sub_14033B420.md), [sub_140388EB4](sub_140388EB4.md), [sub_14038BF34](sub_14038BF34.md), [sub_140392620](sub_140392620.md)
- Observed behaviours: [SkillsetIdsPastTheByte](../behaviors/SkillsetIdsPastTheByte.md)

## Notes

An ability id above 0x1E6 is kept or dropped by the movement-ability class rule. The list is written into the game's static list (0x143D1A1C0), whose address the function returns.

The four id classes line up with the action, reaction, support and movement ability ranges; the class bit decides which kinds a screen lists.

## Open questions

Which unit flag sets bit 0x40 at party +112.
