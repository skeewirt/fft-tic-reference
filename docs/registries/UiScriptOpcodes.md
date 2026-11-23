# UiScriptOpcodes

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [UiScript_Run](../functions/UiScript_Run.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 29-slot handler table (image address 0x1406838F0) that UiScript_Run indexes with the opcode byte of each record; the conditional handlers also index it for the records they govern. Slot 8 is empty. The script ends at opcode 33 (0x21), which has no slot. Each handler takes the record pointer and returns the next record's pointer. Only slots verified in the table are listed.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="uiscript_opdrawwindow"></a>0 | `UiScript_OpDrawWindow` | `0x140327DAC` | V | Bordered window and its fill. |
| <a id="uiscript_opif"></a>1 | `UiScript_OpIf` | `0x140327954` | V | Conditional run of the next records. |
| <a id="uiscript_opifelse"></a>2 | `UiScript_OpIfElse` | `0x140327A04` | V | Conditional with an else branch. |
| <a id="uiscript_opfillrect"></a>3 | `UiScript_OpFillRect` | `0x140327AF0` | V | Flat-coloured rectangle. |
| <a id="sub_140327b7c"></a>4 | `sub_140327B7C` | `0x140327B7C` | V | Draw-cell handler shared by slots 4 and 5 (not read in full here). |
| <a id="sub_140327b7c"></a>5 | `sub_140327B7C` | `0x140327B7C` | V | The same handler as slot 4. |
| <a id="uiscript_opdrawiconcell"></a>6 | `UiScript_OpDrawIconCell` | `0x140327CF4` | V | Picture cell from a row callback's descriptor. |
| <a id="uiscript_opdrawline"></a>7 | `UiScript_OpDrawLine` | `0x140327C3C` | V | Line between two points. |
| <a id="uiscript_opsetpaletteword"></a>9 | `UiScript_OpSetPaletteWord` | `0x140328734` | V | Palette word. |
| <a id="uiscript_opsetpalettewordalt"></a>10 | `UiScript_OpSetPaletteWordAlt` | `0x140328780` | V | Palette word with an alternate operand set. |
| <a id="uiscript_opsettint"></a>11 | `UiScript_OpSetTint` | `0x1403288C8` | V | Tint colour. |
| <a id="uiscript_opsetpageword"></a>12 | `UiScript_OpSetPageWord` | `0x1403287FC` | V | Texture-page attribute word. |
| <a id="uiscript_opdrawnumber"></a>13 | `UiScript_OpDrawNumber` | `0x140328920` | V | Number or gauge (zero-padded, no tint). |
| <a id="uiscript_opsetblendflag"></a>14 | `UiScript_OpSetBlendFlag` | `0x140328878` | V | Semi-transparency word. |
| <a id="uiscript_opsetpriority"></a>15 | `UiScript_OpSetPriority` | `0x14032890C` | V | Draw priority word. |
| <a id="uiscript_opscrolllist"></a>16 | `UiScript_OpScrollList` | `0x140329548` | V | Scrolling list. |
| <a id="uiscript_opfilltiles"></a>17 | `UiScript_OpFillTiles` | `0x140328490` | V | Rectangle filled with 16-pixel tiles. |
| <a id="uiscript_opdrawwindowopening"></a>18 | `UiScript_OpDrawWindowOpening` | `0x140328398` | V | Window that opens over a few redraws. |
| <a id="uiscript_opqueuescreenrectonce"></a>19 | `UiScript_OpQueueScreenRectOnce` | `0x140329EFC` | V | Fixed screen rectangle once after a window animation. |
| <a id="uiscript_opqueuerect"></a>20 | `UiScript_OpQueueRect` | `0x140329F4C` | V | Rectangle from the record. |
| <a id="uiscript_opqueuescreenrect"></a>21 | `UiScript_OpQueueScreenRect` | `0x140329FB0` | V | Fixed screen rectangle. |
| <a id="uiscript_opadvanceopening"></a>22 | `UiScript_OpAdvanceOpening` | `0x140329FEC` | V | Advances the opening stage (one-byte record). |
| <a id="shoppage_opdrawnumber"></a>23 | `ShopPage_OpDrawNumber` | `0x140328D54` | V | A handler not read here. |
| <a id="uiscript_opsetdrawmode"></a>24 | `UiScript_OpSetDrawMode` | `0x14032888C` | V | Draw-mode change. |
| <a id="uiscript_opdrawnumber"></a>25 | `UiScript_OpDrawNumber` | `0x140328920` | V | Number, no leading zeros, tinted. |
| <a id="uiscript_opdrawnumber"></a>26 | `UiScript_OpDrawNumber` | `0x140328920` | V | Number, zero-padded with dimmed zeros, sign at a fixed x. |
| <a id="uiscript_opdrawnumber"></a>27 | `UiScript_OpDrawNumber` | `0x140328920` | V | Number, zero-padded, tinted. |
| <a id="uiscript_opdrawlinerel"></a>28 | `UiScript_OpDrawLineRel` | `0x140327C94` | V | Line from a point by an offset. |

## Notes

Slots 4 and 5 and slot 23 point at handlers not documented here. Slots 13, 25, 26 and 27 share one handler that tells them apart by the opcode byte.

## Open questions

None recorded.
