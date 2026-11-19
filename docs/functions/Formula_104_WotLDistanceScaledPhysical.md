# Formula_104_WotLDistanceScaledPhysical

- **Address:** `0x14030D620`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_104(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 104

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Distance-scaled weapon attack: the weapon-type value and WP, with WP + 3 next to the target, WP + 1 at two tiles and half the weapon-type value from three tiles, then the whole physical chain.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation said Y; the bonus goes to B, the weapon power (no ability Y is read).
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 190 bytes.

## Calculation

```text
Gate: sub_140306C90 (physical evade); sub_140305A48 (A = weapon-type value, B = WP)
Distance = max(|dx|, |dy|) of the two units' tiles (+0x4F, +0x50)
1: B += 3; 2: B += 1; 3 or more: A = A / 2
Then element boost, Formula_PhysMods, critical, Damage = A x B, element affinity, absorb, status tail
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
