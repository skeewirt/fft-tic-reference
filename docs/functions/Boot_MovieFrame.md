# Boot_MovieFrame

- **Address:** `0x1402F2E40`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Boot_MovieFrame(void *boot)`
- **Callers:** sub_1400B5A7C
- **Callees:** Input_TestAction, sub_1400D8DDC, sub_14003ABD0, sub_14008757C, sub_14003E6D0, memmove, sub_14003E7C4, Boot_SetState, sub_1400D8B9C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame handler of the boot movie: ends it on the skip rules and copies the decoded frame into three textures.

## Behavior

- V: ends the movie when g_GlobalWork +100 is set; or, with movie flag 0x8 set, when action 81 or 21 fires and the pause manager's state is not 9; or, with flag 0x8 clear, when the controller's result bit 0 is set; or when the player time (+1468) is past +1464.
- V: ending calls Boot_SetState, destroys the MovieControl, sets flag 4 and calls sub_1400D8B9C.
- V: it also copies the decoded frame planes into three textures.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md)

## Referenced by

- Appears in flows: [MovieStart](../flows/MovieStart.md)
- Observed behaviours: [MovieSkipKinds](../behaviors/MovieSkipKinds.md)

## Notes

Name is ours.

## Open questions

? action 21 has no UIKeyAssign row in the stock data (action 81 is the confirm key).
