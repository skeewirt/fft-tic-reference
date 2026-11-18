# RangeOverlay_BuildRowMasks

- **Address:** `0x140389B50`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `short RangeOverlay_BuildRowMasks(int distance)`
- **Callers:** the range overlay setup
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 18 row words of the range overlay diamond for a given distance.

## Behavior

- V: for the three distance modes 0, 1, 2 the distance comes from two unit fields or their sum; 16 and above clears the overlay.
- V: for every row it takes the bit-run mask of the row's distance from the table (0x140693090), shifts it to the unit's column and stores the 18 resulting words; an optional pass removes bits outside the unit's lane.

## Referenced by

- Reads tables: [RangeRowMasks](../tables/RangeRowMasks.md)

## Notes

The table address is reached as an image-relative displacement, so the address does not appear as a plain operand.

## Open questions

?: the callers' exact screen.
