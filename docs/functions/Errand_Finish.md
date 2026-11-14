# Errand_Finish

- **Address:** `0x14036FF30`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int64_t Errand_Finish(int activeSlot)`
- **Callers:** `sub_14037085C`
- **Callees:** Errand_ApplyResult, Errand_TreasureMilestone, `sub_1402D3400`, `sub_140370EDC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends an active errand: totals the gil, queues a result entry and applies the result.

## Behavior

- V: sums the per-unit gil results of the party and adds the bonus gil to form the pending gil total.
- V: appends an entry of kind 17 to the result queue with the active slot recorded in it.
- V: calls Errand_ApplyResult on that entry.
- V: if Errand_TreasureMilestone returns non-zero it continues with `sub_1402D3400`, otherwise with `sub_140370EDC`.

## State touched

- Calls: [Errand_ApplyResult](Errand_ApplyResult.md), [Errand_TreasureMilestone](Errand_TreasureMilestone.md)

## Open questions

None recorded.
