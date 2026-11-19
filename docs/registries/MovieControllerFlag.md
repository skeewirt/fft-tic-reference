# MovieControllerFlag

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The movie controller flag bits Movie_Start sets from the MovieData row (MovieController +24).

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="pausable"></a>32 | `pausable` | `MovieData pausable (+0x24)` | V | Runs the pause state machine (pause window, resume or skip). |
| <a id="skippable"></a>16 | `skippable` | `MovieData skippable (+0x25)` | V | The movie can be skipped from the pause window (MovieControl +25). |
| <a id="skip_on_press"></a>8 | `skip_on_press` | `MovieData skip_on_press (+0x26)` | V | No pause window: a press of action 81 or 21 ends the movie. |
| <a id="ended"></a>4 | `ended` | `set by Boot_MovieFrame` | V | Set when the boot movie is ended. |

## Behavior

- V: MovieController_UpdateSkip runs the skippable publish and the pause state machine only when 0x08 is clear.

## Notes

Struct MovieController (records_skip) holds the flags at +0x18.

## Open questions

None recorded.
