# SaveSlots_LoadFromFile

- **Address:** `0x1400C3B24`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveSlots_LoadFromFile(int64_t mgr)`
- **Callers:** sub_14018403C, UIAgentFFTOTitle_Update, sub_1402185A4, sub_140218728
- **Callees:** sub_140033CBC, sub_140034CF0, sub_1400C6008

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the `fftsave.bin` entry from the save container into the manager's image (the slot cache is filled from it by sub_1402185A4).

## Behavior

- V (decompile): `sub_140033CBC(file, "fftsave.bin")`, then tags the load "CLASSIC" or "ENHANCED" by `dword_1407D453C`.
- V: called when the title menu opens (UIAgentFFTOTitle_Update case 4).

## State touched

- Calls: [sub_140033CBC](sub_140033CBC.md), [sub_140034CF0](sub_140034CF0.md), [sub_1400C6008](sub_1400C6008.md)

## Referenced by

- Appears in flows: [SaveFrameStep](../flows/SaveFrameStep.md)
- Called by: [UIAgentFFTOTitle_Update](UIAgentFFTOTitle_Update.md), [sub_14018403C](sub_14018403C.md), [sub_1402185A4](sub_1402185A4.md), [sub_140218728](sub_140218728.md)
- Reads file formats: [BattleResumeImage](../formats/BattleResumeImage.md), [ManualSaveEntry](../formats/ManualSaveEntry.md)

## Notes

J7 had named sub_140218728 as the load; J9 lists that address as a different flat-image load, so it was left unnamed in the integration pass.

## Open questions

None recorded.
