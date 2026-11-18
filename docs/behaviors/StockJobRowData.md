# StockJobRowData

- **Kind:** observed behaviour
- **Scope:** stock job-related table rows
- **Area:** [Job data](../areas/job-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Facts about the stock job rows of job.en, generaljob and jobtype: unused rows still carry numbers, the generic jobs map to texture part indices, and Ramza's jobs share the Squire's job type.

## Behavior

- V (data): `Job-en` has an empty name in 40 of the 174 rows: 0, 6, 10, 11, 14, 19, 24, 28, 29, 33, 35, 49, 53..59, 142, 143, 146..149, 152, 155..168. Those rows still hold numbers (an `exe.job` row, a `jobtype` id, a `jobcommand` id, a `TexturePartsIndex`), e.g. row 56: job type 34 (the Mystic's), command 16 (the Mystic's), texture parts 12. I: these are unused job slots; nothing in the stock game names a unit with them.
- V (data): the generic jobs 74..93 have `TexturePartsIndex` = id - 73 (Squire 1 .. Mime 20) and their own job types (Squire 1, Chemist 31, Knight 38, White Mage 32, Black Mage 33, Time Mage 44, Summoner 46, Mystic 34, Mime 59). Ramza's jobs 1, 2, 3 ('Squire', 'Squire', 'Gallant Knight') have job type 1 (the Squire's), commands 25 / 26 / 27 and `TexturePartsIndex` 21.
- V (data): `JobType` rows hold only two visual icon ids (`MaleVisualIconId`, `FemaleVisualIconId`); type 21 has 0 / 0 (no icon), as most types between 2 and 30.
- V (data): `GeneralJob` rows 0..19 are the generic jobs by index (job id - 74); rows 0 (Squire) and 1 (Chemist) have no requirement (empty `RequiredJobIds`); every row has the same `RequiredJobExp` [0, 100, 200, 400, 700, 1100, 1600, 2200, 3000].

## Open questions

None recorded.
