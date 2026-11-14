# ShaderSelector_Apply

- **Address:** `0x14039EC9C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int ShaderSelector_Apply(ShaderSelector *sel, ThreadState *ts, unsigned int program)`
- **Callers:** UIRender_ApplyDrawState, SDFFontRenderer_Flush, UIBlur_CopyTarget, UIBlur_DrawPass, UIBlur_DrawTexturedPass, UIBlur_DownsampleDispatch, GUILayer_CopyToTarget, GUILayer_BlurShadowPass, GUILayer_BlitFinal, GUILayer_GlowPass, GUILayer_EffectPass0, UIRender_DrawOverlayQuads, UIRender_DrawLetterbox, sub_1403AC420, sub_1403AC620, sub_1403ACEBC, sub_1403AF890, sub_1403AFA9C, sub_1403AFD34, sub_1403AFF8C, sub_1403B5170, sub_1403B53C8, sub_1403B5664, sub_1403C595C, sub_1403CB9C4
- **Callees:** ShaderProgram_ApplyState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves the selector's current permutation index to a program table and applies the program with the given index (within that permutation) to the thread state.

## Behavior

- V: when the dirty byte sel+76 is set, program table pointer sel+56 = techniqueProgramTable (tech+136) + 8 * (table[slot].base (+24) + permutationIndex (sel+24) * table[slot].stride (+20)), where table = tech+120 with 32-byte entries and slot = sel+72; clears the dirty byte.
- V: then tail-jumps to ShaderProgram_ApplyState(sel + 24, ts, program): the third argument (register r8d) is passed through unchanged. It is the program index within the selected permutation: the program-table slot is the pointer at sel+56 plus 8 * program and the 64-byte state entry is the pointer at sel+48 plus 64 * program.
- V: most call sites pass literal indices, for example: GUILayer_CopyToTarget 0, GUILayer_BlurShadowPass 1, GUILayer_BlitFinal 0, GUILayer_GlowPass 0, GUILayer_EffectPass0 3, sub_1403B53C8 2, sub_1403B5170 4, UIRender_DrawOverlayQuads 5, UIRender_DrawLetterbox 0, SDFFontRenderer_Flush 0..4, UIRender_ApplyDrawState 0, sub_1403AF890 7, sub_1403AFD34 3, sub_1403AFF8C 4, sub_1403B5664 1, sub_1403CB9C4 0; the decompile shows two arguments where the value is a zeroed register.
- V: the UI manager (*(g_Renderer + 37936)) keeps its selectors as pointers at +8 * index: #9 (+72) is used by GUILayer_BlitFinal and sub_1403CB9C4, #10 (+80) by GUILayer_CopyToTarget (program 0) and GUILayer_BlurShadowPass (program 1).

## State touched

- Calls: [ShaderProgram_ApplyState](ShaderProgram_ApplyState.md)

## Referenced by

- Called by: [GUILayer_BlitFinal](GUILayer_BlitFinal.md), [GUILayer_BlurShadowPass](GUILayer_BlurShadowPass.md), [GUILayer_CopyToTarget](GUILayer_CopyToTarget.md), [GUILayer_EffectPass0](GUILayer_EffectPass0.md), [GUILayer_GlowPass](GUILayer_GlowPass.md), [PostTarget_DrawFitted](PostTarget_DrawFitted.md), [UIBlur_CopyTarget](UIBlur_CopyTarget.md), [UIBlur_DownsampleDispatch](UIBlur_DownsampleDispatch.md), [UIBlur_DrawPass](UIBlur_DrawPass.md), [UIBlur_DrawTexturedPass](UIBlur_DrawTexturedPass.md), [UIRender_DrawLetterbox](UIRender_DrawLetterbox.md), [UIRender_DrawOverlayQuads](UIRender_DrawOverlayQuads.md), [sub_1403B5170](sub_1403B5170.md)

## Notes

Live layout (UI manager+64 object): +16 technique, +24 permutation index, +28 digit count, +32 digit sizes (UI: 4, 2), +40 shader object array, +48 64-byte program entries, +56 program table, +64 shader index list. The program index (third argument) is a literal at most call sites and is easy to miss in the decompile, which drops a zeroed register.

## Open questions

Where the pass slot sel+72 is written (always 0 in live reads) (?). ? whether the 64-byte entries at sel+48 are shared by every permutation (the code indexes them by program only).
