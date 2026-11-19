# MovieStart

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a movie starts and ends: row read, controller flags, sound banks, subtitle window, skip rules.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Movie_Start](../functions/Movie_Start.md) | V | Reads the MovieData row: path, classic path, language track, sound bank, subtitle link and the three controller flags. |
| <a id="2"></a>2 | [MovieSound_LoadBank](../functions/MovieSound_LoadBank.md) | V | Loads the bgm, voice and se banks of the sound number. |
| <a id="3"></a>3 | [ClassicSubtitles_Step](../functions/ClassicSubtitles_Step.md) | V | Classic movies (link 192): per frame, finds the current line and its layout state. |
| <a id="4"></a>4 | [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) | V | Pause state machine when flag 0x20 is set and 0x08 clear. |
| <a id="5"></a>5 | [Boot_MovieFrame](../functions/Boot_MovieFrame.md) | V | Ends the boot movie by the skip rules. |

## Notes

Movies with skip_on_press end on one press of action 81 or 21; the enhanced story movies open the pause window.

## Open questions

? which screen plays the movies that end on one press.
