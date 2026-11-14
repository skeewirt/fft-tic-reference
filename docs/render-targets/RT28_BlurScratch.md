# RT28_BlurScratch

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 28
- **Size:** output size
- **Format:** `R8G8B8A8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scratch target of the UI blur's horizontal pass (UIBlur_Run gets 28 as its scratch index from the drop-shadow pass).

## Behavior

- V: GUILayer_BlurShadowPass passes scratch index 28 to UIBlur_Run; RT 28 is RGBA8 (live resource list).
- V (capture): the horizontal result is stored at 8 bits before the vertical pass reads it.

## Open questions

None recorded.
