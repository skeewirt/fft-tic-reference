# WorldMapBaseList_Construct

- **Address:** `0x14015F480`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t WorldMapBaseList_Construct(int64_t self)`
- **Callers:** WorldMapAgent_CreateAddons
- **Callees:** sub_140158C38, sub_14028F46C, UIListGadget_Ctor, sub_14028BB54, UIGadgetFFTORadioButtonMenu_Ctor, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the Locations list addon (struct WorldMapBaseList).

## Behavior

- V: base constructor sub_140158C38, then the list addon's vtable 0x14070F5C8 at +0 and the second base's vtable 0x14070F578 at +48.
- V: three 104-byte parts at +400 (sub_14028F46C), the list gadget at +720 (UIListGadget_Ctor), two button guide parts at +1048 and +1224 (sub_14028BB54), the radio button menu at +1400 (UIGadgetFFTORadioButtonMenu_Ctor).
- V: three record vectors at +1696 + 32 t (allocator at +0, begin +8, end +16, capacity end +24) set empty.
- V: current tab +1840, current location +1844 and +1848 = -1; the panel pointers +1792..+1832 cleared; the word +1852 = 1 (sound on row change on), +1854 = 0; +64..+343 and +360..+383 cleared.

## State touched

- Calls: [UIListGadget_Ctor](UIListGadget_Ctor.md), [UIGadgetFFTORadioButtonMenu_Ctor](UIGadgetFFTORadioButtonMenu_Ctor.md)

## Referenced by

- Called by: [WorldMapAgent_CreateAddons](WorldMapAgent_CreateAddons.md)

## Open questions

None recorded.
