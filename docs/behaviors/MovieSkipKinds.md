# MovieSkipKinds

- **Kind:** observed behaviour
- **Scope:** engine (movies)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [Movie_Start](../functions/Movie_Start.md), [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md), [Boot_MovieFrame](../functions/Boot_MovieFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Classic movies and the first four movies end on one press; the enhanced story movies open the pause window, from which they can be skipped.

## Behavior

- M: MovieData skip_on_press is 1 on movies 1..4 and the classic movies 16..22, 0 elsewhere; pausable and skippable are 1 on the enhanced movies 5, 6, 7 and 9..15 and equal on every row.
- M: the empty row 8 has all three flags 0.
- M: sound_bank is -1 on the classic movies and the empty row, and 0, 10, 20 .. 120 on the enhanced movies 1..15: a folder number, not a table key.

## Open questions

? which screen plays movies 1..4.
