# EffectScript_OpSetCallback

- **Address:** `0x14031AC30`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectScript_OpSetCallback(struct EffectScriptCtx *ctx)`
- **Callers:** EffectScript_Run (through the opcode handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect script opcode: attaches one of the effect callbacks to a live callback slot.

## Behavior

- V: unless the game is paused or stepping, stores the callback pointer chosen by the signed word at instruction offset + 2 (the effect callback table at 0x1406759C0) into slot ((byte at +1) >> 2) & 0x3F of the live callback list.
- V: always advances the instruction offset by 4 and returns 1 (go on with the next opcode).

## Referenced by

- Called by: [EffectScript_Run](EffectScript_Run.md)

## Notes

Name is ours.

## Open questions

None recorded.
