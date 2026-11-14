# RenderQueue_Flush

- **Address:** `0x1403A4308`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall RenderQueue_Flush(__int64 m)`
- **Callers:** RenderFrame_Update (V: single xref)
- **Callees:** scheduler vtable slots +24 (count), +56 (enqueue), +64 (kick), job record vtable slot +8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets every 264-byte job record of the pass array and re-submits it to the scheduler, then submits the trailing fence record and kicks the scheduler.

## Behavior

- V: sched = *(g_Application + 1168); count = sched->vtable[+24]() (dword). Loop count times over records at *(m+13760) + i*264.
- V: per record: rec->vtable[+8](rec) (reset / prepare), then sched->vtable[+56](sched, rec) (enqueue). Stride 264 bytes (both the vtable lookup offset v4 and the argument v5 advance by 264).
- V: after the loop the fence record at m+13768 gets the same two calls (vtable[+8], then sched vtable[+56]).
- V: last call sched->vtable[+64](sched, 0) is the kick, and its result is returned.
- I: record array pointer at m+13760 is the pass jobs of RenderFrame; m+13768 is a single embedded record used as end-of-frame fence.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

No blend / sampler / GPU state is touched here; it is pure job bookkeeping.

## Open questions

? class names of the scheduler and of the 264-byte job record; what the arg of the +64 call (0) selects.
