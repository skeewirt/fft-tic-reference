# PanelSlideCurve

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14068489E`
- **Rows:** 12 rows of 2 bytes
- **Keyed by:** animation step 0..11
- **Read by:** [sub_140338A28](../functions/sub_140338A28.md)
- **Row layout:** [SlideCurveStep](../structs/SlideCurveStep.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Easing curve (symmetric, peak 144) a battle unit panel uses to slide a part of the panel in and out. Verdict: engine-data.

## Behavior

- V: sub_140338A28 (battle unit panel task): reads table[step] for steps below 10 into a primitive word; the candidate is the table start (the code adds 0x16 to the start of the preceding string-looking symbol)
- V: 12 words between two other word tables; reader bound: step < 10 then clamps; the shape is symmetric like the pop-up arc table of the event-scene batch but the values differ

## Notes

Our names. Tags: V values, I meaning.

## Open questions

- ?: whether the first value (100) is the rest position
