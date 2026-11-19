# BattleVoice_SpeakAbilityPhase

- **Address:** `0x1401ECC90`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_SpeakAbilityPhase(void *controller, void *request)`
- **Callers:** sub_1401ED708
- **Callees:** NxdEntry_GetRow, sub_1401ECEFC, sub_1401ECC44

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the voice line of an ability from the Ability row's voice list by the request phase and speaks it.

## Behavior

- V: the list is the Ability row's voice offset (+0x24) and count (+0x28); the entry is chosen by the request phase (+8): 3 and 4 give entries 0..1, 5 entry 0, 6 entry 1 or 2 by vtable slot 7, 7 and 8 entry 0 or 1.
- V: a line that BattleVoice_UsesRows2And3 marks replaceable goes through BattleVoice_SpeakSwapped, others are played directly.

## State touched

- Calls: [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)

## Notes

Name is ours.

## Open questions

None recorded.
