# MusicTrackFilesAreOpenedByNameThroughTheFileManager

- **Kind:** observed behaviour
- **Scope:** engine (music)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventMusic_LoadTrack](../functions/EventMusic_LoadTrack.md), [sub_14034004C](../functions/sub_14034004C.md), [sub_14033FE00](../functions/sub_14033FE00.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A music change queued on the audio command queue ends in EventMusic_LoadTrack, which builds the file name sound/music/music_NNNNN.sab from the track number (the music id minus 1) and opens it through the game's file manager by that path.

## Behavior

- V (seen live): queuing kind 1 with the parameter of id 5 in slot 2 made the queue service load track 4 on channel 8.
- V (seen live): loading a track not already held passes the path sound/music/music_NNNNN.sab to the file manager's path resolver.

## Notes

Seen 2026-11-16 on the Steam PC build.

## Open questions

None recorded.
