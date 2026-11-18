# FieldSchema_LoadFromNode

- **Address:** `0x1400B059C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t FieldSchema_LoadFromNode(int64_t ctx, int64_t schema, int64_t node, int64_t rec, uint32_t flags)`
- **Callers:** FieldSchema_Run (the load direction, ctx+8 == 1)
- **Callees:** sub_1400B0FE8 .. sub_1400B14D4 (per-type loaders), sub_1405A415C, sub_1405A48F0, sub_1405A6614

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The load half of the field-schema walker: for each descriptor of a schema it looks a node up by name and decodes it into the record.

## Behavior

- V (decompile): when the node is absent it records error 0x96090007 and continues with the next descriptor, leaving the record field untouched; nodes that no descriptor names are never looked at.
- V: the return value is discarded by FieldSchema_Run.
- V: so a save that lacks a node still loads (the field keeps its value), and nodes no descriptor names are ignored.

## Notes

Correction: the manual save `fftsave.bin` is a flat memory image, not this tree; the tree is a different path (resume / cloud, ?).

## Open questions

None recorded.
