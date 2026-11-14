# g_EventScriptActive

- **Kind:** global
- **Address:** `0x142FF9EC0`
- **Type:** `uint32[2]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Low dword: 1 while EventScript_Run runs a script (set at its start, 0x14023A8DE; cleared at both ends 0x14023EDD0 / 0x14023F29E, by sub_14023F324, sub_140210AF0, Video_RefreshState and sub_1402D3918); EventControl_Update runs only while it is set. High dword: written 2 / 0 by Battle_InitScene; read by other event code as a slot mask.

## Referenced by

- Read by: [EventControl_Update](../functions/EventControl_Update.md)

## Open questions

None recorded.
