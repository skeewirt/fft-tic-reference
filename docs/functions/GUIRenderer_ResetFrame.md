# GUIRenderer_ResetFrame

- **Address:** `0x1403E6160`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall GUIRenderer_ResetFrame(__int64 r, unsigned __int8 a2, __int64 a3)`
- **Callers:** GUICore_CommitFrame, sub_1403D64F4 (V)
- **Callees:** UIDrawState_Copy, GUILayer_ResetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame reset of the GUI renderer: default draw states, clip bounds sentinels, the quad UV transform and all 512 layer records.

## Behavior

- V: UIDrawState_Copy(r, &unk_1408FF878) and UIDrawState_Copy(r+48, ...) install the default draw states in two slots; r+4 &= 0xFFFFFFF0, r+24 &= ~0x200, r+72 &= mask (I: clears blend / flag bits of those states).
- V: r+96 = 0, byte r+136 = 0 (recording flag, read by UIRender_AppendCommand / QueueImageDraw bit 0). Bounds sentinels: r+152 and r+160 = 0x41DFFFFFFFC00000 (as a double = +2147483647.0) and r+168 and r+176 = 0xC1E0000000000000 (double -2147483648.0): an inverted min / max rectangle initialised to extremes (I).
- V: quad UV transform at r+41264...41328: r+41264 = 2.0 / (float)*(int*)(r+184) (2 / width), r+41284 = 2 / -(float)*(int*)(r+188) (2 / -height, so y flips); r+41268, +41276, +41288, +41296 = 0; +41304 = 1.0 (0x3F800000 = 1065353216); +41312 = -1.0 (-1082130432); +41316 = 1.0; +41320 = -0.0 (0x80000000); +41324 = 1.0. This is a 4x4 screen-space-to-NDC matrix (x' = 2x/w - 1, y' = 1 - 2y/h) (I from the numbers).
- V: for layer index 0..0x1FF (512): layer record (592 bytes each, base r+303492 + 592*i): +0 = index, +572 = v10 = *(qword*)(R + 8*? + 6560) (R = qword_143CDA098: a default render target pointer, array at R+6560; r+...); GUILayer_ResetRecord(r, i) is called for each; V (disassembly, 2026-10-30): per slot the dirty rectangle (16 bytes at r + 512 * i + 41824), the layer id dword (r + 512 * i + 41840) and the flag byte after it (+41844) are zeroed, which is what GUILayer_Flush / GUILayer_ExpandBounds use.
- V: tail: r+606604 = -1, r+606584 / +606592 = 0, r+606600 = 0, r+606608 = 0, r+606616 = 0x7FFFFFFF, and the deferred-draw vector end r+606704 = begin r+606696 (clears the list GUIRenderer_RunDeferredDraws walks). *(*(R+37936)+208) = r + 303480 (current layer record pointer = the layer header just before the first record).

## State touched

- Calls: [UIDrawState_Copy](UIDrawState_Copy.md), [GUILayer_ResetRecord](GUILayer_ResetRecord.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)
- Writes: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

The decompile lost several register assignments (r in rdx/r10 etc.), so offsets above are exact but the grouping of the sentinel bounds (which pair is min vs max, float vs double) is I.

## Open questions

? which fields r+152..r+176 are (clip rect min/max?). ? exact meaning of a2 and a3 (unused in the decompile). ? what the 592-byte layer record holds besides index (+0) and default target (+572).
