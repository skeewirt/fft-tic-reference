# ChronicleTimeline_LayoutChapters

- **Address:** `0x140178384`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ChronicleTimeline_LayoutChapters(void *bar, int n2, int n3, int n4, int n5, int n6)`
- **Callers:** not recorded
- **Callees:** GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lays out the timeline bar by the number of periods in each chapter section.

## Behavior

- V: total = the sum of the five counts; positions the range of the 'Knob' part and the section nodes a1[51..55] by cumulative count / total, and plays 'Show' / 'HideChapter01..04Sepalator' at the section ends (the spelling is the game's).

## State touched

- Calls: [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Called by: [ChronicleTimeline_Setup](ChronicleTimeline_Setup.md)

## Open questions

None recorded.
