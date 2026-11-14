# ConfigFile_Serialize

- **Address:** `0x1400C5868`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void ConfigFile_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** ConfigRoot_Serialize
- **Callees:** FieldSchema_Run, ConfigGuideFlag_Serialize, ConfigSettings_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the config file body: the settings and guide records, the output id, window position, resolution, refresh rate and the cleared, classic-started and enhanced-started flags.

## Behavior

- V: builds 12 descriptors and runs FieldSchema_Run over them.
- V: field names: `config`, `guide`, `outputId`, `windowPosX`, `windowPosY`, `resolutionW`, `resolutionH`, `refreshRateNumerator`, `refreshRateDenominator`, `isGameCleared`, `isClassicStarted`, `isEnhancedStarted`.
- V: its nested records use ConfigGuideFlag_Serialize, ConfigSettings_Serialize.
- V: used by ConfigRoot_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [ConfigGuideFlag_Serialize](ConfigGuideFlag_Serialize.md), [ConfigSettings_Serialize](ConfigSettings_Serialize.md)

## Referenced by

- Called by: [ConfigRoot_Serialize](ConfigRoot_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
