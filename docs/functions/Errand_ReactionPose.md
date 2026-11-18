# Errand_ReactionPose

- **Address:** `0x1402D2CEC`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int Errand_ReactionPose(int basePose, unsigned unitIndex)`
- **Callers:** `sub_140370414` (result scene unit setup)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses which reaction pose a unit shows in the errand result scene from its Brave, Faith and sex.

## Behavior

- V: Brave and Faith are each classed: below 36 gives class 0, 36..65 gives 1, 66..100 gives 2, above 100 gives 0.
- V: result = basePose + table[3 x faithClass + braveClass] + 3 when the unit is female (bit 7 of the record byte +4 clear).
- V: the table is the reaction matrix in the errand data block; a unit index of 54 or more falls back to a placeholder record.

## Referenced by

- Reads tables: [ErrandBlob](../tables/ErrandBlob.md)

## Open questions

None recorded.
