# g_UIStateFade

- **Kind:** global
- **Address:** `0x143CD9E00`
- **Type:** `object *`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UI state and fade object: +16 float fade timer (the title's actions wait for it to reach 0 or less), +24 the requested state; a transition is started with the state change helper on obj + 16. States the title writes: 6 (fade out) and 19.

## Referenced by

- Read by: [Boot_Frame](../functions/Boot_Frame.md), [Boot_SetState](../functions/Boot_SetState.md), [Boot_Update](../functions/Boot_Update.md), [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md), [Game_MainLoop](../functions/Game_MainLoop.md), [OpeningScene_Start](../functions/OpeningScene_Start.md), [OpeningTask_10](../functions/OpeningTask_10.md), [TitleScene_Start](../functions/TitleScene_Start.md), [TitleScene_Task](../functions/TitleScene_Task.md), [TitleScene_Update](../functions/TitleScene_Update.md), [UISaveLoad_Open](../functions/UISaveLoad_Open.md), [UISaveLoad_StateEnter](../functions/UISaveLoad_StateEnter.md), [UISaveLoad_StateSourcePick](../functions/UISaveLoad_StateSourcePick.md)
- Written by: [Boot_SetState](../functions/Boot_SetState.md), [Boot_Update](../functions/Boot_Update.md), [OpeningTask_10](../functions/OpeningTask_10.md), [TitleScene_Start](../functions/TitleScene_Start.md), [TitleScene_Task](../functions/TitleScene_Task.md), [TitleScene_Update](../functions/TitleScene_Update.md), [UISaveLoad_Open](../functions/UISaveLoad_Open.md), [UISaveLoad_StateSourcePick](../functions/UISaveLoad_StateSourcePick.md)

## Open questions

None recorded.
