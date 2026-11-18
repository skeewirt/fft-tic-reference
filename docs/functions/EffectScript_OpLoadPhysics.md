# EffectScript_OpLoadPhysics

- **Address:** `0x14031B9DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectScript_OpLoadPhysics(EffectScriptCtx *ctx)`
- **Callers:** EffectScript_Run (through tbl_EffectScriptHandlers, opcode 0x27)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect script opcode 0x27: loads the effect's gravity and drag from the header of section 3.

## Behavior

- V: section 3 +4 / +8 = gravity x, y (qword_143C51D70), +12 = gravity z (dword_143C51D78), +16 = drag (dword_143C51D4C); the emitter records follow the 20-byte header, 196 bytes each.

## Notes

Name is ours (was sub_14031B9DC).

## Open questions

None recorded.
