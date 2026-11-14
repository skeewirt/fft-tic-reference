# RenderState_SeedCommands

- **Address:** `0x1403A32F4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderState_SeedCommands(void)`
- **Callers:** RenderFrame_Record
- **Callees:** sub_140069A38 (command allocate), sub_140069980 (submit)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues 79 tiny 8-byte render-state commands (type 38) on the thread's command list: one for each id in a fixed list, one for 44..59 and one for 79, 83, ... 281 step 4.

## Behavior

- V: v3 = thread-local render context (TLS +56). For each id the context dword +8 (qword) is set to (id << 31) and a command is allocated with sub_140069A38(ctx, 38, 8) and submitted with sub_140069980 when non-null.
- V: ids: first the 12 words of table unk_140720B40 = 17, 24, 43, 32, 66, 67, 68, 69, 284, 805, 823, 829; then i = 44..59 (16 ids); then j = 79, 83, 87, ... 279 (51 ids; the loop ends when j > 0x119 = 281, so 79..279); 12 + 16 + 51 = 79 commands.
- I: the commands look like per-pass or per-state 'enable' bits (id << 31 as a bitmask word) placed once at frame start; the consumer was not read.

## State touched

- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Called by: [RenderFrame_Record](RenderFrame_Record.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A32F4).

## Open questions

? what command type 38 does and what the ids index.
