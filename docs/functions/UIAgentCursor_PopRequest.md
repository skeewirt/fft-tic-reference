# UIAgentCursor_PopRequest

- **Address:** `0x1401D2A10`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentCursor_PopRequest(UIAgentCursor *agent)`
- **Callers:** sub_140188080, sub_140188428
- **Callees:** UIAgentCursor_Show, UIAgentCursor_Hide

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes the last cursor request off the agent's request stack and applies it: mode, rest offset, static flag, show or hide.

## Behavior

- V: the stack is a vector of 16-byte entries at agent+104 .. +112 (end of storage +120). With an empty stack: agent+72 (mode) = 0, UIAgentCursor_Hide and, when the addon exists, the rest offsets agent+80 / +84 = 0.
- V: otherwise the last entry is removed and applied: agent+72 = entry int +0 (mode), agent+80 / +84 = entry ints +4 / +8 (the offsets GUICursorHand_Update adds to the focused node's rect), agent+132 = entry byte +13 (static flag). Mode 1 or 2 calls UIAgentCursor_Show; any other mode sets agent+72 = 0, hides and clears the offsets.
- V: when the entry's byte +12 is set, UIAgentCursor_Show is called once more unless the cursor widget is already active.

## State touched

- Calls: [UIAgentCursor_Show](UIAgentCursor_Show.md), [UIAgentCursor_Hide](UIAgentCursor_Hide.md)
- Reads: [UIAgentCursor.requests_begin](../structs/UIAgentCursor.md#requests_begin)
- Writes: [UIAgentCursor.mode](../structs/UIAgentCursor.md#mode), [UIAgentCursor.offset_x](../structs/UIAgentCursor.md#offset_x), [UIAgentCursor.offset_y](../structs/UIAgentCursor.md#offset_y), [UIAgentCursor.static_mode](../structs/UIAgentCursor.md#static_mode)

## Notes

The name is ours (IDB: sub_1401D2A10). It answers where hand+80 / +84 of GUICursorHand_Update come from: the entries of this stack.

## Open questions

? The function that pushes entries was not found (no add of 16 to agent+112 in the code); so which request the Job Tree's hand uses (offsets, mode) is not read.
