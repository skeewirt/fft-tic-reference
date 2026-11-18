# JobChangeTransitionShapeFromTheListEntryByte

- **Kind:** observed behaviour
- **Scope:** engine (Change Job transition sprite)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md), [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

While a job change plays its light pillar, the Status header figure is drawn in a shape JobScreen_UpdateState asks Unit_ResolvePreviewShape for, passing the Change Job list entry's job as one byte; for a generic unit that shape is the character byte + 2 x (job + 38), one byte.

## Behavior

- V (disassembly): at 0x140368F9A JobScreen_UpdateState loads r8b from g_RuntimeJobList (2 bytes an entry) at the list cursor and calls Unit_ResolvePreviewShape (unit, outPalette, job); the result's low byte is stored as the shape.
- V (decompiled): Unit_ResolvePreviewShape reads jobs 92 and 93 one lower; for character byte 0x80 / 0x81 it answers the character + 31 for job 160, + 33 for 161 and 164, else the character + 2 x (job + 38); a named character (below 0x80) gets its own byte; 0x82, 0xA2..0xA9 and 0xA5 have rows of their own.
- V (seen live 2026-11-17): a list entry whose job id is 300 was drawn during the pillar as the figure of job 44 (300's low byte): a grey-haired figure in purple and gold; after the pillar the Status figure is drawn by its own path.

## Open questions

None recorded.
