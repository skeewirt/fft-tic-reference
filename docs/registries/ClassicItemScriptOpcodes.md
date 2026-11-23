# ClassicItemScriptOpcodes

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [ClassicItemUsePage_Run](../functions/ClassicItemUsePage_Run.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 25-slot handler table (image address 0x1406932A0) that the item pages of the legacy party menu run inline (ClassicItemUsePage_Run); the slot layout equals that of UiScriptOpcodes up to slot 24 where both have a handler, the draw globals are the item pages' own. Slot 8 is empty; the script ends at opcode 25 which has no slot.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="classicitemui_opdrawwindow"></a>0 | `ClassicItemUi_OpDrawWindow` | `0x14039B2C8` | V | Bordered window and its fill. |
| <a id="classicitemui_opif"></a>1 | `ClassicItemUi_OpIf` | `0x14039AD90` | V | Conditional run of the next records. |
| <a id="classicitemui_opifelse"></a>2 | `ClassicItemUi_OpIfElse` | `0x14039AE40` | V | Conditional with an else branch. |
| <a id="classicitemui_opfillrect"></a>3 | `ClassicItemUi_OpFillRect` | `0x14039AF2C` | V | Flat-coloured rectangle. |
| <a id="sub_14039b050"></a>4 | `sub_14039B050` | `0x14039B050` | V | Draw-cell handler shared by slots 4 and 5 (not read here). |
| <a id="sub_14039b050"></a>5 | `sub_14039B050` | `0x14039B050` | V | The same handler as slot 4. |
| <a id="classicitemui_opdrawiconcell"></a>6 | `ClassicItemUi_OpDrawIconCell` | `0x14039B210` | V | Picture cell from a row callback's descriptor. |
| <a id="classicitemui_opdrawline"></a>7 | `ClassicItemUi_OpDrawLine` | `0x14039B110` | V | Line between two points. |
| <a id="classicitemui_opsetpaletteword"></a>9 | `ClassicItemUi_OpSetPaletteWord` | `0x14039BBD0` | V | Palette word. |
| <a id="classicitemui_opsetpalettewordalt"></a>10 | `ClassicItemUi_OpSetPaletteWordAlt` | `0x14039BC1C` | V | Palette word with an alternate operand set. |
| <a id="classicitemui_opsettint"></a>11 | `ClassicItemUi_OpSetTint` | `0x14039BDD0` | V | Tint colour. |
| <a id="classicitemui_opsetpageword"></a>12 | `ClassicItemUi_OpSetPageWord` | `0x14039BC98` | V | Texture-page attribute word. |
| <a id="classicitemui_opdrawnumber"></a>13 | `ClassicItemUi_OpDrawNumber` | `0x14039BE28` | V | Number or gauge. |
| <a id="classicitemui_opsetblendflag"></a>14 | `ClassicItemUi_OpSetBlendFlag` | `0x14039BD14` | V | Semi-transparency word. |
| <a id="classicitemui_opsetpriority"></a>15 | `ClassicItemUi_OpSetPriority` | `0x14039BE14` | V | Draw priority word. |
| <a id="classicitemui_opscrolllist"></a>16 | `ClassicItemUi_OpScrollList` | `0x14039C784` | V | Scrolling list. |
| <a id="classicitemui_opfilltiles"></a>17 | `ClassicItemUi_OpFillTiles` | `0x14039B914` | V | Rectangle filled with 16-pixel tiles. |
| <a id="classicitemui_opdrawwindowopening"></a>18 | `ClassicItemUi_OpDrawWindowOpening` | `0x14039B81C` | V | Window that opens over a few redraws. |
| <a id="classicitemui_opqueuescreenrectonce"></a>19 | `ClassicItemUi_OpQueueScreenRectOnce` | `0x14039D0FC` | V | Fixed screen rectangle once after a window animation. |
| <a id="classicitemui_opqueuerect"></a>20 | `ClassicItemUi_OpQueueRect` | `0x14039D14C` | V | Rectangle from the record. |
| <a id="classicitemui_opqueuescreenrect"></a>21 | `ClassicItemUi_OpQueueScreenRect` | `0x14039D1B0` | V | Fixed screen rectangle. |
| <a id="classicitemui_opadvanceopening"></a>22 | `ClassicItemUi_OpAdvanceOpening` | `0x14039D1EC` | V | Advances the opening stage (one-byte record). |
| <a id="drawcmd_printnumber"></a>23 | `DrawCmd_PrintNumber` | `0x14039C200` | V | A handler not read here. |
| <a id="classicitemui_opsetdrawmode"></a>24 | `ClassicItemUi_OpSetDrawMode` | `0x14039BD28` | V | Draw-mode change. |

## Notes

Slots 4 and 5 (shared handler) and 23 are not documented here.

## Open questions

None recorded.
