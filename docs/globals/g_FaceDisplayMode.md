# g_FaceDisplayMode

- **Kind:** global
- **Address:** `0x142FF9ED8`
- **Area:** [Graphics](../areas/graphics.md)
- **Type:** `int32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Face display mode word: when (mode & ~2) is 0 the face readers map a portrait code through SpriteId_ToShape, else they use the raw code; written 0 then 2 by sub_140210AF0 (battle setup), 0 by Video_RefreshState and sub_1402D3918 (I: 0 field and menus, 2 battle, other values event scenes).

## Referenced by

- Read by: [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md)

## Open questions

None recorded.
