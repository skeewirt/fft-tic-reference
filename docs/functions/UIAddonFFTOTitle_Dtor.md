# UIAddonFFTOTitle_Dtor

- **Address:** `0x1401C3E64`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOTitle_Dtor(UIAddonFFTOTitle *addon)`
- **Callers:** the add-on's vtable
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Destructor of the title menu add-on: puts the base class's vtables back and frees the 240 bytes.

## Behavior

- V: the base class vtable 0x14070CDD8 is stored back before the base destructor runs; the 240-byte block is freed.

## Open questions

None recorded.
