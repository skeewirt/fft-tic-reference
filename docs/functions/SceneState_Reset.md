# SceneState_Reset

- **Address:** `0x1402D3918`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneState_Reset(void)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the shared scene state before a legacy scene and installs its menu node arrays.

## Behavior

- V: clears a long list of scene words, resets the face display state, the dialogue face slots and the event skip words.
- V: when the chara render manager exists stores pointers to seven nodes (stride 88) from slot 126, from 0x1408F2C10 (language 0) or 0x1408F2E80, then from 0x1408F30F0 two nodes, then seven nodes from slot 133 (0x1408FA5F0 or 0x1408FA890) and two from 0x1408FAB30.

## Referenced by

- Called by: [Game_MainLoop](Game_MainLoop.md), [TitleScene_Start](TitleScene_Start.md), [sub_1401839E4](sub_1401839E4.md)
- Reads tables: [SceneMenuNodesADefault](../tables/SceneMenuNodesADefault.md), [SceneMenuNodesALanguage0](../tables/SceneMenuNodesALanguage0.md), [SceneMenuNodesBDefault](../tables/SceneMenuNodesBDefault.md), [SceneMenuNodesBLanguage0](../tables/SceneMenuNodesBLanguage0.md)

## Notes

Read to the end of the node installation (1671 bytes).

## Open questions

?: the cleared words one by one.
