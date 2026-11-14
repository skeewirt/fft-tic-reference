# CharaRenderer_PostFrame

- **Address:** `0x1402567E0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 CharaRenderer_PostFrame(__int64 a1, int a2, int a3, int a4)`
- **Callers:** frame render
- **Callees:** sub_1400D0D3C, CharaRenderer_GlareChain, sub_1403CB56C, sub_1403CB8BC, sub_1403CB9C4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

End-of-frame pass of the unit (chara) renderer: runs the glare chain when enabled, then the post/resolve steps.

## Behavior

- V: with g_CharaRenderer+153013 == 0 and +152992 != 0 it calls sub_1400D0D3C(g_CharaRenderer + 148512, a2, a3, a4, (float)dword_142E7FAE4) and then CharaRenderer_GlareChain (sub_1400D1018) on g_CharaRenderer + 148512, and sets v5 = 1 (the second render-target description at unk_142C819D0 + 136).
- V: with +153012 != 0 and +153013 == 0 it renders the UI-style full-screen pass (shader id 1002 through the shader table qword_140D3AD60) and sets +153013 = 1.
- V: then resolves through sub_1403CB8BC / sub_1403CB9C4 (colour-grading input xmmword_142E7FC70) unless disabled by qword_143CD9DD0+103 or the two debug words.

## State touched

- Calls: [CharaRenderer_GlareChain](CharaRenderer_GlareChain.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)

## Notes

Flags at g_CharaRenderer+152992 (glare on), +153012 and +153013 (post pass done) have not been read live yet.

## Open questions

Whether the Job Tree UI is drawn into the target this chain post-processes (?).
