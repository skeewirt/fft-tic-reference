# EventNode_PlayShow

- **Address:** `0x14013BA64`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `char EventNode_PlayShow(uint64_t node)`
- **Callers:** EventScript_Run, case 0xC4 (call site 0x14023E342), and sub_140181914 (call site 0x140181974).
- **Callees:** UIName_Key, GUINode_FindState, GUINode_PlayState, `sub_1403D8D1C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When a global byte is set, marks a UI node and plays its Show state.

## Behavior

- V: does nothing unless the byte at the global object qword_140C69690 +23 is nonzero.
- V: sets byte +416 of the GUI object at +48 of the node to 1.
- V: builds the key 'Show' with UIName_Key and finds that state with GUINode_FindState on the GUI object at +48.
- V: when the state is found, it sets the state's byte +104 to 1 and calls GUINode_PlayState on it.
- V: when the key's interned id is nonzero, it releases the id with sub_1403D8D1C on qword_143CDA2A0.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Open questions

What the byte at qword_140C69690 +23 is, and what sets it.
