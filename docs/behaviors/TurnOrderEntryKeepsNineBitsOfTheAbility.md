# TurnOrderEntryKeepsNineBitsOfTheAbility

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A turn-order entry keeps 9 bits of the pending ability (byte 1 plus bit 7 of byte 0 for 256), so the combat timeline names an ability of 512 or more by the stock ability 256 + its low byte (512 = Vengeance).

## Behavior

- V (code): the tag and unit-panel decoders (TurnPanel_SetTag, TurnPanel_SetUnitPanel) and two more decoders build the timeline's name strings (Battle_TimelineBuildStrings 0x1403244FF, Battle_TimelineBuildStrings2 0x140364BD3: token 0x7000 + the decoded id).

## Open questions

None recorded.
