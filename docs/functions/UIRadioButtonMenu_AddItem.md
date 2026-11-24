# UIRadioButtonMenu_AddItem

- **Address:** `0x1402AD750`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t UIRadioButtonMenu_AddItem(int64_t menu, int64_t node)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds a node to a radio button menu and registers the menu's id as one of the node's owners.

## Behavior

- V: writes the menu id (menu +8) into the first free of the node's four owner dwords at +584, unless already there.
- V: appends the node to the item array at menu +24 and increments the count at menu +16; there is no bound check. Returns the new count.

## Open questions

None recorded.
