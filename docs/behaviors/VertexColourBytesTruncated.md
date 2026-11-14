# VertexColourBytesTruncated

- **Kind:** observed behaviour
- **Scope:** engine (UI node colours)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIImage_PS](../shaders/UIImage_PS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A UI node's vertex colour reaches the shader as bytes: each channel is the product of the node colour and its opacity, truncated to an integer. An opacity of 0.19999998807907104 on alpha 255 gives 50, not 51.

## Behavior

- V (frame t4): the floor's stone image (opacity 0.19999998807907104) fits a weight of 0.981 x 0.2 = 50 / 255 (least squares over 389043 pixels); with alpha 50 / 255 the floor model is 97.9 % exact, with 51 / 255 or the float 47.9 %.
- V: the node colour path combines bytes with integer truncation (sheet GUINode_ApplyAnimChannels: colour c = sampled * node byte / 255, truncating).

## Open questions

? the exact code that packs the vertex colour of a drawn quad (the multiply by opacity and the conversion to bytes).
