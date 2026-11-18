# UIAgentFFTOTitle_Tick

- **Address:** `0x1401C2D20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOTitle_Tick(UIAgentFFTOTitle *agent, float dt)`
- **Callers:** not recorded
- **Callees:** UIAgentFFTOTitle_Update

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of the title agent (vtable 0x14070A5B0 slot 1).

## Behavior

- V: when the agent is active it runs UIAgentFFTOTitle_Update, then its +80 part.

## State touched

- Calls: [UIAgentFFTOTitle_Update](UIAgentFFTOTitle_Update.md)

## Open questions

None recorded.
