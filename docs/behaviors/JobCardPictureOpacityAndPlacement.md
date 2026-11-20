# JobCardPictureOpacityAndPlacement

- **Kind:** observed behaviour
- **Scope:** engine (job card pictures)
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A job card (the painting behind the Status panel) is a 400 x 652 picture that is never fully opaque and fades out toward its lower left; its figure touches the top edge with the head left of the middle.

## Behavior

- V (data): the 38 stock cards are ui/ffto/icon/job_visual/texture/jv_NN_<m|f>_uitx, 400 x 652 with an alpha channel.
- M (2026-11-19, the 38 cards): the most opaque pixel is alpha 182 on 30 cards (up to 227 on the other 8). Taking the most opaque value any card has at each place, the opacity follows 215 + x / 2 - 0.54 y clipped to 0..182 (mean difference 9.8 of 255): full in the upper right, 0 at the lower left, about 40 to 85 along the lower right edge.
- M (the 38 cards): the figure starts in row 0 on every card; its rows 20..70 are 136 px wide in the median (quartiles 127 .. 170) and centred on x 188 (179 .. 194); its rows 150..330 span x 58 .. 316 in the median.

## Open questions

? whether the game adds a fade of its own when it draws the card.
