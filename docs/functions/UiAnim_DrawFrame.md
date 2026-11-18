# UiAnim_DrawFrame

- **Address:** `0x140342070`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UiAnim_DrawFrame(UiAnimState *anim, void *out)`
- **Callers:** sub_140342008, sub_140343110
- **Callees:** sub_1403406E8, sub_1402CCD48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Advances one widget animation by a frame and draws the sprite pieces of the frame set the current step names.

## Behavior

- V: the animation state holds a sequence index (+4); the sequence list table (0x140693A50) gives a list whose first dword is the step count and whose later dwords carry a frame set id in the low 16 bits and the step duration in the high 16 bits.
- V: the step counter (+16) increases each draw (unless a global pause bit, bit 27 of the world state dword, is set and the widget's own flag 0x800 is clear); when it reaches the step's duration the step number (+12) advances (wrapping to 0 at the end of the list) and the counter restarts; a duration of 0xFFFF holds the step for ever.
- V: the frame set pointer comes from the language's frame set table: language 0 uses 0x1406935E0, language 2 uses 0x140693E60, language 3 uses 0x1406942D0, every other language 0x140694740.
- V: for each piece (count from the frame set's first dword) the code turns the two piece dwords into one textured quad with the widget's screen offset; the frame sets for ids 41 and 42 use two extra offset lists (at 0x14071E9A0 and 0x14071E9A8) when they have four pieces.
- I: this is the draw step of the animated cursor and icon widgets.

## Referenced by

- Reads tables: [FrameSetsDefault](../tables/FrameSetsDefault.md), [FrameSetsLanguage0](../tables/FrameSetsLanguage0.md), [FrameSetsLanguage2](../tables/FrameSetsLanguage2.md), [FrameSetsLanguage3](../tables/FrameSetsLanguage3.md)

## Notes

Read: the whole function except the exact bit layout of the piece dwords.

## Open questions

?: the meaning of the piece dword bits; the two extra offset lists.
