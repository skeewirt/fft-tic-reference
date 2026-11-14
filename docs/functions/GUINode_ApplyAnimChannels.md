# GUINode_ApplyAnimChannels

- **Address:** `0x140400840`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ApplyAnimChannels(AnimChannelSet *a, float t, GUINode *node, char absolute)`
- **Callers:** GUIComponent_ApplyStateAnims
- **Callees:** sub_1404080C4, sub_140407C18, UIAnim_SampleFloatTrack, sub_140408218, sub_140408328, sub_140407DF8, sub_140407D40, sub_140407D9C, GUINode_SetPosition, sub_1403EF6B4, sub_1403EF738, sub_1403F4604, sub_1403F1BB8, sub_1403F1C24, sub_1403F1C90

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Samples every keyframe track of one animation channel set at time t and stores the results into the node's transform / colour / opacity / per-kind fields.

## Behavior

- V: returns at once when node+150 != 0. Track pointers are a[6]..a[31]; a null track is skipped; a track that returns 0 (no key at or before t, or the key's interpolation id is 0) leaves the field unchanged.
- V (tracks, in order): a[6] position (int pair, sub_1404080C4) -> GUINode_SetPosition; a[7] size (int pair) -> sub_1403EF6B4; a[8] scale (float pair, sub_140407C18) -> sub_1403EF738; a[9] rotation float -> node+88 (dirty +149 when it changes by > 1.19e-7); a[10] sort order int -> node+92 (and sets parent+216 re-sort flag); a[11] colour -> node+100; a[12] colour percent -> node+104; a[13] opacity float -> node+108; a[14] bool track -> node+144 (visible).
- V (combination with the current value when absolute = 0; with absolute != 0 the sampled value replaces it): position += (node+56, node+60); size += (node+64, node+68); scale *= (node+80, node+84); rotation += node+88; sort order += node+92; colour: each byte c = sampled * node+100 byte / 255 (integer truncating, alpha too); colour percent: clamp(sampled * node+104 / 100, 0, 255) per channel, alpha likewise; opacity *= node+108; visible = sampled && node+144.
- V (per kind, same combine rule): kind 2 (image) a[15] -> node+248, a[16] -> node+252 (ints; sets the part / frame); kind 3 (text) a[17] colour -> node+280; kind 4 a[15] -> +224; kind 5 a[15] -> word +312; kind 6 four colour tracks (indices 15..18, via sub_140407DF8) -> the four colour dwords node+208..+220 (colour multiply /255); kind 7 a[15] int -> +224, a[22]/a[23] floats -> +228 / +232, a[24]/a[25] colours -> +236 / +240; kind 8 a[26..28] floats -> +260 / +264 / +268 (+260 sets +279 dirty), a[29]/a[30] colours -> +240 / +244, a[31] float -> +284 (multiply; sets +279), and per element tracks 65.. (4 tracks per element of the 552-byte vector at node+216: two int pairs added to the element's +0/+4, +8/+12 and +16/+20, and a float multiplied into +24); kind 9 a[15] -> +232.
- V: absolute = the state's byte +111 (GUIComponent_ApplyStateAnims passes S+111). GUIComponent_LoadDef and UIAnim_PlayStateTracks set it to 1 for every UIB timeline state, so file states always replace the node's fields and nothing accumulates; the combining formulas above apply only to states created another way (? none found).

## State touched

- Calls: [UIAnim_SampleFloatTrack](UIAnim_SampleFloatTrack.md), [GUINode_SetPosition](GUINode_SetPosition.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Referenced by

- Called by: [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md)

## Notes

The name is ours (IDB: sub_140400840). Colour tracks are interpolated per byte by sub_1404022A8 (float lerp, clamp 0..255, truncating (int)), position / size tracks by UIAnim_SampleInt2Track, so animated node positions are integers.

## Open questions

Whether any state is created with absolute = 0 (file states are not); what kinds 4 / 5 / 6 / 7 are; the meaning of bool track a[14] timing (sub_1403F4604 handles hold length and curve < 1.0 steps).
