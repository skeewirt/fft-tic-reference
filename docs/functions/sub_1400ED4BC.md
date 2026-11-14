# sub_1400ED4BC

- **Address:** `0x1400ED4BC`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int sub_1400ED4BC(void)`
- **Callers:** `sub_1403358FC`, `sub_140336B88` (2 sites)
- **Callees:** the UI module's kind accessor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the item screen's current list mode: the dword at the UI object's `+0x12EC`, or 0 when the module is not up.

## Behavior

- V: it is the dword twin of the equip-slot getter: same module check, same fallback of 0, field `+0x12EC`.
- V: two call sites, both in the item screen's list and sort handlers.
- V: the value is used as a mode selector by those callers, not as a count or an index.
- V: it takes no argument and writes nothing.
- I: the field is the page or tab the item list is showing; the item research uses it to tell the equip screen from the item menu.
- ?: the exact set of mode values and their page names.

## Referenced by

- Called by: [sub_1403358FC](sub_1403358FC.md), [sub_140336B88](sub_140336B88.md)

## Notes

Read in full. Its role as a screen discriminator is inferred from the two callers.

## Open questions

None recorded.
