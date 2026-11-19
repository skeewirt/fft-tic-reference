# ChronicleTimeline_Setup

- **Address:** `0x140173E08`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ChronicleTimeline_Setup(void *screen)`
- **Callers:** not recorded
- **Callees:** ChroniclePeriod_ListUnlocked, ChronicleTimeline_LayoutChapters, sub_140178F84

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up the Chronicle timeline bar from the unlocked periods.

## Behavior

- V: builds the unlocked period list with ChroniclePeriod_ListUnlocked and finds the index of the current period (the low byte of the word at save block +7778, capped at 28).
- V: counts the listed periods by timeline_section (+0x10) values 2..6 and calls ChronicleTimeline_LayoutChapters(bar, n2, n3, n4, n5, n6), then sub_140178F84(bar, index).

## State touched

- Calls: [ChroniclePeriod_ListUnlocked](ChroniclePeriod_ListUnlocked.md), [ChronicleTimeline_LayoutChapters](ChronicleTimeline_LayoutChapters.md)

## Open questions

None recorded.
