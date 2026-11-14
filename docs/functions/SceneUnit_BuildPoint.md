# SceneUnit_BuildPoint

- **Address:** `0x140272BD0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 sub_140272BD0(__int16 previewIndex, _WORD out[3])`
- **Callers:** `SceneUnit_MeasureRange`, event scripts via `SceneCallback_Dispatch`
- **Callees:** `sub_140260ABC`, `sub_140262AF4`, `sub_140262B20`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the three-word world point (x, height, z) of a unit from its live record.

## Behavior

- V: finds the scene node for the preview index with `sub_140260ABC`; missing -> 0.
- V: out[0] (world x) is 28 times the tile-x byte at offset 79 of the node's unit record, plus 14 (tile x centre).
- V: out[2] (world z) is 28 times the tile-y byte at offset 80 of the node's unit record, plus 14 (tile y centre).
- V: height = `sub_140262B20(record, &point)`; when `(node+300 & 3) == 1` it adds a unit height term minus 10.
- V: returns 1.

## Referenced by

- Called by: [sub_140389D84](sub_140389D84.md)

## Notes

Confirms that unit tile coordinates are bytes +79/+80 and that the grid pitch is 28 world units with a 14-unit centre offset. The Legate's live read (Ramza 6,8 -> 6,7) matches this rule.

## Open questions

? the exact height expression (the decompiler loses one register); ? the meaning of node+300 bits.
