# BuildReport_ReadEnvironment

- **Address:** `0x1400B1AA4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `DWORD BuildReport_ReadEnvironment(void *record)`
- **Callers:** sub_1400B1844 (0x1400B1A7C)
- **Callees:** GetEnvironmentVariableA

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears a large report record's sections and copies three build environment variables into it.

## Behavior

- V: zeroes a 0x40-byte head and about a dozen sections (each a count dword, a flag byte set to 1 and a data area of 0x80 .. 0x4E20 bytes) of the 61,272-byte record.
- V: reads the environment variables JOB_NAME (up to 128 bytes, at +55216), BUILD_NUMBER (up to 32 bytes, at +55352) and BUILD_URL (up to 256 bytes, at +55392).
- V: a variable that is not set leaves its field empty (the result of the last read is returned).
- V: the array of records that this runs for (256 records at unk_141D8BD00) is referenced only by BuildReport_InitAll; the three fields have no reader that was found.
- I: searched the displacements 0xD7B0, 0xD838 and 0xD860 across the code; the array base is referenced only by BuildReport_InitAll.
- I: the record is a build or crash report that was meant to carry a build-server identity; nothing in this build reads it (rests on the field names and the absence of readers).

## Referenced by

- Observed behaviours: [BuildServerVariablesCopiedAtStartup](../behaviors/BuildServerVariablesCopiedAtStartup.md)

## Notes

sub_1400B1844 clears the record the same way and then calls this function; BuildReport_InitAll runs it for each of the 256 records.

## Open questions

? what the other sections of the record hold.
