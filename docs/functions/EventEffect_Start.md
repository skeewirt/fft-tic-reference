# EventEffect_Start

- **Address:** `0x140273708`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventEffect_Start(unsigned int effectWord, int flag, int64_t unused, char flagByte)`
- **Callers:** sub_14023A0B4
- **Callees:** Effect_SelectForAbility

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the effect an event script asked for: builds a small request record, fills its flag bytes and calls Effect_SelectForAbility with the effect word.

## Behavior

- V: builds a request record whose first word is 1, with bytes +3..+231 zeroed; stores the fourth argument at record byte +8 and, when the second argument is nonzero or the effect word is 220, at byte +200.
- V: calls Effect_SelectForAbility(0, effect word, record); the effect word is passed unchanged as an int.
- V: its only code caller is the event effect starter sub_14023A0B4, which reads the word at 0x140D40930 with a sign extension and passes it on (the address is the caller's: this body never touches it).

## State touched

- Calls: [Effect_SelectForAbility](Effect_SelectForAbility.md)

## Notes

The two flag arguments come from a byte of the event state and from a word test of the scene.

## Open questions

What the request record's other bytes carry.
