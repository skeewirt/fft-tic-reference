# JobTreeCursorNeighbourTable

- **Kind:** observed behaviour
- **Scope:** engine (Job Tree)
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [JobTree_RefreshAddon](../functions/JobTree_RefreshAddon.md), [JobTree_HandleInput](../functions/JobTree_HandleInput.md), [JobTreeNavRecord](../structs/JobTreeNavRecord.md), [JobTreePanel](../structs/JobTreePanel.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Job Tree pad cursor does not search the screen for the nearest panel: each job row of the GeneralJob table names, for each of eight pad directions, up to two panels to move to. The 16 columns and 16 flag bytes that look like arrow slots are this table; the arrows come from the requirement lists.

## Behavior

- V: JobTree_RefreshAddon copies, for each of the 20 panels, the 8 directions x 2 candidates x {panel byte, flag byte} from the job's GeneralJob row into the panel record at +0x1A8 (32 bytes, struct JobTreeNavRecord).
- V: JobTree_HandleInput builds the direction from two groups of four input bytes of the input module (+13648..13651 and +13652..13655, each ordered down, left, up, right): 0 up, 1 up-right, 2 right, 3 down-right, 4 down, 5 down-left, 6 left, 7 up-left.
- V: the first group wins; the second group is used only when the first gives no direction, and then a candidate whose flag byte is non-zero is skipped. A candidate equal to the hidden gender panel (17 or 18, chosen by addon +12240) is skipped in both cases. The first accepted panel index below 20 gets the focus; 20 means none.
- I: the second group is the 'held' or the 'pressed' state of the same four directions; which one was not decided (the bytes are filled from the per-action rows of the input module).

## Open questions

? which of the two input groups is the held state and which the pressed state.
