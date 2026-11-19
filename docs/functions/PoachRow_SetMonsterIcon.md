# PoachRow_SetMonsterIcon

- **Address:** `0x1402A4508`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void PoachRow_SetMonsterIcon(...)`
- **Callers:** the poacher shop rows
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the monster icon of a poacher list row.

## Behavior

- V: IconMonster plays 'Rare' or 'Normal' by PoachItem +0x34 (column rare); its Icon part frame is PoachItem +0x30 (column icon).

## Open questions

None recorded.
