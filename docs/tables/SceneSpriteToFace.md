# SceneSpriteToFace

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1407146D0`
- **Rows:** 160 rows of 4 bytes
- **Keyed by:** scene sprite id up to 0x9F (not the job)
- **Read by:** [SpriteId_ToShape](../functions/SpriteId_ToShape.md), [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md), [sub_1401F3858](../functions/sub_1401F3858.md), [sub_140214134](../functions/sub_140214134.md), [sub_140221798](../functions/sub_140221798.md), [sub_1402DF374](../functions/sub_1402DF374.md), [sub_1402F8684](../functions/sub_1402F8684.md), [sub_140338A28](../functions/sub_140338A28.md)
- **Row layout:** [SceneSpriteFaceRow](../structs/SceneSpriteFaceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Face number of each scene sprite id, read by the sprite-id-to-shape function and five inline copies of it.

## Behavior

- V: eleven functions read it.
- V: 11 functions read this table (cross-references in the database); the first ten are linked.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
