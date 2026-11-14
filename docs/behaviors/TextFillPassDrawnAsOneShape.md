# TextFillPassDrawnAsOneShape

- **Kind:** observed behaviour
- **Scope:** UI text (SDF font runs: the screen title, the job name tag, the level boards)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SDFFontRenderer_Flush](../functions/SDFFontRenderer_Flush.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A text run's fill pass reaches its target as one shape: the fill glyphs are drawn without blending under a depth test (LESS_EQUAL, depth = 1 - the distance at the pixel centre), so where neighbouring glyph quads overlap the glyph with the largest distance keeps the pixel; the result is composited once. The shadow pass is blended glyph by glyph.

## Behavior

- V (code, function SDFFontRenderer_Flush and the five program entries of shader/SDFFont.tec): the glyph pass with program 1 has blending off and depth test + write LESS_EQUAL, the fill pixel shader is the only one that writes SV_Depth (= 1 - d); the glyph pass with program 0 blends straight alpha without depth. I: program 1 is the fill and program 0 the shadow (shader lists in file order).
- V (studio): choosing the winner by the centre distance (a later glyph on a tie) gives the same frames as choosing by the most coverage.
- V (frame t4, the 'Squire' name tag: every draw of the tag layer replayed offline against the capture): per-glyph blending 0.084 mean / max 33 at the touching serifs of u-i, r-e, q-u; the run's fill as one shape with the maximum coverage per pixel 0.011 / max 2 (the shadows too as one shape) and in the studio 0.004 / max 1 with the shadows per glyph.
- V (studio, the three text regions of frame t4 and the Archer frame): fills as one shape, shadows per glyph: title 0.056 / max 18 -> 0.034 / max 1, name tag 0.101 / max 33 -> 0.004 / max 1, Lv board 0.083 -> 0.081, chips 0.037 -> 0.036; Archer frame name tag 0.057 -> 0.015. Worse: the shadows as one shape as well (title 0.086), the fills blended with a MAX operation (title 1.07), the first or the last glyph winning an overlap (> 1.6), the maximum taken on the distances before the coverage curve (title 0.049, tag 0.050 / max 23).

## Open questions

? where the fill target is composited (program 2's quad is issued before the batch's glyph draws in SDFFontRenderer_Flush); ? the depth format.
