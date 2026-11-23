# UIAgent_IsActive

- **Address:** `0x1401D15B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool UIAgent_IsActive(UIAgentBase *agent)`
- **Callers:** agent vtables, slot 2 (base 0x140713238; System 0x14070DF00, Title 0x14070A5B0, SaveLoad 0x14070DE48); the base plus 54 agent vtables, 55 slots in all, no direct call site
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Base virtual slot 2: true while the agent's add-on list is non-empty.

## Behavior

- V: returns 1 when `addons_begin` (+0x10) differs from `addons_end` (+0x18), else 0. Only those two pointers are read.
- V: it is base vtable slot 2 (0x140713238 + 0x10); every agent vtable in the build repeats it at the same slot.
- M: the IDB records 55 data references to this function, one per vtable (the base plus 54 agent vtables), and no direct call site; all uses go through the vtable.
- I: "active" therefore means "at least one add-on attached", not "shown" and not "state is non-zero"; an agent with an empty list reads inactive even when it has a state machine (rests on AttachAddon/DetachAddon maintaining this vector and on no other field being read).
- ?: whether a false result is what makes a caller skip an agent's per-frame work was not traced.

## State touched

- Reads: [UIAgentBase.addons_begin](../structs/UIAgentBase.md#addons_begin), [UIAgentBase.addons_end](../structs/UIAgentBase.md#addons_end)

## Referenced by

- Appears in flows: [UIAgentLifecycle](../flows/UIAgentLifecycle.md)

## Notes

12 bytes: two loads and a compare. Every agent vtable in this build inherits the base implementation unchanged; no derived agent overrides slot 2.

## Open questions

The manager-side use: whether a false result stops an agent's frame work.
