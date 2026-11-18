# EffectSprite_StepAnimation

- **Address:** `0x140387B70`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectSprite_StepAnimation(EffectSpriteNode *node, char r, char g, char b)`
- **Callers:** (through the effect sprite node list)
- **Callees:** sub_14038DC58, sub_1403807F4, sub_1400D31CC, EffectSprite_EmitPieces

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steps one effect sprite's animation script and, on a frame change, points the sprite at the new frame's pieces; then draws it.

## Behavior

- V: when not paused and bit 0 of dword_1407B0758 is set, the hold counter (node +22, s16) drops by 2; at 0 or below the next step of the script (node +24 pointer, node +32 position) is read.
- V: script steps are 3 bytes: frame (0..127), hold (stored at +22), a depth mode (stored at +20); a hold of 0 leaves the position on that step (the frame stays). A first byte of 0x80 or more is a code: 0x81 back to the start, 0x82 then s16 x, s16 y = set the position (+8, +10), 0x83 then s8 dx, dy = move it.
- V: a new frame (node +35 differs) sets +6 bit 0; then the frame set offset is the s16 at section 0 + byte node +34, the frame record at section 0 + the u16 at (that offset + 2 * frame), its piece count at record +2 and its pieces (24 bytes each) from record +4; the sprite primitive (+40) gets one pointer per piece (a new primitive when the count changes).
- V: the depth mode picks the drawing order slot: 1 = depth - 8, 2 = 8, 3 = 382, 4 = 16, 5 = depth - 16, else the projected depth / 4, clamped 0..382; the sprite is drawn by EffectSprite_EmitPieces.
- V: section 0 is the file's header dword [0] + 4 (qword_1411A3850); the script comes from section 1 (qword_1411A3858): EffectEmitter_Spawn sets node +24 to section 1 + the u16 at (2 * emitter byte +21) and node +34 to 2 * emitter byte +24.

## State touched

- Calls: [EffectSprite_EmitPieces](EffectSprite_EmitPieces.md)

## Notes

Name is ours (was sub_140387B70). The codes 0x81..0x83 are tested in the code as a negative byte and (byte & 0x7F) == 1, 2, 3, so the literal numbers do not appear. Seen from data: every one of the 397 stock effect files decodes by these rules into frames that match its texture sheet.

## Open questions

? the rate of the animator step in seconds (one step per drawn frame at 30 or 60 per second).
