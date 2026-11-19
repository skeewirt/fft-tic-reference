# Mem_CopyChecked

- **Address:** `0x14002630C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void Mem_CopyChecked(void *dst, size_t dstSize, const void *src, size_t count)`
- **Callers:** 127 call sites in 51 functions, among them sub_140281488, BattleAction_BuildReaction, BattleAction_ReleaseCharged, Battle_ExecuteSecondaryAction, BTurn_PreviewAction, Battle_ResolveAction, EventScript_LoadIntoBuffer, sub_1400C7F54 (IDA code references)
- **Callees:** memmove, memset, _errno, _invalid_parameter_noinfo, sub_140026BD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The game's checked copy: copies the smaller of the destination size and the count, and reports a destination too small or a null pointer; every copy of the 20-byte action block (unit +0x1A0) and of the formula block's record copies goes through it.

## Behavior

- V: n = min(count, dstSize); with n zero nothing is copied. With a null destination it stores errno 22 and calls _invalid_parameter_noinfo.
- V: with both pointers set it calls memmove(dst, src, n); with a null source it clears the destination (memset to dstSize), stores errno 22 and calls _invalid_parameter_noinfo. The errno 34 (range) branch tests dstSize >= n, which min() always satisfies, so it cannot run (I: the compiler kept the C runtime's own code).
- V: when dstSize is smaller than count it calls sub_140026BD4 (a report helper, arguments: a string, dstSize, a constant, 2) after the copy.
- V: 127 call sites in 51 functions (IDA code references, 2026-11-12): the event script loader, the file command readers, the unit record copies and the battle action code.
- V: the battle action block at unit +0x1A0 (0x14 bytes: +1 command byte, +2 ability id u16) is never copied by a move instruction: every copy of it (the request queue, the reaction and charge saves, the secondary action, the preview, the AI current action) calls this function with size 0x14 (the size, the block offsets +0x24 and unit offset +0x1A0 are the callers' arguments, never operands of this body). Battle_ResolveAction also uses it for the 0x14-byte ability record copy at g_FormulaBlock +0x24, the 8-byte weapon record at +0x38 and the 6-byte inflict record at +0x40.

## State touched

- Writes: [UnitWorkRecord.action_request](../structs/UnitWorkRecord.md#action_request)

## Referenced by

- Called by: [Ai_UnitTurnStep](Ai_UnitTurnStep.md), [Battle_ResolveAction](Battle_ResolveAction.md), [Battle_StatusResolve](Battle_StatusResolve.md), [ClassicMenu_LoadPageArtPack](ClassicMenu_LoadPageArtPack.md), [Formula_04_MagicGun](Formula_04_MagicGun.md)
- Observed behaviours: [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md)

## Notes

Read 2026-11-12. 175 bytes, read whole. The name is the C runtime's (the shape and the two errno values, 22 invalid argument and 34 range, are Mem_CopyChecked's); the extra truncation to the smaller size is the C runtime's own behaviour here.

## Open questions

? what sub_140026BD4 does with its arguments (not read).
