# JobTreePanelSprite

- **Kind:** observed behaviour
- **Scope:** the unit sprite of every Job Tree panel
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md), [PreviewUnit_BuildRecord](../functions/PreviewUnit_BuildRecord.md), [JobList_Build](../functions/JobList_Build.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Each panel shows the viewed unit as that job: the generic sheet of the unit's gender for the 20 tree jobs, the unit's own sprite for its own special job (Ramza's Squire panel). A female unit's Bard panel is the Dancer.

## Behavior

- V: JobTree_FillJobRecords computes the panel's shape inline for the jobs 74..93: jobs 92 and 93 count as 91 and 92, then shape = 2 * job - 52 + female, female = bit 6 of the viewed unit's byte +6. So Squire is shape 96 / 97, Bard 130 (male), Dancer 131 (female), Mime 132 / 133.
- V: any other job id (a story unit's own job, such as Ramza's Squire job) takes Unit_ResolvePreviewShape, which returns a story unit's marker itself: Ramza's own sprite (shape 1 for the chapter-1 sheet).
- V: the list's first entry is the unit's own base job, so for Ramza the Squire panel shows Ramza and every other panel the generic male sheet; for a generic unit every panel, the Squire too, shows the generic sheet of its gender.
- V: JobList_Build lists job 91 (Bard) or 92 (Dancer) by the unit's gender, so the Bard panel is the Dancer for a female unit.
- V: the HD sheet of a shape is the dword table at 0x1407151F0 (first g2d entry of the sheet pair: shape 1 -> 830, 96 -> 992, 97 -> 994, ..., 133 -> 1066); the colours come from the job's classic sheet.
- V (retail frames): the generic Squire's classic sheet is mina_m / mina_w (both match, see below); the 10m / 10w sheets are civilians.
- V: the palette is recoloured per shape before the atlas is built (CharShape_ApplyClut / CharClut_ApplyToPalette): Ramza's shapes carry CharShape charclut+Id 1, and every enabled CharCLUT row of key 1 replaces the 16-colour block numbered by its second key (Key2) with its RGB triples packed to RGB555. Without it the hovered Ramza differs by 0.8 mean in green and blue (frame t4); with it 0.042 mean, max 2 (91 % exact), which also settles the block index as Key2.
- V (retail frame, 2026-10-30): a generic male unit's Squire panel shows the generic Squire. A generic female unit's Dancer panel, black (nobody has it), is the female Dancer silhouette.

## Notes

Verified for a generic male and a generic female unit; Ramza by the earlier frame t4.

## Open questions

? Which shapes Ramza's later chapters use (shapes 2..4 point at the sheets 832..836).
