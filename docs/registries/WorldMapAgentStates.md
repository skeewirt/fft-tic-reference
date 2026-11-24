# WorldMapAgentStates

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [WorldMapAgent_SetState](../functions/WorldMapAgent_SetState.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

States of the world map UI agent (agent 20, state dword +228) set by WorldMapAgent_SetState: which of its addons each state shows and the footer guide it sets.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="hidden"></a>0 | `hidden` | `no guide` | V | Hides the main map, frame menu, Locations list and deep dungeon menu. |
| <a id="map"></a>1 | `map` | `guide from the main map` | V | Shows the main map and frame menu; hides the Locations list and the deep dungeon menu. |
| <a id="state 2"></a>2 | `state 2` | `guide 3006` | V | Shows the main map and frame menu; hides the Locations list. |
| <a id="locations list"></a>3 | `Locations list` | `guide 3002` | V | Shows the main map, frame menu and the Locations list (addon +80). |
| <a id="deep dungeon menu"></a>4 | `deep dungeon menu` | `guide 3005` | V | Shows the main map, frame menu and the deep dungeon menu (addon +96). |
| <a id="state 9"></a>9 | `state 9` | `no guide` | V | Hides all four; WorldMapAgent_IsMapShown still answers true in it. |

## Behavior

- V (seen live): the state reads 1 while the map is open with the list closed and 3 while the Locations list is open.
- V: every change calls vtable slot 25 of each addon with (new state, old state); the Locations list empties its records for any state but 3.

## Open questions

? states 5, 6 and 8 (they change only the frame menu).
