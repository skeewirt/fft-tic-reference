# NxdDataAchievementRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.achievement table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="telemetry_achievement"></a>`0x4` | telemetry_achievement | `int32` | M | Measured over every stock row: Every value is a key of nxd.TelemetryAchievement-en. Observed in the stock rows: 0 to 1049, 51 distinct values. |
| <a id="counter"></a>`0x8` | counter | `int32` | V | Read in the code: Id of the UserSituation counter that the counter-type achievements test (value read from g_UserSituation +24 + 4*id, or +104 + 4*id when the bank bit of +16 is set). Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="threshold"></a>`0xC` | threshold | `int32` | V | Read in the code: The counter achievement is earned when the counter named by +8 is at least this value; 0 never earns. Observed in the stock rows: 0 to 2040, 8 distinct values. |
| <a id="book"></a>`0x10` | book | `int32` | V | Read in the code: The achievement of class AchievementOtherNovel is earned when a NovelReadThroughNotification arrives whose book id equals this value (a Book key: the book read to the end). Observed in the stock rows: 0 to 4, 2 distinct values. |
| <a id="event_id"></a>`0x14` | event_id | `int32` | V | Read in the code: The achievement of class AchievementOtherJournal is earned when a JournalNotification arrives whose value equals this one; that value is the Journal row's +0x18 (the scene started from the Chronicle's Events list). Observed in the stock rows: 0 to 159, 2 distinct values. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 51 distinct values, 1 empty. |

## Referenced by

- Described by tables: [NxdDataAchievement](../tables/NxdDataAchievement.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 7 columns not decoded.
