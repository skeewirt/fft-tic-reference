# PoachSell_ShowTotal

- **Address:** `0x1401B23A0`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void PoachSell_ShowTotal(...)`
- **Callers:** the poacher sell screen
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows the sale total of the poacher sell screen.

## Behavior

- V: shows amount x the value at window +2808 (the sell price of the chosen row: PoachItem row +0x28, read by the code that fills the window, not in this body) as the row price.

## Open questions

None recorded.
