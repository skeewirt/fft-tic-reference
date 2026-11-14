# CharaRender_InitTargets

- **Address:** `0x1400CCEC0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaRender_InitTargets(CharaRendererState *s, short size, short groundX, short groundY)`
- **Callers:** sub_1400D4648 (renderer init)
- **Callees:** sub_1403D1498, sub_140087120, sub_140087AB4, sub_140086D28, sub_140087318, sub_14026E484

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the per-slot render targets and vertex buffers (256 slots) and stores the target geometry used by the draw.

## Behavior

- V: stores size, ground x, ground y at +75832, +75834, +75836; the renderer init (sub_1400D4648) passes 256, 128, 192 (config struct values 256 / 128 / 192, scale 2.0 float).
- V: for each of 256 slots creates a size x size texture (sub_1403D1498) and its render target, plus a 16-byte state and a vertex buffer; then loads the six default colour tables for the current language.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_TextureTable](../globals/g_TextureTable.md)

## Referenced by

- Called by: [CharaRenderer_Init](CharaRenderer_Init.md)

## Open questions

None recorded.
