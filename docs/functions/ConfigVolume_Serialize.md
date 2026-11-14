# ConfigVolume_Serialize

- **Address:** `0x1400C48FC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void ConfigVolume_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** ConfigSettings_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the volume settings: overall, music, sound effects, voice and movie volume, and the visual-effect switch.

## Behavior

- V: builds 6 descriptors and runs FieldSchema_Run over them.
- V: field names: `volumeAll`, `volumeBGM`, `volumeSE`, `volumeVoice`, `volumeMovie`, `enableVisualEffect`.
- V: used by ConfigSettings_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [ConfigSettings_Serialize](ConfigSettings_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
