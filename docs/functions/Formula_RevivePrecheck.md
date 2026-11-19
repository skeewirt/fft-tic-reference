# Formula_RevivePrecheck

- **Address:** `0x140309504`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_RevivePrecheck(void)`
- **Callers:** Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_53_Revive, sub_140308C98
- **Callees:** Formula_ZeroResult, Formula_StatusTailKeepHit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Revive gate: runs the status tail and continues only when a status is pending or the target is Undead.

## Behavior

- V: calls Formula_StatusTailKeepHit first.
- V: returns 1 when R+39 bit 0x08 is set or the target has +0x61 bit 0x10 (Undead).
- V: otherwise it calls Formula_ZeroResult, sets R+2 = 7 and returns 0.

## State touched

- Calls: [Formula_ZeroResult](Formula_ZeroResult.md), [Formula_StatusTailKeepHit](Formula_StatusTailKeepHit.md)

## Referenced by

- Called by: [Formula_75_ItemRevive](Formula_75_ItemRevive.md)

## Notes

60 bytes, read whole.

## Open questions

None recorded.
