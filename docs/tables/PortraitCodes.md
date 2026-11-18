# PortraitCodes

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1406807C0`
- **Rows:** 211 rows of 2 bytes in each of five byte-identical copies (0x1406807C0, 0x140680070, 0x140681A90, 0x1406829F0, 0x140683A70)
- **Keyed by:** (0x60 | female) + 2 * (job - 74), or the job own look; guard below 0xD3
- **Read by:** [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [sub_140300768](../functions/sub_140300768.md), [sub_140300D74](../functions/sub_140300D74.md), [sub_14032AB3C](../functions/sub_14032AB3C.md)
- **Held in:** [g_PortraitCodeA](../globals/g_PortraitCodeA.md), [g_PortraitCodeD](../globals/g_PortraitCodeD.md), [g_PortraitCodeE](../globals/g_PortraitCodeE.md), [g_PortraitCodeF](../globals/g_PortraitCodeF.md)
- **Row layout:** [PortraitCodeRow](../structs/PortraitCodeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Portrait code word of each generic look. The game keeps five byte-identical copies (compared in the database), each read by its own function: Unit_GetSpriteSetId (scene branch only, scene types 21, 43, 44, 51; its result is turned into a face number by the sprite-id-to-shape function), the party job record builder, the scripted event message, two functions of one screen and one more. 0 = no portrait.

## Behavior

- V: the value is shape - 71 for generic shapes on the scene branch.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: whether copies B and C existed (the copy letters skip B and C)
