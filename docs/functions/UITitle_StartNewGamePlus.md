# UITitle_StartNewGamePlus

- **Address:** `0x1401C3A28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UITitle_StartNewGamePlus(UIAgentFFTOTitle *agent)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Kind 1 (text 2226, New Game +): fades out and sets agent state 0x201, only when no save request is pending.

## Behavior

- V: the menu action for kind 1 jumps here.

## Notes

This name replaces an earlier one (`UITitle_StartType1`).

## Open questions

None recorded.
