# WorldMapNode_PlayTexChange

- **Address:** `0x140158E30`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapNode_PlayTexChange(void *node, int location)`
- **Callers:** not recorded
- **Callees:** GUINode_FindState, GUINode_PlayState, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the texture-change state of a location's base node.

## Behavior

- V: plays the state 'TexChange%02d' (Town base_number, +0x2C) on a node; location 21 uses 'TexChange14_34'.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [Str_Format](Str_Format.md)

## Referenced by

- Called by: [WorldMapBaseList_DrawRow](WorldMapBaseList_DrawRow.md)

## Open questions

None recorded.
