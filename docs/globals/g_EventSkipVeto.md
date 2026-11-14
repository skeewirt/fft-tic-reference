# g_EventSkipVeto

- **Kind:** global
- **Address:** `0x142FF9E54`
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Low dword: 1 while Battle_InitScene builds a battle (set at 0x1402C8A1B, cleared at 0x1402C9F36); 0 from sub_140210AF0, Video_RefreshState, sub_1402D3918. EventSkip_IsAvailable needs 0.

## Referenced by

- Read by: [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md)

## Open questions

None recorded.
