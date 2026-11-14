# GUIComponentProps_Copy

- **Address:** `0x1403DF454`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char sub_1403DF454(GUIComponentProps *dst, const GUIComponentProps *src)`
- **Callers:** sub_140408C4C
- **Callees:** UIName_Assign

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a component's 254-byte render-property block (the effect enable bytes and values: blend, colour transform, offsets, drop shadow, glow, clip and the two mask names) from one component to another. The pointers are component + 16.

## Behavior

- V: the block offsets below are relative to component+16 (add 16 for the runtime component offset used by GUIComponent_LoadProps and ComponentEffects_Collect). It copies: +0 (blend type, comp+16), +4 qword (comp+20..+27, blend 17 parameters), +12..+27 and +28..+43 (comp+28..+59: colour multiply and add), +44 (comp+60 enable), +48 / +56 / +64 qwords (comp+64..+87: the six offset floats), +72 (comp+88 enable), +76 and +80 (comp+92 float, comp+96 enable).
- V: drop-shadow group: +84 (comp+100, blur radius), +88 (comp+104, strength), +92 qword (comp+108 / +112, offset), +100 (comp+116, colour), +104 byte (comp+120, enable). Then +108..+139 eight dwords (comp+124..+155, the blend 14..16 parameters).
- V: glow group: +140..+155 four dwords (comp+156..+171: strength, radius, colour, mode), +156 byte (comp+172, enable). Then +160 / +164 dwords (comp+176 / +180), bytes +168 / +169 / +170 (comp+184 / +185 / +186, the +186 group flags and enable), +172 dword (comp+188) and +176 byte (comp+192, enable).
- V: clip: +180 sixteen bytes and +196 dword (comp+196..+211, +212 margins), +200 byte (comp+216, enable). Mask: UIName_Assign for the name at +208 (comp+224) and +232 (comp+248), dword +224 (comp+240), bytes +228 (comp+244 enable), +248, +249, +252 and +253 (comp+264, +265, +268, +269).
- V: padding bytes between the fields are not copied; the function returns the last byte copied (+253).
- V: its only caller sub_140408C4C calls GUIComponent_ResetEffects first, then sub_1403DF454(a1 + 16, a2 + 16), then copies the node data at +272 (sub_1403EF54C), the name at +504, the flags +520..+572 and the child list, and ends by stopping / playing the +554-selected state names (GUINode_StopState / GUINode_PlayStateAtFrame). I: it is the component clone / assign routine.

## State touched

- Calls: [UIName_Assign](UIName_Assign.md)

## Notes

Proposed name: GUIComponentProps_Copy (the in-memory twin of GUIComponent_LoadProps, which fills the same fields from the UIB file). The scan hit on fields +100 / +104 / +116 / +120 is this function's copy of the drop-shadow group (block +84 / +88 / +100 / +104 plus 16). sub_140408C4C has three callers: sub_1403F9DC4, sub_14040BFB0, sub_14040E7F0.

## Open questions

? which component operations call the three callers of sub_140408C4C (clone for list items, template instantiation?). ? the role of +4 qword (comp+20) for blend types other than 17.
