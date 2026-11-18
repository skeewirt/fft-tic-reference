# SaveFieldDescriptor

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 88 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One field of a saved record, as the save walker reads it (built on the stack by each schema function).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="name"></a>`0x0` | name | `char *` | V | Pointer to the field name; becomes the name of the child node. |
| <a id="type"></a>`0x8` | type | `uint32` | V | Value kind: 0 nested record (own callback), 1 unsigned byte, 2 signed byte, 3 signed 16-bit, 4 32-bit, 5 64-bit, 6 and 7 value-only nodes, 8 raw record bytes, 9 value mapped through a lookup list. |
| <a id="offset"></a>`0xC` | offset | `uint32` | V | Byte offset of the field in the record. |
| <a id="element_size"></a>`0x10` | element_size | `uint16` | V | Stride between elements of an array. |
| <a id="count"></a>`0x12` | count | `uint16` | V | Element count; above 1 the walker writes one child per element. |
| <a id="callback"></a>`0x18` | callback | `function *` | V | Nested-record callback for type 0 (a generic schema runner). |
| <a id="callback_arg"></a>`0x20` | callback_arg | `function *` | V | Argument of the callback: the schema function of the nested record. |
| <a id="lookup_callback"></a>`0x38` | lookup_callback | `function *` | V | Type 9: returns the lookup list. |
| <a id="lookup_arg"></a>`0x40` | lookup_arg | `pointer` | V | Type 9: argument of the lookup callback. |
| <a id="lookup_extra"></a>`0x48` | lookup_extra | `pointer` | I | Type 9: extra argument, passed to the lookup callback by address. |

## Referenced by

- Described by tables: [SaveFieldDescriptorLists](../tables/SaveFieldDescriptorLists.md)

## Open questions

None recorded.
