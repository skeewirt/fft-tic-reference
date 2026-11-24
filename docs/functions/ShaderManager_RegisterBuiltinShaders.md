# ShaderManager_RegisterBuiltinShaders

- **Address:** `0x1403CD018`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 ShaderManager_RegisterBuiltinShaders(void)`
- **Callers:** sub_1401E6E5C (0x1401E70EF)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Registers the 37 built-in shaders, ids 1000 to 1036, each with a name, a vertex blob and a pixel blob, in the shader manager at qword_140D3AD60+432.

## Behavior

- V: one register call per shader (the manager's virtual slot at +24) with the id, a vertex blob and its size, a pixel blob and its size, and the name text; the ids 1000 .. 1036 are consecutive.
- V: id 1020 is SHADER_ID_DEBUG_LINE and id 1021 is SHADER_ID_DEBUG_DEPTH; the others are the fill, font, sprite, render-target, classic and refined background and character shaders, the effect, post-effect, blur and depth-of-field shaders.
- V: id 1010 passes a pointer to a blob that starts with the DXBC magic where the others pass a data pointer.
- V: finishes by calling the manager's virtual slot at +72 with 1002 and 0.
- I: the two debug shaders are never requested by a draw path in this build. Searched: the draw-mode table (DrawMode_BuildShaderTable never assigns them), Shader_GetStateOverrides, and a scan of all immediates and displacements for 1020 and 1021, whose other hits are unrelated (UserSituation_IsMet calls with 1020 in sub_1400FD0E4 and sub_1402AC520, a 1020 in sub_1401158E4, a 1021 in sub_140121144, memset sizes and struct displacements).

## Referenced by

- Observed behaviours: [DebugShadersAreRegisteredButNeverRequested](../behaviors/DebugShadersAreRegisteredButNeverRequested.md)

## Notes

The shader blobs are compiled shader programs; their contents are not documented here.

## Open questions

? whether a draw path computes an id from a variable (a computed 1020 / 1021 would not show in the scan).
