# Battle_ResolveReaction

- **Address:** `0x140283C00`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_ResolveReaction(void *unit, const void *action, const void *targets)`
- **Callers:** none found
- **Callees:** memcpy, BattlePreview_BuildAction, BattleAction_GetRangeInfo, Battle_ResolveAction, sub_14030A410

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves a reaction or secondary action: it copies the action, rebuilds the preview and range, calls the action resolver and then the reaction bookkeeping.

## Behavior

- V: the unit action block is at unit +0x1A0; the twenty-byte action is copied twice, once from the caller and once from the target list.
- V: it clears a global byte, calls BattlePreview_BuildAction and sets the state word at 0x14186AF80 to 2.
- V: BattleAction_GetRangeInfo is called on the target block and a result of -1 aborts with the failure return.
- V: it reads the unit action record through the ability record and copies the range/area fields.
- V: Battle_ResolveAction is the resolver called with the twenty-byte action and the target array.
- V: the reaction bookkeeping function 0x14030A410 runs after the resolver and the battle context word is restored.
- V: it has no direct call site in the image; the reaction dispatch reaches it through a stored pointer or a computed target.
- I: this is the reaction path of the action resolver, because it is the second of the three Battle_ResolveAction call sites.
- ?: how the reaction pointer is installed; no data reference to this address was found.

## State touched

- Calls: [BattlePreview_BuildAction](BattlePreview_BuildAction.md), [BattleAction_GetRangeInfo](BattleAction_GetRangeInfo.md), [Battle_ResolveAction](Battle_ResolveAction.md)

## Notes

Whole function read (545 bytes). The missing direct caller is a fact; the dispatch route is inferred from the list of Battle_ResolveAction call sites.

## Open questions

None recorded.
