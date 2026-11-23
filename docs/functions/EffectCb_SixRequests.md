# EffectCb_SixRequests

- **Address:** `0x14035E214`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall EffectCb_SixRequests(__int16 slot, int index, int, int)`
- **Callers:** reached only through tbl_EffectCallbacks (0x1406759C0, index 139), i.e. EffectScript_OpCallCallback
- **Callees:** EventWork_RunCommand (six calls)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect callback (entry 139 of the effect callback table): on its first call it issues six requests through `EventWork_RunCommand` and moves its state byte to running; on a finish request it resets the state.

## Behavior

- V: the state byte is at `0x141D33136 + 312 * slot + index`, that is byte 38 + index of the 312-byte script record of the slot (the record layout `EffectScript_OpCallCallback` works with).
- V: state 1: calls `EventWork_RunCommand(0x80, k, 1, 1)` for k = 1 to 6 (0x80 is encoded as a sign-extended byte immediate), sets the byte to 2 and returns 2.
- V: state 3: sets the byte to 0 and returns 0.
- V: any other state (0 and 2) returns the byte unchanged and does nothing.
- V: the database declares four arguments but only the first two are read; nothing else is called.
- I: states 1 / 2 / 3 mean start / running / finish (rests on the three callbacks 139, 143 and 148 sharing this pattern and on the value returned).
- ?: what `EventWork_RunCommand` selector 0x80 with indices 1..6 does (the callee was not read).

## State touched

- Calls: [EventWork_RunCommand](EventWork_RunCommand.md)

## Notes

V: whole body read. The name is ours.

## Open questions

?: the effect that uses callback 139; the meaning of selector 0x80 of `EventWork_RunCommand`.
