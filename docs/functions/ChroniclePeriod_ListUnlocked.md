# ChroniclePeriod_ListUnlocked

- **Address:** `0x1401E572C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ChroniclePeriod_ListUnlocked(int *out)`
- **Callers:** not recorded
- **Callees:** UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lists the Chronicle periods that are unlocked.

## Behavior

- V: walks every UIChroniclePeriod row by index and keeps the first key (not 0) of each row whose user_situation (+0xC) is non-zero and met, up to 50 entries, into a2 (a count qword, then a dword list).

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md)

## Referenced by

- Called by: [ChronicleTimeline_Setup](ChronicleTimeline_Setup.md)

## Open questions

None recorded.
