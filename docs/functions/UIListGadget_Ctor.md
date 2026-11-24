# UIListGadget_Ctor

- **Address:** `0x14028C458`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIListGadget_Ctor(UIListGadget *gadget)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the row list gadget (General Options +1744).

## Behavior

- V: +24 holds the list component and +96 the cursor row.

## Referenced by

- Called by: [WorldMapAgent_CreateAddons](WorldMapAgent_CreateAddons.md), [WorldMapBaseList_Construct](WorldMapBaseList_Construct.md)

## Notes

Struct: UIListGadget.

## Open questions

None recorded.
