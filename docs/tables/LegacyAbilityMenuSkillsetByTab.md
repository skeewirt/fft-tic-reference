# LegacyAbilityMenuSkillsetByTab

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140684E44`
- **Rows:** 4 rows of 1 byte
- **Keyed by:** ability menu tab 0..3
- **Read by:** [ClassicMenu_LoadPageArtPack](../functions/ClassicMenu_LoadPageArtPack.md)
- **Row layout:** [LegacyAbilityMenuSkillsetByTabRow](../structs/LegacyAbilityMenuSkillsetByTabRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four skillset ids, one per tab of the legacy ability menu; the same object continues with two 7-entry dword tables (run starts 0, 6 ... 36 and 0, 60 ... 360) that cut the page art into per-page ranges. Verdict: designer-data.

## Behavior

- V: reader indexes byte [tab] then calls Skillset_BuildAbilityList(skillset, 1); the dword tables are read as table[page] and table[page + 1] - table[page]
- V: sub_140388EB4 and sub_14038BF34 (legacy ability list builders): index the bytes with the tab number and build the ability list of that skillset
- V: ClassicMenu_LoadPageArtPack (0x140343770) reads the two dword tables that follow in the same 0x4C-byte object

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which in-game skillsets 0x0A, 0x0B, 0x0C and 0x10 are
- ?: what unit the run starts count (sprite cells or tiles of the page art)
