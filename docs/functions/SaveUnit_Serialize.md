# SaveUnit_Serialize

- **Address:** `0x1400B99BC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveUnit_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorld_Serialize (as the per-unit schema)
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes one saved unit (character) record: it builds a table of 108 field descriptors and runs FieldSchema_Run over it. The largest schema in the game.

## Behavior

- V: builds 108 descriptors on the stack, each with a name, a type and an offset into the unit record, then returns FieldSchema_Run(ctx, node, record, table, 108).
- V: the fields cover identity (character id, name key, display name, name number, sex, two birth values, union), job state (current job, job-change flag, job level, 23 job-point fields and 23 total-job-point fields), abilities (two reaction, two support and two move slots, the sub-command, 22 ability-flag groups), equipment (the equipped items and three equipment sets plus the current set number), progress and base stats (experience, level, starting bravery and faith, base HP, MP, WT, AT and MAT) and a few unit-order, team and join fields.
- V: the function has no direct callers; it is referenced as the per-unit schema from SaveWorld_Serialize.
- I: this is the `GlobalWork` character record of the old notes; both describe 108 fields.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

The 23 job-point and total-job-point fields line up with the 23 job slots

## Open questions

Map each descriptor offset to the in-memory unit record fields.
