# BlendTermsRoundedSeparately

- **Kind:** observed behaviour
- **Scope:** GPU (the test machine's GPU and driver), UI draws into a layer target
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIImage_PS](../shaders/UIImage_PS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A UI draw's blend into its 8-bit target behaves as if both terms were rounded to 8 bits before they are added: result = round(source) + round(destination * (1 - source alpha)), not round(source + destination * (1 - source alpha)).

## Behavior

- V (frame t4, the floor: a solid rect (13, 12, 11): under the stone texture at alpha 50 / 255): the separate rounding reproduces 97.9 % of 389043 floor pixels exactly, one rounding 28.3 %. The destination term alone explains the game's integer offsets 10 / 10 / 9 (13, 12, 11 x 205 / 255 rounded).
- I: the same result comes from drawing the textured node into its own 8-bit layer and compositing it (store 1 then store 2); the two cannot be told apart on this frame. On the glove (drawn into a cleared target) both rules agree with the measured 99.4 %.
- V (studio, GameCompose.draw with this rule and the truncated vertex alpha): the whole frame t4 goes from 43.8 % to 93.3 % of pixels exact (header 99.9 %, floor 92.6 - 94 %).

## Open questions

? which of the two mechanisms the hardware uses (fixed-function blend arithmetic or an extra layer).
