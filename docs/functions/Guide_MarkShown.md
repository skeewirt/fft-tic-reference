# Guide_MarkShown

- **Address:** `0x1400DA454`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Guide_MarkShown(int id)`
- **Callers:** not recorded
- **Callees:** Guide_GetEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks a guide of window type 1 or 2 as seen.

## Behavior

- V: sets the guide's seen bit in the config bits g_ConfigData +204; also raises +225 / +224.
- I: the name is proposed from the bit it sets.

## State touched

- Calls: [Guide_GetEntry](Guide_GetEntry.md)
- Writes: [g_ConfigData](../globals/g_ConfigData.md)

## Referenced by

- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
