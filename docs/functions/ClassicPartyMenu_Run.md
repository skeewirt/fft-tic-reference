# ClassicPartyMenu_Run

- **Address:** `0x14033E4C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long ClassicPartyMenu_Run(int unit)`
- **Callers:** a menu scene task
- **Callees:** Inventory_RebuildOrders, Unit_ReloadFromJobRow, sub_14033E038, sub_1403972C0, sub_1403957E4, sub_14028531C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame driver of the legacy party menu: prepares the shared header state and runs the handler of the current mode.

## Behavior

- V: on mode 0 (first call) rebuilds the inventory orders, loads the page art and sets mode 1; otherwise keeps the mode.
- V: sets the header geometry words (two sets depending on a state flag), then calls the handler of the mode from the 6-slot mode table (0x140684918).
- V: afterwards, while a mode of -1 is pending, compares the unit's saved fields with the preview copy and reloads the preview unit when they differ; clamps the preview HP and MP to their maxima.

## State touched

- Calls: [Inventory_RebuildOrders](Inventory_RebuildOrders.md), [sub_14033E038](sub_14033E038.md), [sub_14028531C](sub_14028531C.md)

## Open questions

?: the modes other than 1.
