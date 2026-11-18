# ImageDissolve_Step

- **Address:** `0x140372518`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long ImageDissolve_Step(void *job, int step, void *source)`
- **Callers:** sub_140371F68, sub_14037270C, sub_140372990
- **Callees:** sub_140260718

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One step of a dissolve that reveals an image through scattered pixels.

## Behavior

- V: step 0 clears the target buffer to 0xFF and the 16 line counters; steps 1..49 copy, for each of 16 line groups, 32 pixels at the offsets of the next row of the dissolve table (0x1407BE720) per group and advance that group's counter (up to 32 rows); the buffer is uploaded after each group.
- V: returns 1 when every group finished and 0 otherwise; a step above 49 ends the effect.

## Referenced by

- Reads tables: [DissolveOffsets](../tables/DissolveOffsets.md)

## Open questions

None recorded.
