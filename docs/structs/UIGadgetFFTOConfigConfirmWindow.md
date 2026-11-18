# UIGadgetFFTOConfigConfirmWindow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The confirm window gadget of General Options (+2400; vtables 0x140712448 and 0x1407124A0): a message and up to three option buttons loaded from a UIDialog row.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="button_text_0"></a>`0x48` | button_text_0 | `GUINode *` | V | Text node of option 1 (+80, +88 the others; text id at node +248). |
| <a id="message_text_id"></a>`0xC0` | message_text_id | `int32` | V | The message text id. |
| <a id="flags"></a>`0x1AD` | flags | `uint8[]` | V | The row's flags (`ShowBlack` / `HideBlack`, the `Button<n>` layout by the number of options). |

## Behavior

- V: ConfirmWindow_SetDialog loads a UIDialog row; ConfirmWindow_SetArgs copies the message arguments (264 bytes each: text char[256], type at +256: 4 text, 1 number); input is vtable +64 (ConfirmWindow_OnInput): out[0] = the chosen button (0 the first, -1 nothing yet; 100 / 105 in its special modes).

## Open questions

None recorded.
