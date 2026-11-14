# ResourceHandle_StateStep

- **Address:** `0x1403BA658`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 ResourceHandle_StateStep(ResourceHandle *h)`
- **Callers:** vtables only: FontResourceHandle_14071FD18, ModelResourceHandle_140720298, TextureResourceHandle_1407203C8, CustomResourceHandle_140720578, AdditionalKerningResourceHandle_1407206A8 (slot 7)
- **Callees:** virtual +136 / +176 / +184 / +224 / +240 / +280 / +288, sub_140096120, sub_140026BD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 7 of every faith::Graphics::*ResourceHandle class (Font, Model, Texture, Custom, AdditionalKerning): advances the handle's load state machine by one step.

## Behavior

- V: state = dword h+84 (atomic read). 0 and 1 return 0. 2: calls virtual +224, sets state 7, returns sub_140096120(h). 3 returns 0. 4 or anything above 7: falls to the last block. 5: virtual +240(h, h+96); on a negative result returns sub_140026BD4(Str, ..., result, 2) (error report), else state = 6 and continues as 6. 6: requires virtuals +176 and +280 to return non-zero (else returns 2), virtual +288 and +184 to be >= 0 (else error report with 0x96120027); then state = 3 and returns 0. 7: state = 1000 and then the last block.
- V (last block): result = virtual +136(h); negative -> error report; 0 -> returns 1; else returns result.
- I: state numbers: 1 = idle / not started, 2 = unload requested, 3 = ready, 5 = created, 6 = opened, 7 = unloaded (reload starts the streaming state 1000 of TextureResourceHandle_StreamStep).

## Notes

Name proposed (IDB: sub_1403BA658); the state names are inferred from the transitions only.

## Open questions

? names of the virtuals +136 .. +288 and of the states; ? the return convention (0 = done, 1 = still working, 2 = failure).
