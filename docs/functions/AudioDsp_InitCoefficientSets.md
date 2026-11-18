# AudioDsp_InitCoefficientSets

- **Address:** `0x1404A203C`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `unsigned long long AudioDsp_InitCoefficientSets(int *config, long long memory)`
- **Callers:** the audio library DSP creation code (sub_140499C58)
- **Callees:** sub_14049F75C, sub_14049F098, sub_1404A26A4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises the work area of an audio DSP unit and fills its per-channel coefficient pointer slots.

## Behavior

- V: aligns the memory to 16 bytes and clears 0x2208 bytes; lays out one 512-byte buffer per channel (the channel count is config[0]) behind it and two further work blocks.
- V: copies pairs of pointers from the lists of exe.audio.dsp_coefficient_block_pointers into the channel slots: with more than eight channels from the sub-lists at the table start and 0xC0 bytes on, otherwise from the sub-lists 0x180 and 0x200 bytes on (the code addresses them as symbol differences, so no 0x180 constant shows in the decompilation; the choice also reads config[4]).
- V: stores a 20-byte block copied from config, then calls a second set-up function (sub_1404A26A4) on the work area and returns its address.

## Referenced by

- Reads tables: [AudioDspCoefficientBlockPointers](../tables/AudioDspCoefficientBlockPointers.md)

## Notes

Name is ours. Read partially: the second set-up call and the coefficient meaning are not decoded.

## Open questions

?: what the coefficient blocks compute.
