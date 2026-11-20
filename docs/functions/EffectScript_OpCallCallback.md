# EffectScript_OpCallCallback

- **Address:** `0x14031AC98`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectScript_OpCallCallback(struct EffectScriptCtx *ctx)`
- **Callers:** EffectScript_Run (through the opcode handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect script opcode: runs one effect callback at once.

## Behavior

- V: unless paused or stepping, takes the callback from the effect callback table (0x1406759C0) by the signed word at instruction offset + 2, keeps it in the context (+288) and calls it with the context's word at +2.
- V: always advances the instruction offset by 4 and returns 1.

## Referenced by

- Called by: [EffectScript_Run](EffectScript_Run.md)

## Notes

Name is ours.

## Open questions

None recorded.
