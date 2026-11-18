# SaveSlot_LoadToLive

- **Address:** `0x1400C45A0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `uint8_t *SaveSlot_LoadToLive(int64_t mgr, int slot)`
- **Callers:** sub_1401839E4, UIAgentFFTOTitle_Update
- **Callees:** SaveWork_UnpackToLive, Str_Format, sub_140033CBC, sub_140034CF0, memmove, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads one save slot: copies it from the RAM cache into the work copy and unpacks it into the live arrays.

## Behavior

- V (decompile): `memmove(g_SaveWorkCurrent, g_SaveSlotCache + 40164 * slot, 0x9CE4); SaveWork_UnpackToLive(0)`.
- V: if the situation byte (`Src[282]`) is 1 it also loads the `resume_enma%02d_world.sav` entry as AUTOENHANCED and flags a battle resume.

## State touched

- Calls: [SaveWork_UnpackToLive](SaveWork_UnpackToLive.md), [Str_Format](Str_Format.md), [sub_140033CBC](sub_140033CBC.md), [sub_140034CF0](sub_140034CF0.md)

## Referenced by

- Appears in flows: [AutoSaveRead](../flows/AutoSaveRead.md)
- Called by: [UIAgentFFTOTitle_Update](UIAgentFFTOTitle_Update.md), [sub_1401839E4](sub_1401839E4.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md)
- Reads file formats: [BattleResumeImage](../formats/BattleResumeImage.md), [ResumeEntry](../formats/ResumeEntry.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
