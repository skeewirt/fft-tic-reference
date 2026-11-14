# MovieController

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

ffto::Game::GameUI::MovieController (vtables 0x140702D20 and 0x140702D30): the movie host at *(qword_143CD9DC8) + 0xC8. Only the fields the skip path uses.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="movie_flags"></a>`0x18` | movie_flags | `uint32` | V | Set by Movie_Start from the MovieData (NXD 65) row: bit 0x20 = byte +36 (pause overlay on), 0x10 = byte +37 (skippable), 0x8 = byte +38 (skip handling off), bit 0 selects movie/half/ over movie/full/. | [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) |  |
| <a id="result_flags"></a>`0x1C` | result_flags | `uint32` | V | Cleared by Movie_Start; bit 0 set by MovieController_UpdateSkip when MovieControl state is 3 (skip taken). |  | [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) |

## Behavior

- I: MovieController_UpdateSkip is a virtual of the second vtable, so it receives the controller + 8 and reads these fields at +16 / +20 (consistent with Movie_Start writing +24 / +28 of the controller).

## Notes

Detail and evidence: the function sheets named on this page.

## Open questions

? The other fields.
