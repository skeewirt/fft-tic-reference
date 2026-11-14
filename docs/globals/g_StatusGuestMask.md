# g_StatusGuestMask

- **Kind:** global
- **Address:** `0x1406829E4`
- **Type:** `battle status effects`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

5 bytes (the values 0xEF 0x00 0x31 0x79 0xE2): the statuses a unit whose +0x1B4 byte is negative (a guest or special unit) can still receive. Status_FilterPendingSets ANDs it into the pending-add set for such a unit; no other reader

## Open questions

None recorded.
