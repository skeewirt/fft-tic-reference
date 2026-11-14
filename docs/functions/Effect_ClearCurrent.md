# Effect_ClearCurrent

- **Address:** `0x14031A7E0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 Effect_ClearCurrent(void)`
- **Callers:** sub_140235804
- **Callees:** sub_14031A6AC, sub_14031A740, sub_140381A54

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the running effect: resets its bookkeeping and sets the current effect number to -1.

## Behavior

- V: clears dword_143C51C6C, dword_143C51C98, dword_143C51CA4 and qword_143C51D30, calls sub_14031A6AC, sub_140381A54 and sub_14031A740.
- V: sets word_141D330BC and dword_142E801F4 to -1; unless the battle state is 0x34 it writes 0x501 to the map view camera manager at +288.

## Notes

Name is ours.

## Open questions

None recorded.
