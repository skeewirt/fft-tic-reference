# Formula_ElementAffinity

- **Address:** `0x140305554`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_ElementAffinity(uint8_t element)`
- **Callers:** Formula_104_WotLDistanceScaledPhysical, Formula_45_HolySword, Formula_46_DarkSwordCrush, Formula_EarthFloatAndAffinity, Formula_PhysAttackFull, sub_140309380
- **Callees:** Status_FilterPendingSets, Formula_ZeroResult

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The target's element affinities applied to R+6: absorb, null, half, weak and the Oil double.

## Behavior

- V: with the element byte in cl: target +0x76 mask match sets R+18 bit 0x0400 (absorbed); +0x77 match calls Formula_ZeroResult (nullified); else +0x78 match halves R+6 and +0x79 match sets R+18 bit 0x0800 and doubles R+6.
- V: in the same non-null branch, element & target +0x63 bit 0x80 (status 16, Oil) sets R+36 bit 0x80 (I: the remove set, status 16 is Oil, so the doubled hit takes Oil away), doubles R+6 and sets R+39 = 8 when Status_FilterPendingSets(0) is non-zero.
- V: finally the element byte is stored at 0x1407B07BA.

## State touched

- Calls: [Formula_ZeroResult](Formula_ZeroResult.md)

## Referenced by

- Called by: [Formula_PhysAttackFull](Formula_PhysAttackFull.md)

## Notes

154 bytes, read whole. The absorb and weak flags are read later by Formula_FinalizeAbsorb and the result applier. Crosscheck: the store goes to 0x1407B07BA as the label dword_1407B07B8 plus 2 (named by label, not by address).

## Open questions

None recorded.
