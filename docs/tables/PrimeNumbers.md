# PrimeNumbers

- **Kind:** table
- **Area:** [Math](../areas/math.md)
- **Storage:** Executable
- **Address:** `0x14067E1D0`
- **Rows:** 54 rows of 1 byte
- **Keyed by:** list position 0..53
- **Read by:** [sub_140280850](../functions/sub_140280850.md)
- **Row layout:** [PrimeNumbersRow](../structs/PrimeNumbersRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Primes below 256. The math targeting routine marks units whose chosen value (CT, experience, level or a derived value) is in this list. Verdict: engine-data.

## Behavior

- V: the membership test is a linear search over 54 bytes (kind byte bit 8 selects it; bits 4, 2, 1 select multiples of 5, 4, 3)

## Notes

Our names. Tags: V.

## Open questions

None recorded.
