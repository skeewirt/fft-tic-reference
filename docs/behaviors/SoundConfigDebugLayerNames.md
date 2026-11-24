# SoundConfigDebugLayerNames

- **Kind:** observed behaviour
- **Scope:** engine (sound driver)
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [SoundCommand_ProcessQueue](../functions/SoundCommand_ProcessQueue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The sound driver resolves a config category name to a layer number; two names that no config file needs to define have built-in numbers: 'SDebug' is layer -2 and 'SUserConfig' is layer -3.

## Behavior

- V: SoundCommand_ProcessQueue, command 3: a name found in the config file's category list uses that entry's layer byte; otherwise 'SDebug' selects -2, 'SUserConfig' selects -3 and anything else -1.
- V: 'SUserConfig' is also the category named by the settings apply routine sub_1400B6CF8 when it sets volumes; 'SDebug' appears in no other code.

## Open questions

None recorded.
