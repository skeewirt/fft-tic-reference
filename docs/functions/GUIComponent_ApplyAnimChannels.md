# GUIComponent_ApplyAnimChannels

- **Address:** `0x1404015C0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_ApplyAnimChannels(AnimChannelSet *a, float t, GUIComponent *comp, char absolute)`
- **Callers:** GUIComponent_ApplyStateAnims, GUINode_ApplyStateAtFrame (both when the target name is '#Component')
- **Callees:** UIAnim_SampleColorTrack, KeyTrackVec2_Eval, UIAnim_SampleFloatTrack

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component-level counterpart of GUINode_ApplyAnimChannels: samples the tracks of the channel set that is addressed to '#Component' (the component itself) and writes them into the component's effect fields.

## Behavior

- V: tracks are pointers a[32]..a[59]; a null one is skipped, a track that returns 0 leaves its field alone. 'absolute' (a4) != 0 replaces the field with the sample; absolute == 0 combines it with the current value as listed.
- V: a[32] colour (UIAnim_SampleColorTrack): bytes / 255.0 -> RGBA floats; absolute == 0 multiplies each by the current float at comp+44..+56 (the additive colour of the colour-transform effect group), result stored to comp+44..+56. a[33] colour: bytes / 100.0 (percent), multiplied into comp+28..+40 (the multiplicative colour) the same way.
- V: vec2 tracks (KeyTrackVec2_Eval, ADDED to the current when absolute == 0): a[34] -> comp+64/+68, a[35] -> +72/+76, a[36] -> +80/+84, a[40] -> +108/+112.
- V: float tracks (UIAnim_SampleFloatTrack, MULTIPLIED by the current when absolute == 0): a[37] -> comp+92, a[38] -> +100, a[39] -> +104, a[41] -> +156, a[42] -> +160, a[44] -> +188 (the component opacity float). a[43] is written to comp+176 but, when absolute == 0, multiplied by the current value of comp+156 (not +176): read from the disassembly (mulss [rbx+9Ch] then movss [rbx+0B0h]); either a game bug or a deliberate coupling.
- V: only when comp+536 == 15 (BahamutEffect): a[45] vec2 -> comp+648/+652 (added); a[46] colour -> comp+708 (per byte c = sample * current / 255 integer, or replaced); a[47] float -> +704, a[48] -> +700, a[49] -> +672, a[50] -> +692, a[51] -> +696, a[52] -> +676, a[53] -> +680, a[54] -> +684, a[55] -> +688, a[56] -> +656, a[57] -> +660, a[58] -> +664, a[59] -> +668, all ADDED to the current.

## State touched

- Calls: [UIAnim_SampleColorTrack](UIAnim_SampleColorTrack.md), [KeyTrackVec2_Eval](KeyTrackVec2_Eval.md), [UIAnim_SampleFloatTrack](UIAnim_SampleFloatTrack.md)

## Notes

The name is ours (IDB: sub_1404015C0). Field meaning (V from ComponentEffects_Collect): +28..+56 colour transform, +64..+84 / +92 / +100..+112 the other effect groups, +156 / +160 the ring group the UnitSelect ring uses, +176 / +188 the groups at the end (+188 = opacity of the +192 group). So a state animating '#Component' drives these effect parameters; the combine rule (multiply for scalars, add for vec2, multiply for colours) differs from the node version (position add, scale multiply, opacity multiply).

## Open questions

? the a[43] -> +176 using +156 as the base. ? the semantic names of each Bahamut-effect field.
