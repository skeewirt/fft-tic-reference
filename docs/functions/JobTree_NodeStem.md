# JobTree_NodeStem

- **Address:** `0x140134980`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `const char *JobTree_NodeStem(JobTreeAddon *addon, int treeIndex)`
- **Callers:** JobTree_RefreshAddon (4 call sites)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tree index -> UIB node-name stem. The stem is the name of the job's panel node and the `A`/`B` parts of arrow names `Line<A><B>`.

## Behavior

- V: id = index + 74; 74 Squire, 75 Chemist, 76 Knight, 77 Archer, 78 Monk, 79 White, 80 Black, 81 Time, 82 Summoner, 83 Thief, 84 Orator, 85 Mystic, 86 Geomancer, 87 Dragoon, 88 Samurai, 89 Ninja, 90 Arithmetician, 91 Bard, 92 Dancer, 93 Mime; anything else returns the default Str1.

## Referenced by

- Called by: [JobTree_RefreshAddon](JobTree_RefreshAddon.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

V: a leaf that writes only rax and edx; the caller at 0x140133A42 reads the arrow's level back from ecx after the call.

## Open questions

None recorded.
