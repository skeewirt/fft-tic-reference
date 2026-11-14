# JobTreePanelCountLimits

- **Kind:** observed behaviour
- **Scope:** engine (Job Tree)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_RefreshAddon](../functions/JobTree_RefreshAddon.md), [JobTreeAddon](../structs/JobTreeAddon.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What bounds the number of Job Tree panels: the immediate widths of the count and cap compares, the render slots 80 + panel and the per-panel arrow capacity.

## Behavior

- V: the tree addon has 6 count sites (the panel count, 20) and 13 cap sites (19); 4 of the 6 count sites (0x140133941, 0x140133D6F, 0x1401340DF, 0x140368B15) and all 13 cap sites are compares with an 8-bit immediate (the other two count sites load a 32-bit immediate), and an imm8 is sign-extended, so those compares hold values up to 127 only.
- V (executable bytes, 2026-11-08): all 17 one-byte sites are compares with a sign-extended 8-bit immediate; an immediate of 0x80..0xFF compares as -128..-1 (the signed loops end after one pass, the unsigned caps bound nothing).
- V: panel storage is linear: panel nodes at +72 with stride 456, panel records (148 bytes) after them, then a 96-byte tail; the object is allocated by an operator new whose size immediate is one of those sites.
- V: JobTree_SetPanelRecord gives panel p the render slot 80 + p (store of v4 + 80 into the record at +92) and CharaRender_SetSlotRequest refuses slot numbers above 255, so panels 0..175 can hold a sprite; the job-change cells use 61 + cell.
- V: the final loop of JobTree_FillJobRecords draws 6 arrows per panel (6 requirement slots) over a panel count compare against the immediate 0x14; JobTree_RefreshAddon gives each panel 4 label boards.
- V: a panel's content is chosen by list position, not by job id: JobTree_SetPanelRecord stores a record in panel `pos` (+1 for jobs 92 and 93).
- V: every panel needs its own node set in the layout file ffto_job_tree.uib under a stem name (JobTree_NodeStem answers a fixed table for 0..19 and the empty string above).
- ?: the number of nodes or the file size the layout loader accepts was not measured.

## Open questions

None recorded.
