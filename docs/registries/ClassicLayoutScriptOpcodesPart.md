# ClassicLayoutScriptOpcodesPart

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [ClassicUi_RunLayoutScript](../functions/ClassicUi_RunLayoutScript.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The slots of the 22-slot layout script table (image address 0x140693110, run by ClassicUi_RunLayoutScript, end opcode 22): the long list handler and three small rectangle handlers. The other slots are listed by the ClassicUi_Op* sheets.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="classicui_opscrolllist"></a>16 | `ClassicUi_OpScrollList` | `0x1403911B4` | V | Scrolling list. |
| <a id="classicui_opqueuescreenrectonce"></a>19 | `ClassicUi_OpQueueScreenRectOnce` | `0x140391AA4` | V | Fixed screen rectangle once. |
| <a id="classicui_opqueuerect"></a>20 | `ClassicUi_OpQueueRect` | `0x140391B04` | V | Rectangle from the record. |
| <a id="classicui_opqueuescreenrect"></a>21 | `ClassicUi_OpQueueScreenRect` | `0x140391B68` | V | Fixed screen rectangle. |

## Open questions

None recorded.
