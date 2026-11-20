# EventCharaSprite_SetTable256Entry

- **Address:** `0x1400D1B74`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventCharaSprite_SetTable256Entry(void *sub, uint32_t entry_id, float seconds)`
- **Callers:** EventScript_Run, case 0xCB (call site 0x14023E772). Also sub_1400CEB4C (call site 0x1400CEF81), sub_1400CF2A8 (call site 0x1400CF2FB) and sub_14021EE0C (call site 0x14021EE74).
- **Callees:** `sub_1403D325C`, `sub_1403D3AE8`, `sub_1403D2FD8`, `sub_1400D1CB8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads a table-256 (PostEffectGlare) row into a sub-object of the unit sprite renderer and sets how long the change takes. The name is kept, but the table is the glare setting of the picture, not a sprite table.

## Behavior

- V: the first argument is the sub-object at g_CharaRenderer +148512. The second is the table id, passed as the entry id. The third is a float: 0.5 for operand 0xFFFFFFFF from opcode 0xCB, otherwise the signed operand divided by a constant (the divisor was not resolved).
- V: uses the cached table pointer qword_143CD9F60. When it is zero it gets table 256 from the root qword_143CD9CD0 with sub_1403D325C (root, 256) and caches it.
- V: finds the row with sub_1403D3AE8 (table, entry id, and two arguments that the caller does not set).
- V: when the row is missing, or its first qword is non-negative and its data pointer is null, nothing else happens.
- V: copies four dwords from the row data into the sub-object: data +20 to +3888, data +16 to +3892, data +12 to +3896, and data +8 (zero-extended, 8 bytes) to +3900.
- V: stores the entry id at +3912 and the float at +3908.
- V: table 256 is PostEffectGlare; the key a map variation passes is its post_effect_glare member (Map variation element +0x14).
- V: when the float is negative, copies the 16 bytes at +3888 to +3856 and to +3872, then calls sub_1400D1CB8 on the sub-object. Otherwise it copies the 16 bytes at +3856 to +3872 only.
- I: sub_1400D1CB8 computes four positions from the dwords at sub-object +4448 and +4452. It was only partly read.

## Referenced by

- Called by: [MapRenderer_ApplyVariationEffects](MapRenderer_ApplyVariationEffects.md)
- Called by event opcodes: [0xCB](../opcodes/README.md)
- Reads tables: [NxdDataPostEffectGlare](../tables/NxdDataPostEffectGlare.md)

## Notes

The third argument is passed in a float register, and the two unset arguments of sub_1403D3AE8 are not set by the callers in the 0xCB path. The name does not fit what the function loads: table 256 is PostEffectGlare (four floats of a row go to +3888..+3900, the key to +3912). Its callers are the event script command and the map variation applier (MapRenderer_ApplyVariationEffects passes the Map variation element post_effect_glare key).

## Open questions

The divisor for the duration (the float register value at the call site was not found in the function). What the four positions from sub_1400D1CB8 are used for, and the meaning of the dwords at data +8 to +20.
