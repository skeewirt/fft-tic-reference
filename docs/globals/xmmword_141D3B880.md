# xmmword_141D3B880

- **Kind:** global
- **Address:** `0x141D3B880`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `EquipPanelBlock`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle module's copy of the same 64-byte record slice (+0x30..+0x6F), with its five hand words at +0x24; read by the battle panel sub_140399A64.

## Behavior

- V: written by sub_14033E394 (movaps at 0x14033E412-0x14033E437) from a battle record.
- V: read by sub_140399A64 (0x140399ACD/0x140399AD9/0x140399AF6); no other instruction in the census names the 64-byte block.

## Referenced by

- Read by: [sub_140399A64](../functions/sub_140399A64.md)

## Open questions

? the battle record the copy comes from and its hand-word provenance.
