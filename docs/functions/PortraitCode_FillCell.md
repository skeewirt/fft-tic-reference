# PortraitCode_FillCell

- **Address:** `0x1402E16A8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `uint8_t PortraitCode_FillCell(void *rec, int code, int *outSlot, int *outColour)`
- **Callers:** sub_14032AB3C, EventMessage_Scripted, sub_1402C4550, sub_1402D7954, sub_1402D9490, sub_1402DF374, sub_14032D31C, sub_140376040
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a portrait code into the classic portrait atlas cell of a draw record and its colour, and returns the code's low byte.

## Behavior

- V: when outSlot is not null it is set to -1.
- V: the colour is ((code >> 10) & 3) + 8, written to *outColour: bits 10 and 11 of the code choose one of four colours.
- V: the cell comes from the code's low byte b: column (b % 40) & 7 (32 pixels wide, byte +20 and +36), row (b % 40) >> 3 (48 pixels high, +21 / +29 and +37 / +45), page b / 40 + 26 (word +30, low 4 bits, with bit 0x10 set).
- V: the word +22 packs a CLUT row in its bits 6 and up (350 + code for codes 104 to 111, the fixed portraits; 506 + (b - 63) % 6 for low bytes 63 to 82; else 496 + ((b % 40) >> 2); each wrapped with & 0x1FF from 512 up) and a column in its low 6 bits.
- V: returns (uint8_t)code; bits 8 and above (and the colour bits 10, 11) never reach the return value.
- M (unicorn, pristine exe): code 0x05 -> (5, colour 8), 0xD4 -> (212, 8), 0x100 -> (0, 8), 0x2FF -> (255, 8), 0x405 -> (5, 9), 0x805 -> (5, 10), 0xC05 -> (5, 11).

## Referenced by

- Appears in flows: [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md)
- Called by: [sub_1402DF374](sub_1402DF374.md), [sub_14032AB3C](sub_14032AB3C.md)
- Observed behaviours: [PortraitCodeIsAByteOnTheSaveRecordPath](../behaviors/PortraitCodeIsAByteOnTheSaveRecordPath.md)

## Notes

So on every path through this function a portrait code is a byte plus two colour bits: at most 256 distinct faces can come out of a code. The name is ours (IDB: sub_1402E16A8).

## Open questions

None recorded.
