# DeploymentStateLayout

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment screen state)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [DeploymentGrid_CommenceCheck](../functions/DeploymentGrid_CommenceCheck.md), [Battle_RebuildUnitTable](../functions/Battle_RebuildUnitTable.md), [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md), [Deployment_ResetState](../functions/Deployment_ResetState.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The fields of the deployment screen's state object that hold the capacity, the placed party, the candidate list and the unit being placed.

## Behavior

- V: +12 the current deployment area (0 or 1); +64 the capacity; +68..+87 five placed party indices (-1 = none); +88 the next field, zeroed at the start. No deployment function reads +88 by its own offset (the functions found reading +88 at that offset, sub_1401F5FAC and sub_1401F65E4, work on the map camera manager), but every loop over the placed array up to the capacity reaches it once the capacity is above 5.
- V: +1180 54 candidate entries of 12 bytes (first dword = roster index, -1 = none); +1828 the number of candidates (seen live: 7 with 7 party units, entries 0..6 = roster 0..6).
- V: +1840 the candidate under the carousel glove and +1844 the previous one; +1848 nine dwords, each a roster index (0..0x35) of a carousel card, matched against +1840 by sub_1401F2D80.
- V: +1884 a placement step written 0 by sub_1401F3EF4, 1 by Deployment_SelectTile (after storing the cursor tile at +1888..+1890), 2 by sub_1401F22D0 and 3 by sub_1401F5CEC; +1912 the roster index being placed and +1916..+1918 its tile and layer (Battle_JoinUnitAndLoad).
- I: the steps are choosing a tile (0), a tile chosen (1), the carousel open (2) and a placement done (3).
- I: +1832 is the first visible carousel row (the carousel shows 5 rows: +1832 + 4 is the last when there are 5 or more candidates).
- V: the fields after the placed array: the constructor (sub_1401EE21C) sets +84..+91 as one qword, clears +92..+99 and +100, and clears 1024 bytes from +104; Deployment_ResetState clears +88..+103; +96 is a dword the deployment's first step sets to 0 and sub_1401F2C50 requires to be 0 before it runs the numbering after commence (sub_1401F16F4); +100 is a byte sub_1401EE9B4 clears. No code of the deployment screen (0x1401EA000..0x1401F8000) reads +88..+95 through the state, so at most 7 placed indices fit before the live dword +96.

## Open questions

? the meaning of +96, +100 and the 1024 bytes at +104; ? the role of +1888 / +1889 (a remembered tile).
