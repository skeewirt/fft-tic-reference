# LookSitesUseTheSaveRecordNotTheSlot

- **Kind:** observed behaviour
- **Scope:** engine (portraits and faces)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [sub_140300768](../functions/sub_140300768.md), [sub_140300D74](../functions/sub_140300D74.md), [sub_14032AB3C](../functions/sub_14032AB3C.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The six portrait readers compute the look from the unit's marker, job byte and sex each time through six copies of one 211-word table; none of them reads the battle slot, and they are separate from the battle sprite path.

## Behavior

- V: the sum 2 * job - 52 (+1 for women, jobs 92 and 93 adjusted) appears in those functions at 0x2C082F, 0x2B573F, 0x2DB44D, 0x3009BD, 0x300F95 and 0x32ABEA, each against its own copy of the table and a bound of 0xD3; none stores the number.
- V: the six copies hold the same 211 words (compared word by word).
- V: JobRecord_FillIconAndGenericFlag computes a flag (job minus 74 above 19), not a sprite number; JobTree_FillJobRecords calls Unit_ResolvePreviewShape for generic jobs and stores the result through SpriteRecord_Fill (32-bit).

## Open questions

None recorded.
