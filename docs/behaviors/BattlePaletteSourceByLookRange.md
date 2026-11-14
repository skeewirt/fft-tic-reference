# BattlePaletteSourceByLookRange

- **Kind:** observed behaviour
- **Scope:** engine (battle palette row)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_14026EB74](../functions/sub_14026EB74.md), [LookQueue_Add](../functions/LookQueue_Add.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where a battle unit's palette row comes from depends on its sprite number: the generic looks (96..133) and 159..162 take the unit's byte +4, every other look its CharShape row's colour override or the queue palette.

## Behavior

- V: sub_14026EB74 tests the sprite word against 159, 160, 161, 162 and sprite - 0x60 <= 0x25; those take unit byte +4 (the queue's palette word when there is no unit) with a limit of 5.
- V: other sprites read CharShape row (key = the sprite): a non-zero +12 gives sub_1401E3A10's value with a limit of 16, else the queue palette with a limit of 5; the scene unit's +0xB gets the value when below the limit, else 0.
- M (unicorn): sprite 101 takes the unit-byte branch, 60 and 200 the CharShape branch.

## Open questions

None recorded.
