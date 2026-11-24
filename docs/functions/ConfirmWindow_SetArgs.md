# ConfirmWindow_SetArgs

- **Address:** `0x14029C9A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfirmWindow_SetArgs(ConfirmWindow *window, void *vector)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the message arguments from a vector {allocator, begin, end, capacity}.

## Behavior

- V: each argument is 264 bytes: text `char[256]`, then its type at +256 (4 text, 1 number).

## Referenced by

- Called by: [sub_1401321FC](sub_1401321FC.md)

## Open questions

None recorded.
