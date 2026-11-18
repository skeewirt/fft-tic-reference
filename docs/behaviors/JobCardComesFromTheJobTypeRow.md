# JobCardComesFromTheJobTypeRow

- **Kind:** observed behaviour
- **Scope:** engine (job card art on the Status screen)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobRecord_FillIconAndGenericFlag](../functions/JobRecord_FillIconAndGenericFlag.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The job card (the large faded painting behind the right half of the Status panel) is chosen by the job's JobType row, not by the job row's TexturePartsIndex (that is the small job icon): Job row +24 names a JobType row, whose MaleVisualIconId / FemaleVisualIconId name an Icon row holding the card's part file path.

## Behavior

- V (decompiled): JobRecord_FillIconAndGenericFlag reads the job row, then the JobType row (UI table 0xC8) by the job row's +24, and stores the icon id at out[0]: the female id for a record whose +8 byte is 0 or above, the male id otherwise.
- V (data): Icon rows 701..738 hold 'job_visual/textureparts/jv_NN_<m|f>_uitx.utexpt'; Icon rows 739.. are blank, JobType rows 115..124 are blank (0 / 0).
- V (file): a card part file is 93 bytes: a 0x20-byte header (u16 652 at +0x18 and 400 at +0x1C: the picture's height and width), the texture path, then 'TexturePart'; the u32 at +0x0C is the offset of 'TexturePart' counted from +0x0C. The texture is 400 x 652 RGBA: the figure's silhouette at about 70 % opacity (alpha at most 182), fading toward the lower left (about 215 + x / 2 - 0.54 y), clear outside the figure (measured over the 38 stock cards).
- V (seen live, owner 2026-11-17): Ramza shows no card in any job; a generic unit shows its job's card (the female Knight's for a female Knight).
- V (seen live): a job row naming another JobType showed that type's card; one naming a JobType whose Icon row has a new part file showed the new picture.

## Notes

The JobType id also feeds the per-type flag array and Job_SameJobType (see the field notes in data/jobs/fields.jsonl).

## Open questions

None recorded.
