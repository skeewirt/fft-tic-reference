# Formula_98_PhysicalBasedBraveModify

- **Address:** `0x14030934C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_98(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 98

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Brave change with a magic roll that ignores Faith: the magic evade gate, then a MA + X chance; on a hit the target's Brave changes by Y.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above (re-read 2026-11-18: the earlier calculation called the hit physical).
- V: Current-build symbol size is 50 bytes.
- V: Typical abilities: Dread Gaze.

## Calculation

```text
Gate: sub_140306D70 (shield and accessory evade)
Hit: Formula_MagicHitNoFaith (MA + X with the magic modifiers, no Faith)
On success: Brave change byte (R+24) = Y & 0x7F, kind bits 1
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
