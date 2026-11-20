# SoundCue_Play

- **Address:** `0x1402BAA30`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int SoundCue_Play(uint32_t cue)`
- **Callers:** EventCmd_AllocSlot, EventChannel_BindStepTask, EventScript_SkipTick, JobScreen_ShowPopup, sub_1400F4BCC, sub_140269554, sub_14026B310, EffectScript_OpRunTimeline, sub_14031CF90 and about 20 more battle effect and UI functions
- **Callees:** IdRemap_Lookup, sub_1401D7808, sub_1401D736C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays a sound cue on the first free sound channel of 13..19: remaps the cue with IdRemap_Lookup, drops it when the result is above 0x2B1, and returns the channel used or -1.

## Behavior

- V: the cue is passed through IdRemap_Lookup first; a result above 0x2B1 (which includes -1, the remap table's "no sound") returns -1 and plays nothing.
- V: it then tests channels 13 to 19 in order with sub_1401D7808 on the sound manager qword_143CD9DD8 and stops at the first channel where that test returns 0 (free); all seven busy returns -1.
- V: on a free channel it calls sub_1401D736C(manager, channel, remapped cue), stores the remapped cue in dword_14375F8C4[channel - 13] and returns the channel number.
- V (live 2026-11-12): a battle effect's sound event reaches it from EffectScript_OpRunTimeline with cue = the effect track value + dword_14114B124 - 1 (0x730000 for a stock Potion); IdRemap_Lookup turns 0x730000 into 0x137, which plays (the Potion chime). A cue the remap table does not list is returned unchanged and, being above 0x2B1, is dropped silently.

## State touched

- Calls: [IdRemap_Lookup](IdRemap_Lookup.md)

## Referenced by

- Called by: [EffectScript_OpRunTimeline](EffectScript_OpRunTimeline.md), [EquipSprite_BuildPieces](EquipSprite_BuildPieces.md), [EventChannel_BindStepTask](EventChannel_BindStepTask.md), [EventCmd_AllocSlot](EventCmd_AllocSlot.md), [JobScreen_ShowPopup](JobScreen_ShowPopup.md), [sub_1400F4BCC](sub_1400F4BCC.md), [sub_140269554](sub_140269554.md)
- Observed behaviours: [SoundCuesAreRemappedBeforeTheyPlay](../behaviors/SoundCuesAreRemappedBeforeTheyPlay.md)
- Reads file formats: [EffectSoundTracks](../formats/EffectSoundTracks.md), [SoundBankSab](../formats/SoundBankSab.md)

## Notes

Read 2026-11-12. Every caller passes a cue id, not a resource handle; the bound 0x2B1 is checked after the remap, so the remap table is what makes the large cue ids (effect bank values such as 0x730000) playable.

## Open questions

? what sub_1401D736C does with the channel beyond starting the cue (the cue bank lookup); whether channels 13..19 are shared with event music.
