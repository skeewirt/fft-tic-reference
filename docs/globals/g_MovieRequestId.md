# g_MovieRequestId

- **Kind:** global
- **Address:** `0x142E7FB04`
- **Type:** `int32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

MovieData id of the movie to play, -1 none: Boot_UpdateVideo passes it to Movie_Start; Video_RefreshState resets it to -1; the opening tasks test it (I: 'requested / playing movie' from those uses).

## Referenced by

- Read by: [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md), [OpeningTask_0](../functions/OpeningTask_0.md), [OpeningTask_1](../functions/OpeningTask_1.md), [OpeningTask_10](../functions/OpeningTask_10.md), [OpeningTask_9](../functions/OpeningTask_9.md), [TitleScene_DemoReturn](../functions/TitleScene_DemoReturn.md), [TitleScene_NewGameHandoff](../functions/TitleScene_NewGameHandoff.md)

## Open questions

None recorded.
