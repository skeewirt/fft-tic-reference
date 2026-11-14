# UIGadgetFFTOVScrollText_ApplyScroll

- **Address:** `0x1402AAD30`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIGadgetFFTOVScrollText_ApplyScroll(UIGadgetFFTOVScrollText *g, __int64 ownerNode)`
- **Callers:** vtable only: vftable_ffto::Game::UI::UIGadgetFFTOVScrollText_140716A50 slot 8
- **Callees:** GUINode_SetPosition, GUINode_FindPartByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the scroll offset: moves the text node (g+40) to y = -scroll and re-centres the marker node (g+160) on the 'ScrollMark' part of the owner.

## Behavior

- V: runs only when ownerNode == qword (g + 8). y = 0, unless the owner's byte +416 is set, then y = (int)(0.0 - float(ownerNode + 672)) (the scroll offset of the scroll component).
- V: GUINode_SetPosition(text node g+40, its x (+56), y).
- V: part = GUINode_FindPartByName(ownerNode + 272, key at qword_143CDA2A0 + 0x13F8). When the marker node (g+160) and the part exist: SetPosition(marker, its x, marker.h (+68) + part.y (+60) + part.h (+68) / 2 - marker.h / 2) with C integer halving. (Hex-Rays showed v6 as an unset register; the disassembly loads it from g+0xA0.)

## State touched

- Calls: [GUINode_SetPosition](GUINode_SetPosition.md), [GUINode_FindPartByName](GUINode_FindPartByName.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

Name proposed (IDB: sub_1402AAD30). The text is scrolled by moving the node, not by clipping offsets inside the text. The key text at +0x13F8 was not read.

## Open questions

? the text of the part name key +0x13F8 (I: a scroll-bar track / thumb part).
