# JobLearnedBitsPointerIsBuiltFromTheUnitRecord

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [sub_14028A474](../functions/sub_14028A474.md), [JobAbilityList_Build](../functions/JobAbilityList_Build.md), [sub_140392620](../functions/sub_140392620.md), [sub_14028A8B0](../functions/sub_14028A8B0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The readers of a job's learned bits compute a pointer into the unit record (unit record + 123 + 3 * job index) and hand it to the bit reader, which reads 24 bits = 3 bytes.

## Behavior

- V (code): sub_14028ACD8, JobAbilityList_Build, sub_14028A474 and sub_140392620 each compute rec + 3 * (index + 41) (or + 0x36 * 3) and hand it to the bit reader (qword_143C49BF0 / qword_143C5C938), which reads 24 bits = 3 bytes.

## Open questions

None recorded.
