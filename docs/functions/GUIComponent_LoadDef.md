# GUIComponent_LoadDef

- **Address:** `0x1403F5764`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_LoadDef(UILoader *ld, int *rec, GUIWidget *w, GUIComponent *comp)`
- **Callers:** sub_1403F4BA8 (component instantiation)
- **Callees:** GUIComponent_LoadProps, sub_1403F5910, sub_1403F0654, sub_140402EDC, sub_140409684, sub_1403D8870, UIAnim_PlayStateTracks

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a runtime component from its UIB component record (0x40 bytes): property block, node tree, states.

## Behavior

- V: GUIComponent_LoadProps(ld, rec, w, comp) first.
- V: nodes: rec[5] entries of the node table at rec + rec[4]; entry k = int at table + 4k, the node at table + entry; each is built by sub_1403F5910 (-> GUINode_LoadTree) and linked into comp+272 in order.
- V: states: rec[7] records of 0x60 bytes at rec + rec[6]; a record of type 3 (timeline, +8) gets a state object found by its name (sub_140409684): frame count (+36) -> state+88, loop byte (+40) -> state+108, its names, then UIAnim_PlayStateTracks.
- V: every offset is a signed int added to the record's address, so a record may point backward.

## State touched

- Calls: [GUIComponent_LoadProps](GUIComponent_LoadProps.md), [UIAnim_PlayStateTracks](UIAnim_PlayStateTracks.md)

## Notes

The name is ours. The state records hold the arrow states Lock / Unlock / LockOnCursor / UnlockOnCursor that JobTree_SetArrowState plays; two components may share one state table (they target their layer by name).

## Open questions

What the record's last pointer (+36, an 8-byte block) holds (?).
