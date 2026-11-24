# DebugShadersAreRegisteredButNeverRequested

- **Kind:** observed behaviour
- **Scope:** engine (shader library)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [ShaderManager_RegisterBuiltinShaders](../functions/ShaderManager_RegisterBuiltinShaders.md), [DrawMode_BuildShaderTable](../functions/DrawMode_BuildShaderTable.md), [Shader_GetStateOverrides](../functions/Shader_GetStateOverrides.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The shader library registers two debug shaders, a line shader (id 1020) and a depth shader (id 1021), like the other 35. No draw-mode table entry and no instruction in the executable asks for them by id; the pixel shaders also carry an unused-looking debug parameter in their constant buffer.

## Behavior

- V: ShaderManager_RegisterBuiltinShaders registers the ids 1000..1036 including 1020 (SHADER_ID_DEBUG_LINE) and 1021 (SHADER_ID_DEBUG_DEPTH).
- V: DrawMode_BuildShaderTable never assigns 1020 or 1021 to a draw mode.
- I: no draw path requests them; searched: that table, Shader_GetStateOverrides and a scan of all immediates and displacements for 1020 and 1021, whose other hits are unrelated (UserSituation_IsMet calls in sub_1400FD0E4 and sub_1402AC520, sub_1401158E4, sub_140121144, memset sizes, struct displacements).
- V: Shader_GetStateOverrides clears the byte at out+4 for 1020 and for 1000 only.
- I: the two debug shaders are never drawn with in this build.
- V: the string m_vDebugParam occurs 25 times in the shader blobs (cbDrawPS 26 times), as a name in the constant-buffer description, not read from shader code.
- ?: whether any of those shaders reads m_vDebugParam, and whether the CPU side writes it (not traced).

## Open questions

? how the registered ids are chosen when drawing (a computed id would not be seen).
