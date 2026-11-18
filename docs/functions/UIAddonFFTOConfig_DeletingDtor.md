# UIAddonFFTOConfig_DeletingDtor

- **Address:** `0x1401886CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOConfig_DeletingDtor(UIAddonFFTOConfig *addon)`
- **Callers:** the add-on's vtable
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 0 of the General Options add-on: runs the destructor body and frees the object.

## Behavior

- V: calls the destructor body at 0x140188700.

## Open questions

None recorded.
