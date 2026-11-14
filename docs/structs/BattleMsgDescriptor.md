# BattleMsgDescriptor

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 4-dword descriptor the banner takes: class, subtype, kind and a message word. The banner resolves it to a template through a class/subtype switch; class 0 subtype 2 turns the kind and the word's low 11 bits into a table-172 message id, class 1 subtype 27 is a UI text id and class 1 subtype 171 a table-172 key.

## Fields

| Offset | Field | Type | Conf | Meaning | Indexed by registries |
|---|---|---|---|---|---|
| <a id="class"></a>`0x0` | class | `uint32` | V | 0 or 1 in the studied code. The text resolver switches on this together with the subtype (V, decompile). |  |
| <a id="subtype"></a>`0x4` | subtype | `uint32` | V | 2 (event-script message id), 27 (UI text id) or 171 (direct table-172 key) in the studied code (V, decompile). |  |
| <a id="kind"></a>`0x8` | kind | `uint32` | V | Message kind. For class 0 subtype 2 it is the multiplier of the 1000-wide message-id base; only the kinds in registry BattleMsgKindBase give an id (V, decompile). | [BattleMsgKindBase](../registries/BattleMsgKindBase.md) |
| <a id="word"></a>`0xC` | word | `uint32` | V | Message word, read as a u16 and masked with 0x7FF: the row index below the kind's base, or a table-172 key for class 1 subtype 171 (V, decompile and live trace). | [BattleMsgKindBase](../registries/BattleMsgKindBase.md) |

## Behavior

- V (live trace 2026-10-31, tracepoint on the banner function, one call during an ability cast): {0, 2, 10, 0x5062}, enable 1.
- V (decompile): 0x5062 packs group 10 in bits 11 and up and index 98 in the low 11 bits, an event-script message.
- ?: whether the traced call was produced by the ability cast. The code that builds the banner descriptor for an ability cast is not identified.

## Notes

V: a producer of descriptors of this shape is the scene task SceneMsgTask_Run. It reads the current scene task record's u16 at +28 as the word, takes group = word >> 11 to select one of the group objects at qword_140D40990, uses index = word & 0x7FF, asks the group object (sub_1400FC85C) for class and kind, and passes the descriptor to sub_1400EF9EC / sub_1400E5F78. I: its role in battle presentation follows the descriptor shape only; that it feeds the banner is not established (?).

## Open questions

? the producer of the descriptor the banner shows for an ability cast; ? how a scene task message reaches the banner, if it does.
