# GUIWidget_FindComponentByName

- **Address:** `0x1403F96CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIWidget_FindComponentByName(GUIWidget *w, element *name)`
- **Callers:** sub_1401BC92C (a dozen call sites), GUINode_DrawKind10 and others
- **Callees:** sub_140098898, sub_140098A58

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a component of the widget by its name key (component+280 name pointer, +288 hash): first in the widget's std::map at +136, then by a round-robin scan of the component vector at +104..+112; a vector hit is put into the map.

## Behavior

- V: returns 0 when the name string is empty (first char 0).
- V: map pass: the tree at w+136 is ordered by an unsigned int at node+32; the range of nodes whose key equals name+8 (the hash) is walked in order; a candidate (node+40) matches when its +512 is 0 and its name key equals `name` (hash compare when both nonzero, else string compare). The first match is returned.
- V: vector pass (no map hit): components are the 8-byte pointers w[104..112); the scan starts at index w+280 (a cached cursor) and wraps modulo the count; the first element with +512 = 0 and an equal name key is taken, the cursor is set to its index, and 0 is returned when none matches.
- V: after a vector hit it finds the element in the map by pointer (in-order walk), calls sub_140098898 on that position and then sub_140098A58 with (hash = comp+288, comp), i.e. it re-inserts the component into the map under its hash; the component is returned.

## Referenced by

- Called by: [ComponentEffects_Collect](ComponentEffects_Collect.md)

## Notes

The name is ours. Components whose +512 is nonzero are skipped; +512 is the hash of a second key (sub_1403F9938 matches it against its second name), so this function finds components whose second key is empty (I). The map acts as a lazily filled cache of the vector (I).

## Open questions

What sub_140098898 does (erase or hint) was not read; the meaning of the component keys at +280 and +504 (name and source?) was not determined.
