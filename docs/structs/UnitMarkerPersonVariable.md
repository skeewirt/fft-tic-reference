# UnitMarkerPersonVariable

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the UnitMarkerPersonVariables table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unit_marker"></a>`0x0` | unit_marker | `int16` | V | unit marker (the CharaName table key held in the party record) the pair belongs to; 0xFFFF ends the list |
| <a id="person_var"></a>`0x2` | person_var | `int16` | V | event variable id of that person (960 + position, 0x3CE .. 0x3F5 in this table); the value 12 is written into it when the dismissal is confirmed (the confirm is I) |

## Referenced by

- Described by tables: [UnitMarkerPersonVariables](../tables/UnitMarkerPersonVariables.md)

## Open questions

None recorded.
