# SaveErrorMessages

- **Kind:** table
- **Area:** [Save data](../areas/save-data.md)
- **Storage:** Executable
- **Address:** `0x14071F270`
- **Rows:** 48 rows of 8 bytes
- **Keyed by:** result code (searched)
- **Row layout:** [SaveErrorMessage](../structs/SaveErrorMessage.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Result code of the save-data layer to message number for the save and load screens. Verdict: engine-data.

## Behavior

- V: four readers scan the first 0x30 rows; the message number is the dword after the code; default 21
- V: message numbers 1..20 appear (ten of them twice or more)

## Notes

Our names. Tags: V.

## Open questions

None recorded.
