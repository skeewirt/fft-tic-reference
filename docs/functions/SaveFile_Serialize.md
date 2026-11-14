# SaveFile_Serialize

- **Address:** `0x1400C2598`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveFile_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** None found directly (referenced through a pointer).
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the top level of a save file: the list of sections and which schema fills each.

## Behavior

- V: builds a table of 11 descriptors and runs FieldSchema_Run over it.
- V: the sections are `card`, `info`, `world`, `battle`, `user`, `ffto_world`, `ffto_battle`, `ffto_achievement`, `ffto_config`, `ffto_brave_story` and `ffto_v150`.
- V: no direct callers; it is reached through a function pointer.
- I: the plain sections come from the original game; the `ffto_` sections hold the data this edition adds.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

Sub-schemas such as SaveWorld_Serialize and SaveJobNew_Serialize are reached from the section descriptors.

## Open questions

Where the save and load code picks this function up.
