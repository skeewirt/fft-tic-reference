# GUIComponentCustom_Create

- **Address:** `0x140406048`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponentCustom *GUIComponentCustom_Create(void *owner, void *def)`
- **Callers:** component instantiation paths
- **Callees:** GUIComponent_Ctor, GUIComponent_Init

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates a 648-byte GUIComponentCustom from the UI pool (pages of 64), constructs it, links it into the owner's child list and registers it by id.

## Behavior

- V: pool bookkeeping at qword_143CDA280+808.
- V: sets vftable_faith::UISystem::GUIComponentCustom (0x140722490).

## State touched

- Calls: [GUIComponent_Ctor](GUIComponent_Ctor.md), [GUIComponent_Init](GUIComponent_Init.md)

## Notes

Instances are named 'Unit#N' (N = creation order) for the tree's UnitJob references.

## Open questions

None recorded.
