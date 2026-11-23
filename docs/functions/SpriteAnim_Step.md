# SpriteAnim_Step

- **Address:** `0x14038EDD4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned long SpriteAnim_Step(int *anim, int arg)`
- **Callers:** the opening scene tasks
- **Callees:** none (all work is inline)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Advances one opening / title sprite animation by a tick and queues the cells of its current frame.

## Behavior

- V: picks the cell list set of the text language (0x1407BF170 language 0, 0x1407BF0A0 language 3, 0x1407BF240 default, 0x1407BF310 language 2) and the frame list of the animation id from the 18-pointer script table (0x140699730).
- V: increments the tick counter; when it reaches the frame's hold ticks the frame index advances (wrapping at the frame count, 0xFFFF holds), then queues up to 32 cells of the frame's cell group with the animation's colour.

## Referenced by

- Called by: [SceneLoop_Run](SceneLoop_Run.md)
- Reads tables: [OpeningSpriteLists](../tables/OpeningSpriteLists.md), [SpriteAnimScripts](../tables/SpriteAnimScripts.md)

## Open questions

?: the cell group record layout.
