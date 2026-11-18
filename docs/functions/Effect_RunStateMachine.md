# Effect_RunStateMachine

- **Address:** `0x140319DA4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Effect_RunStateMachine(void)`
- **Callers:** sub_14031A3DC (at 0x14031A4B8)
- **Callees:** SceneObject_FindBySlot, sub_1400D258C, sub_14024F5A0, sub_1402741E0, sub_14031A840, sub_14031A994, sub_14031D658, sub_140381A54, sub_14038DD00

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame state machine of one battle effect: waits for the file load, uploads the texture, sets up the effect sections and runs the effect to its end.

## Behavior

- V: the state is dword_1418732C8. State 0 only returns 0. State 1 returns 1 (busy) unless the pause flag (bit 8 at g_PauseManager + 24) or bit 2 of dword_1407B0758 is set. State 2 (same guards) calls sub_14024F5A0 with 0x71 (built as 1 + 0x70 in the code), sets word_142FEF6DC to 1, calls EffectFile_UploadTexture and moves to state 3.
- V: state 3 (same guards) resets the effect heap (a free list starting at the texture section pointer qword_1411A3840 and ending at unk_141982E00) and reads the header dwords of the file at qword_143740220[word_141D330BC]: +0 and +4 (each plus 4) give two block pointers (qword_1411A3850, qword_1411A3858), +8 the main script pointer (qword_141873078), +12 a block (qword_1411A3810), +16 the records of 160 bytes (qword_1411A3848), +20 a block (qword_1411A3830), +24 the sound and timing section (qword_1411A3828), +28 a section with an 8-byte header (qword_1411A3860), +32 an optional section (0 = absent; qword_1411A3808) whose u16 at +10 shifted left by 16 becomes dword_14114B124, the sound cue base.
- V: state 3 then calls sub_1400D258C with the effect number (the NXD parameter rows) and starts the first effect node.
- V: state 4 runs the node list each frame (sub_14031D658, sub_14031A840 per node) and, when the list is empty, restores the renderer values, plays sub_14024F5A0 with 0x72, sets dword_142E801F4 to -1 and returns the state to 0.
- V: state 6 (reached through the default branch, same guards) repeats the heap reset from the saved pointers qword_1411A3838 and qword_1411A3820 and restarts the node list; it then sets the state to 4 plus an inner value.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [EffectSequence_Run](EffectSequence_Run.md)

## Notes

Name is ours. The header dwords are offsets inside the file (the pointer is the file base plus the dword), so the file does not depend on its own number. Section meanings below +8 are inferred from their readers (sub_14034xxx per-primitive renderers, sound functions sub_14031C2DC / sub_14031D010).

## Open questions

? the layout of the blocks at +0, +4, +12, +16, +20 and +28; what drives state 6 and what states above 6 do.
