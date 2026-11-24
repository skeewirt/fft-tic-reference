# BuildServerVariablesCopiedAtStartup

- **Kind:** observed behaviour
- **Scope:** engine (start-up)
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [BuildReport_InitAll](../functions/BuildReport_InitAll.md), [BuildReport_ReadEnvironment](../functions/BuildReport_ReadEnvironment.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Before the game starts, a static initialiser fills 256 report records and copies three build-server environment variables (a job name, a build number and a build address) into each. Nothing reads them.

## Behavior

- V: BuildReport_InitAll runs for the 256 records at unk_141D8BD00 (61,272 bytes each) as part of the C runtime initialisers.
- V: BuildReport_ReadEnvironment reads JOB_NAME, BUILD_NUMBER and BUILD_URL into three fields of each record.
- I: on a player's machine the variables are normally absent, so the fields stay empty; no reader of the fields or of the array was found.

## Open questions

None recorded.
