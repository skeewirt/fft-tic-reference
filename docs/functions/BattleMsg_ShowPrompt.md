# BattleMsg_ShowPrompt

- **Address:** `0x1400EE908`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BattleMsg_ShowPrompt(void *a1, ...)`
- **Callers:** not enumerated (no xref list was read for this address)
- **Callees:** UIMessageBanner_Show (I), sub_140111B74 (twice)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a class 1 / subtype 27 message descriptor from a dword of the object and shows it in the banner; then calls sub_140111B74 twice.

## Behavior

- V: builds the descriptor {class 1, subtype 27, kind 0, word = the dword at a1+13592}.
- V: shows the descriptor; its class and subtype are the UIText_Get path in BattleMsg_TextFromDescriptor.
- V: then calls sub_140111B74 twice.
- I: the show call is UIMessageBanner_Show; the descriptor and the banner object are the ones that function takes, but the call was not read name by name.
- I: the name ShowPrompt and the prompt role are ours; nothing read shows which prompt it serves. The owner observation that the facing-direction prompt shares the banner bubble style does not attribute it to this function.

## State touched

- Calls: [UIMessageBanner_Show](UIMessageBanner_Show.md)

## Notes

The name is ours (IDB: sub_1400EE908). The function is 326 bytes.

## Open questions

What a1+13592 holds; what sub_140111B74 does and why it is called twice; which prompt uses this path.
