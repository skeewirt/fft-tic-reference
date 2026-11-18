# g_TrackedDateCounters

- **Kind:** global
- **Address:** `0x1411A7220`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[64]: one counter per tracked date slot, capped at 99; slot 0 counts the date held in event variables 95 and 96, slots 1..63 the {month, day} pairs at 0x1407B8130. Written by the daily calendar tick (sub_1402CCEE0) and the jump by N days (sub_14039DA58); read by the page of the second tavern list (sub_140376040) at index (entry >> 4); copied by the save pack and unpack, the checkpoint pair and the errand state copy (saved at +0x48C of the save work block); reset by sub_14033FB84.

## Open questions

None recorded.
