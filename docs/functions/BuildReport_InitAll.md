# BuildReport_InitAll

- **Address:** `0x14000D844`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 BuildReport_InitAll(void)`
- **Callers:** runtime initialiser table
- **Callees:** sub_1400B1844

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Static initialiser: sets up all 256 build report records.

## Behavior

- V: loops 256 times over the array at unk_141D8BD00 in steps of 61,272 bytes and calls sub_1400B1844 on each record.
- V: it is registered in the C runtime's initialiser list (a data reference to the function sits in the table at 0x140613208, outside the function) and has no direct caller.
- I: because the records are filled before the game starts, the environment variables are read once at process start (rests on it being a static initialiser).

## Referenced by

- Observed behaviours: [BuildServerVariablesCopiedAtStartup](../behaviors/BuildServerVariablesCopiedAtStartup.md)

## Notes

See BuildReport_ReadEnvironment for the fields that are filled.

## Open questions

? who uses the 256 records.
