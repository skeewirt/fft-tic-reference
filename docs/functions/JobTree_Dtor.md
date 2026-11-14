# JobTree_Dtor

- **Address:** `0x140133574`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_Dtor(JobTreeAddon *addon)`
- **Callers:** UI manager (wrapper sub_14013349C)
- **Callees:** sub_14028F528

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Destructor body of UIAddonFFTOUnitJobTree (called through wrapper sub_14013349C, vtable slot 0).

## Behavior

- V: restores the base vtables, destroys the 20 panel records (stride 456) in reverse, then runs the base destructor. The wrapper deletes with size 0x2FD8.

## Open questions

None recorded.
