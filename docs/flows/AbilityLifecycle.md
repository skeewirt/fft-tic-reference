# AbilityLifecycle

- **Kind:** flow
- **Area:** [Ability data](../areas/ability-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The order in which the game reads an ability, from the skillset row that offers it to the presentation and the save: where it comes from for a unit, the menus and lists, choosing and targeting, the action request and turn order, resolving, passive abilities, presentation, and what is stored. Each step names the functions and the id width at that point (8, 9, 10 or 16 bits); the width differs between steps, which is why an id that fits one step is cut at the next.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1a source: skillset row"></a>1a source: skillset row | [Skillset_GetAbility](../functions/Skillset_GetAbility.md) | V | Decodes a set row (low byte + flag bit, 9 bit ids; sets above 226 give 0). Eleven functions call it. |
| <a id="1b source: skillset list"></a>1b source: skillset list | [Skillset_BuildAbilityList](../functions/Skillset_BuildAbilityList.md) | V | Builds the 24-entry list of a set and sorts ids into ranges (below 0x1A6, 0x1A6..0x1C5, 0x1C6..0x1E6, above); 17 functions call it. |
| <a id="1c source: job list"></a>1c source: job list | [JobAbilityList_Build](../functions/JobAbilityList_Build.md) | V | Maps a job to its set and filters by tab (tab 0 keeps ids 1..421); two more copies of the filter sit in Skillset_BuildTabAbilityList and sub_140392620. List words carry flags 0x1000/0x2000/0x4000 above a 10-bit id. |
| <a id="1d source: learned state"></a>1d source: learned state | [Unit_TryLearnAbility](../functions/Unit_TryLearnAbility.md) | V | Learning sets a bit per slot of the job's set (22 bits per class); the bit means Skillset_GetAbility(set, slot). |
| <a id="1e source: item command"></a>1e source: item command | [Unit_ListItemCommandItems](../functions/Unit_ListItemCommandItems.md) | V | The Item command maps item ids 240..253 to abilities 368..381 (item + 0x80) through a 14-byte table. |
| <a id="1f source: crystal"></a>1f source: crystal | [sub_140271EFC](../functions/sub_140271EFC.md) | V | The post-battle roll learns from a 512-id bitmap and skips ids above 0x1FF. |
| <a id="1g source: learn abilities and jp"></a>1g source: Learn Abilities and JP | [Ability_GetJpCost](../functions/Ability_GetJpCost.md) | V | JP cost is the Ability name row's value at +64; the learn screen rows go through the name-row getter. |
| <a id="2a menus: battle lists"></a>2a menus: battle lists | [sub_14030E368](../functions/sub_14030E368.md) | V | Usable-ability lists per command (with sub_14030DD8C and sub_14030EC48); ids outside 1..0x16F and 406..413 are listed with no cost entry; a skillset that is neither the unit's primary nor secondary counts every slot as learned. |
| <a id="2b menus: selection message"></a>2b menus: selection message | [sub_140237FA4](../functions/sub_140237FA4.md) | V | Writes the selection message whose +6 word is the chosen ability; the command-list word is cut to 9 bits here in stock. |
| <a id="2c menus: names and help"></a>2c menus: names and help | [AbilityTable_GetRow](../functions/AbilityTable_GetRow.md) | V | Name, description, icon, JP and order key come from the Ability name table by key with no range check on the id (24 calls in 18 functions). |
| <a id="3a choose: confirm"></a>3a choose: confirm | [sub_140206F90](../functions/sub_140206F90.md) | V | Confirm handler: stores the shape result at unit +0x194 and cuts unit +0x17A to 9 bits before reading the aux row. |
| <a id="3b choose: range and area"></a>3b choose: range and area | [BattleRange_ApplyShape](../functions/BattleRange_ApplyShape.md) | V | Marks range and area from the action record; returns -1 for ids at or above 368 (with BattleRange_MarkRing and BattleRange_MarkArea). |
| <a id="3c choose: mp"></a>3c choose: MP | [sub_1402828E4](../functions/sub_1402828E4.md) | V | Checks and pays MP only for ids up to 0x16F with command kind 0; the preview twin is sub_14030B1A0. |
| <a id="4a request: queue"></a>4a request: queue | [sub_140281488](../functions/sub_140281488.md) | V | Validates the candidate and writes the request block at unit +0x1A0 (ability word at +0x1A2, 10 bit id plus unit); an item request is rewritten by +0x80. |
| <a id="4b request: current action"></a>4b request: current action | [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md) | V | Cuts the packed word to id & 0x3FF and builds the current-action block; reads the kind 1, 3 and 4 tables; ids at or above 368 get no record. |
| <a id="4c turn order"></a>4c turn order | [TurnList_InsertEntry](../functions/TurnList_InsertEntry.md) | V | Stores the ability low byte plus bit 0x80 in a 4-byte entry (9 bits, no spare bit); the two panel readers decode it. |
| <a id="5a resolve: targets"></a>5a resolve: targets | [BattleAct_BuildResult](../functions/BattleAct_BuildResult.md) | V | Scans targets from the range marks and calls Battle_ResolveAction for each; writes the effect word and the 512 sentinel. |
| <a id="5b resolve: dispatch"></a>5b resolve: dispatch | [Battle_ResolveAction](../functions/Battle_ResolveAction.md) | V | Takes the action row (id below 368, else row 0), clamps the formula byte at +8 to 1..106, calls the handler from the 106-entry registry, then runs the post tests for formula below 7 and equal to 100. |
| <a id="5c resolve: handlers"></a>5c resolve: handlers | [Formula_106_ReDispatchChainFormula](../functions/Formula_106_ReDispatchChainFormula.md) | V | Handlers read the ability id from the formula block word at 0x1407B0778; five of them switch on it; one re-indexes the registry unclamped. |
| <a id="6a passive: bit map"></a>6a passive: bit map | [Unit_SetAbilityBit](../functions/Unit_SetAbilityBit.md) | V | Innate and equipped reaction, support and movement ids 0x1A6..0x1FD become bits at unit +0x94..+0x9E. |
| <a id="6b passive: reaction chain"></a>6b passive: reaction chain | [Battle_ApplyActionResult](../functions/Battle_ApplyActionResult.md) | V | The tail tests the bits in a fixed order and hands the first hit to a Brave-roll helper; the executor sub_1403095E4 handles 422..434, 438, 439, 444 and 446 only. |
| <a id="7a presentation: look"></a>7a presentation: look | [BattleAnim_SelectMotion](../functions/BattleAnim_SelectMotion.md) | V | Animation, charge and text come from g_AbilityAnim (454 rows) indexed by the effect word, not by the ability id; 512 is a no-effect sentinel. |
| <a id="7b presentation: effect"></a>7b presentation: effect |  | V | Effect_SelectForAbility (0x140319B50) maps ids below 454 to g_AbilityEffectNumber and 512..548 to a 37-row pseudo table. |
| <a id="7c presentation: banner"></a>7c presentation: banner | [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md) | V | Case 7 cuts the word to 9 bits, adds 0x7000 and stores it as a kind-6 entry; the resolver BattleMsg_ResolveEntry masks 0x7FF and reads the Ability name row. |
| <a id="8 persistence"></a>8 persistence |  | V | Equipped reaction, support and movement ids are u16 in the save (A+8..13); learned abilities are bits per slot (ability_flag_00..21); skillset ids are bytes (A+7), u16 in the party record (B+96). |

## Behavior

- V: the id width differs per step: 9 bit at the aux accessor, the banner dispatcher, unit +0x17A and the turn entry; 10 bit in list words, the packed action word and unit +0x1A2; u16 in the save's equipped fields; 22 slot bits for learned state.
- V: the ability kind is not stored; Ability_GetAuxRecord derives it from eight id thresholds and several list builders repeat the ranges.
- V: the accessor caller sets match the research census: Ability_GetAuxRecord 18 functions, AbilityAction_GetRecord 33, Skillset_GetAbility 11, Skillset_BuildAbilityList 17, Ability_GetJpCost 7, JobAbilityList_Build 8 (IDA code references, 2026-11-10).

## Notes

Function names are the published reference names; the open database names some of them differently (same addresses).

## Open questions

? which 0x3FF masks act on an ability word (the notes disagree: 6 or 31 sites); ? what unit +0x17A holds.
