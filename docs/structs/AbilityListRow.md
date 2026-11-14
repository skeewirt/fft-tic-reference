# AbilityListRow

- **Kind:** structure
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 8-byte row of the job screen's ability page: word 0 job id, word 1 ability id with flag bits; the list ends with {0, 0xFFFF}.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by |
|---|---|---|---|---|---|
| <a id="job_id"></a>+0 | job_id | `uint16` | V | Job the row belongs to; sub_14028A474 stores the tab's job id, sub_14028A8B0 stores the unit's job for the first row of a tab. | [sub_14028A474](../functions/sub_14028A474.md) |
| <a id="ability_word"></a>+2 | ability_word | `uint16` | V | Ability id with 0x1000 (known), 0x4000 (not learnable / already known) or 0x6000 (hidden), set by sub_14028A474 (0x14028A61B-0x14028A678) and sub_14028A8B0 (0x14028A9F7-0x14028AA06). | [sub_14028A474](../functions/sub_14028A474.md) |
| <a id="padding"></a>+4 | padding | `uint32` | V | Zero; the row is moved as a qword by the sorter (0x14028AB74-0x14028AB7F). |  |

## Behavior

- V: the row is an address-taken record: sub_14028A8B0 swaps whole qwords, so the flag bits travel with the id, while the sort key masks the id.
- V: sub_14028A8B0 de-duplicates on the raw ability word, so the same id with different flags is kept twice.

## Notes

V: see the sheets sub_14028A474, sub_14028A8B0 and JobScreen_BuildJobTabRows.

## Open questions

? who reads 0x1000 / 0x4000 / 0x6000 on these rows; the consumers are outside the exported set.
