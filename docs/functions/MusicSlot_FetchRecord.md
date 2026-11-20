# MusicSlot_FetchRecord

- **Address:** `0x1402B1F08`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 MusicSlot_FetchRecord(int slot)`
- **Callers:** EventCmd_ActivateSlotParam and about 18 more event and menu functions
- **Callees:** sub_1402B1ED0 (reset)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Activates an event sound slot: loads its sound id and the three record dwords into the music state.

## Behavior

- V: clears the music state (resets it from a default block); a slot of 0 returns 0.
- V: stores slot - 1 as the active slot, loads the sound id of the slot into the music state and copies the three dwords of the sound's record (MusicSlotRecords, stride 12) into words 1..3.
- V: when the slot has an object, remembers it as the current slot object and returns it.

## Referenced by

- Called by: [sub_1401D9174](sub_1401D9174.md), [sub_14033FE00](sub_14033FE00.md)
- Observed behaviours: [EventSoundGroupAndMusicSlotOperandWidths](../behaviors/EventSoundGroupAndMusicSlotOperandWidths.md), [MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath](../behaviors/MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath.md)

## Notes

Name is ours.

## Open questions

?: what the two record numbers do in the music loader.
