# JobTree_Create

- **Address:** `0x140113970`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void *JobTree_Create(...)`
- **Callers:** UI manager
- **Callees:** JobTree_Ctor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Factory that allocates a UIAddonFFTOUnitJobTree and runs JobTree_Ctor (call at 0x140113E28).

## Behavior

- V: operator new(0x2FD8) at 0x140113E16 (the size is an immediate first argument): the whole addon is one fixed-size object.

## State touched

- Calls: [JobTree_Ctor](JobTree_Ctor.md)

## Open questions

None recorded.
