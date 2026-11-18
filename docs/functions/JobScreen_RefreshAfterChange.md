# JobScreen_RefreshAfterChange

- **Address:** `0x1402BD05C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `_UNKNOWN **JobScreen_RefreshAfterChange(void)`
- **Callers:** `sub_1402BD740`, `sub_1402D67C8`, `sub_1402D6E14`, `sub_1402D6F10`? (through the handlers)
- **Callees:** `memset`, `sub_1402855F0`, `sub_140360700`, `sub_140112A04`, `sub_1402C1310`, `sub_1402C2778`, `sub_1402C19EC`, `sub_140289894`, `sub_140337DA0`, `sub_140336D5C`, `sub_140336E68`, `JobTree_FillJobRecords`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Refreshes the job/equip screen after a change: it copies the selected party record into the 0x1407B27xx record,
the 0x141876E90 panel block and the 0x141876C80 tail record, then rebuilds the job list.

## Behavior

- V: It copies the selected unit record's first 0x30 bytes to `xmmword_1407B27C0`/`qword_1407B2758` and the
  record's +0x30..+0x6F to `xmmword_141876E90` with four 16-byte moves (0x1402BD15D, 0x1402BD168, 0x1402BD173,
  0x1402BD17E). The hand words at record +0x54..+0x5C therefore land at block +0x24..+0x2C.
- V: It copies the record's +0x70 onward to the 0x141876C80 region with a 4x128-byte loop, so that block is the
  tail of the same record.
- V: It also builds the 0x1407B27xx fields from a battle unit when the selected unit is in the battle table
  (the `sub_1402855F0`/`sub_140360700` branch); that branch overwrites the same block fields.
- V: It calls `sub_1402C1310` with the record parts and the C80 block (0x1402BD5B0 passes the block to
  `sub_1402C19EC`), which renders the equip screen.
- V: The block copy is raw: a bit-15 word in the unit record reaches block +0x24 and is passed to the renderers
  and the panel task unchanged.
- V: It does not strip or mask any equipment word; the only masks are in the callees that read ids.
- I: This is the writer that makes the panel block's hand words a copy of the live party record, not of the save.
- V: it copies the selected party unit's block from +112 (unlock mask, learned bits, levels, the first JP words) into the preview record at 0x141876C10, which never receives +44; the header and preview panels are built from it.

## State touched

- Calls: [sub_1402855F0](sub_1402855F0.md), [JobTree_FillJobRecords](JobTree_FillJobRecords.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_PartyCount](../globals/g_PartyCount.md), [g_PartyUnits](../globals/g_PartyUnits.md)
- Writes: [xmmword_141876E90](../globals/xmmword_141876E90.md)

## Referenced by

- Appears in flows: [EquipPanelBlockFill](../flows/EquipPanelBlockFill.md)
- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md), [sub_1402D67C8](sub_1402D67C8.md), [sub_1403331F8](sub_1403331F8.md), [sub_140333338](sub_140333338.md), [sub_140366ABC](sub_140366ABC.md), [sub_140366FE0](sub_140366FE0.md), [sub_14036AC74](sub_14036AC74.md), [sub_14036B71C](sub_14036B71C.md)
- Observed behaviours: [BattleRosterCopiesCarryTheBattleSlotAt44](../behaviors/BattleRosterCopiesCarryTheBattleSlotAt44.md), [CombatSetJobBytesAreOnlyCopied](../behaviors/CombatSetJobBytesAreOnlyCopied.md)

## Notes

V: copies record +0x30..+0x6F to the panel block with four movaps (0x1402BD15D-0x1402BD17E), so the hand words at +0x54..+0x5C land at +0x24..+0x2C raw.

## Open questions

- ?: whether the battle-unit branch runs while the Outfitter is open; it would replace the block with a
  battle record's words.
