# JournalPanel_Tick

- **Address:** `0x140169404`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalPanel_Tick(void *panel)`
- **Callers:** not recorded
- **Callees:** EventViewer_StartReplay, sub_1400FB3B0, sub_1402CD714

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The replay panel's state steps.

## Behavior

- V: state 1: pauses input, closes the list, sub_1400FB3B0(-2), hides the guide, sub_1402CD714(7), then state 2.
- V: state 2, after the fade: EventViewer_StartReplay(panel +112, +126); dword_142FF9F4C = +116; +127 = 1; state 3.

## State touched

- Calls: [EventViewer_StartReplay](EventViewer_StartReplay.md)

## Referenced by

- Appears in flows: [ChronicleEventReplay](../flows/ChronicleEventReplay.md)

## Open questions

None recorded.
