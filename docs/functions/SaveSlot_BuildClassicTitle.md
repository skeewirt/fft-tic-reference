# SaveSlot_BuildClassicTitle

- **Address:** `0x14021C07C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveSlot_BuildClassicTitle(int slot, uint8_t *out, int64_t arg)`
- **Callers:** sub_14021AEC0 (0x14021AFC5), sub_14021BD04 (0x14021BFA0)
- **Callees:** sub_1402BACCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the CLASSIC-mode slot title text: hero name, job name, level, date and location, in the classic text encoding.

## Behavior

- V (J9): the leader's job byte `Src[274]` walks the classic job-name string block `qword_14375F958` entry by entry (unbounded); the hero name is copied from +257.
- V (J9): it is the only reader of the saved job byte (summary +274) found in the save path.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [sub_14021AEC0](sub_14021AEC0.md), [sub_14021BD04](sub_14021BD04.md)

## Notes

J9 S4: a class name would need a classic text encoder (?).

## Open questions

None recorded.
