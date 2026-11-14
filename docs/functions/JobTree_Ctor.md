# JobTree_Ctor

- **Address:** `0x140133368`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `JobTreeAddon *JobTree_Ctor(JobTreeAddon *this)`
- **Callers:** UI manager
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor for UIAddonFFTOUnitJobTree (RTTI). Sets vtables 0x140711618 and 0x140711718.

## Behavior

- V: the destructor body is sub_140133574 (via wrapper sub_14013349C in vtable slot 0).
- V: the in-process hardware watch arms an execute breakpoint here to catch construction.

## State touched

- Writes: [JobTreeAddon.selectedSlot](../structs/JobTreeAddon.md#selectedslot)

## Referenced by

- Called by: [JobTree_Create](JobTree_Create.md)

## Notes

The addon base moves per run (ASLR), but panel-20 Unit gadget sat at addon - 0x19A3F60 in 5 runs.

## Open questions

None recorded.
