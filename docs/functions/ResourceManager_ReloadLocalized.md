# ResourceManager_ReloadLocalized

- **Address:** `0x1400919A8`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int ResourceManager_ReloadLocalized(ResourceManager *mgr, void *language_entry)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a text language and reloads every localized resource handle (flag 8).

## Behavior

- V: walks a list at manager +40 for an entry whose name equals the argument and returns if found; else appends one (the 32-byte record copied, the name) and calls its function (+16) with (+24, +32), which returns a language number; when that equals the current text language (`g_LanguageInfo` +8, 1 when unset) it returns 0.
- V: otherwise it walks the resource hash (512 buckets from manager +4160, 24 bytes each, each under its shared SRW lock at manager +56 + 8 * i) for handles with flag 8 (+92) and reference count 1 (+80) whose requested path (+24) starts with the entry's name; for each: the key's language nibble (+39 low 4 bits) is set to the new language, vtable +40 (release the data), sub_140095EE0, load status cleared, state +92 low 3 bits = 1, ResourceHandle_LoadNow, flag 0x20000 (bit 17, set and cleared with bit instructions) set around it, vtable +32.
- I: this is the language switch reloading every localized file; every nxd handle has flag 8 (NxdTable_CreateHandle), so a language change reloads the nxd tables through the normal load, NxdHandle_OnLoaded and NxdTable_BindRows. A change of Text Language was seen to redraw the menus at once (behavior TextLanguage); this function itself was not traced live.

## Referenced by

- Observed behaviours: [NxdTableRebinding](../behaviors/NxdTableRebinding.md)

## Open questions

None recorded.
