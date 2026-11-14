# SceneUnit_AddPosition

- **Address:** `0x140272F04`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_AddPosition(int16_t slot, const uint16_t *delta)`
- **Callers:** SceneUnit_ZeroPosAndReset (SceneUnit_ZeroPosAndReset) and EventObject_MoveWorker.
- **Callees:** SceneObject_FindBySlot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds a three-word delta to the position words of the unit node for a slot.

## Behavior

- V: finds the unit node for the slot with SceneObject_FindBySlot; when there is none it returns 0.
- V: adds the delta words 0, 1 and 2 (16-bit) to the node words at +108, +110 and +112 respectively.
- V: returns 1.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [SceneUnit_ZeroPosAndReset](SceneUnit_ZeroPosAndReset.md)

## Notes

The delta pointer is in the second argument register.

## Open questions

None recorded.
