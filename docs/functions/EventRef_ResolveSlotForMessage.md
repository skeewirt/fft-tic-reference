# EventRef_ResolveSlotForMessage

- **Address:** `0x1402DE204`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int EventRef_ResolveSlotForMessage(int ref, char flag)`
- **Callers:** EventMessage_Scripted (4), sub_1402D9490, sub_1402D9F4C
- **Callees:** ScenePreview_FindEntry, sub_140272538, SceneObject_FindBySlot, ScenePreview_IndexOfSlot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The message code's copy of EventRef_ResolveSlot: turns a script reference id into the slot of the object it names (2000 when none).

## Behavior

- V: the same steps as EventRef_ResolveSlot: the preview entry of the id, the named-character lookup for ids 1..73 and 162 / 163, ref 104 (the first record of 0..15 whose byte +5 has bit 0 or 1: its byte +401, 2000 when none; the walk's bound and its 'none found' test both compare with 16 at 0x1402DE2B0 / 0x1402DE2B5), ref 105 (the scene objects of slots 0..20 whose record +440 is set), refs 100..103 from a fixed table.
- V: the record +5 is the entry's byte +24 (Unit_ApplySpawnRecord) for a battle's own unit and 11 or 8 for a party unit (UnitWork_CopySaveFields: 11 when the unit byte is below 4), so ref 104 never names a party unit only because its walk stops at 15.
- M: 4 stock entry keys give an entry those bits (519, 523, 524, 553).

## State touched

- Calls: [ScenePreview_FindEntry](ScenePreview_FindEntry.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md)

## Notes

Name is ours.

## Open questions

None recorded.
