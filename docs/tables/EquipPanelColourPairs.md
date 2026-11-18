# EquipPanelColourPairs

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F3710`
- **Rows:** 11 rows of 4 bytes
- **Keyed by:** colour row 0..10
- **Read by:** [sub_14032B1A4](../functions/sub_14032B1A4.md)
- **Row layout:** [ColourPair](../structs/ColourPair.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Gradient colour pairs of the result panel, one colour per variant. Verdict: designer-data.

## Behavior

- V: sub_14032B1A4 (result panel task): fills 4 colour words from rows 0..3 and 7 from rows 4..10 with a stride of two words, starting at word variant (0 or 1)
- V: reader loops of 4 and 7 with a 4-byte stride starting at 2 x variant; 0x30 bytes of colours, then rectangle data from 0x1408F3740

## Notes

Our names. Tags: V reads, I that it is gradient colours.

## Open questions

None recorded.
