# SaveWorld_Serialize

- **Address:** `0x1400BD078`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveWorld_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize (as the `world` section's schema)
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the world part of a save: the 54 unit slots and the party item, shop, found-item, event and sort lists.

## Behavior

- V: builds a table of 76 descriptors (0x4C) and runs FieldSchema_Run over it.
- V: 54 of them are the unit slots `UnitSaveData_00` to `UnitSaveData_53`, each using SaveUnit_Serialize.
- V: the others cover the party, shop and found items, the event work area (`eventwork`, where the event variable store lives), the option record, the weave-in command and a group of sort-order lists for battle units, world units and items.
- V: no direct callers; it is referenced as a schema by SaveFile_Serialize.
- I: `eventwork` is the saved copy of the event variable store described on the event-system pages.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

A save holds 54 unit slots in this build.

- Correction (from a schema dump by emulation): the top-level section this schema builds is named `battle` (the 54-unit schema); the section named `world` is `0x1400B9228`.

## Open questions

Confirm that `eventwork` is the same storage that EventVar_ResolveSlot addresses.
