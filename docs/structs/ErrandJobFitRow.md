# ErrandJobFitRow

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 22 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Job fit scores of one errand category or type row.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="column"></a>`0x0` | column | `uint8[22]` | V | Score per job column: job below 74 uses column 22 (reads the next row column 0), job 94 or above uses column 21, jobs 74..93 use 0..19; column 20 is never read. |

## Referenced by

- Described by tables: [ErrandJobFitCategory](../tables/ErrandJobFitCategory.md), [ErrandJobFitType](../tables/ErrandJobFitType.md)

## Open questions

None recorded.
