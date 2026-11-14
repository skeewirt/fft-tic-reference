# MenuListFlagFlow

- **Kind:** observed behaviour
- **Scope:** g_MenuList and the three list kinds that reuse it (shop, equip, ability), plus the job list
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [g_MenuList](../globals/g_MenuList.md), [MenuListWord](../structs/MenuListWord.md), [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md), [JobAbilityList_Build](../functions/JobAbilityList_Build.md), [sub_140286A78](../functions/sub_140286A78.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [sub_140336664](../functions/sub_140336664.md), [sub_140366FE0](../functions/sub_140366FE0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The two high bits of the 16-bit list words are per-list-kind state, not part of the id: bit 14 is cannot-equip / cannot-learn / current, bit 15 is not written to g_MenuList at all but marks the equip-candidate buffers.

## Behavior

- V: four builders set bit 14 on g_MenuList entries: Shop_BuildItemList (0x140288FBD, 0x140289061), Inventory_BuildEquipList (0x140288CAF), JobAbilityList_Build (0x1402869F3, 0x140286A2A) and sub_140286A78 (0x140286B81).
- V: JobAbilityList_Build also sets bit 12 (0x140286A03) and bits 13+14 (0x140286A25); sub_14028A474 sets 0x1000 and 0x6000 on 8-byte ability rows.
- V: no instruction writes bit 15 to g_MenuList: the only two 0x8000 list writers, sub_140287D9C (0x140288544) and sub_1402875A4, write their 5-word output buffers (g_EquipCandidates / stack).
- V: seven functions read bit 14 of a g_MenuList entry: ShopEntry_Fill, sub_140332C54, sub_140332C8C, sub_140336664, sub_14036A994, sub_140366FE0 and sub_140333974.
- V: no function in the exported set reads bit 15 of a g_MenuList entry; the bit-15 readers it does contain (ShopEntry_Fill 0x14036B4A9, sub_1402D5CC4) read the party equipment words instead.
- V: the movers copy whole 16-bit words, so a flag travels with an entry through ItemOrder_FilterList (0x140285E7E, memmove 0x140285EA8), sub_140286228 (0x1402863AA), sub_140285B10 (0x140285BF6), sub_140285F2C (0x140285F57) and sub_140336B88 (0x140336D09).
- V: two movers compare a whole word against a masked one and therefore never match a flagged entry: ItemOrder_FilterList compares order[i] unmasked to list[i] & 0x3FF (0x140285E63), and sub_140286228 inserts its row word unmasked but compares it to list[i] & 0x3FF (0x140286309).
- I: sub_140285F2C can carry a flagged word into the saved order list off_14067F498[group], because it copies g_MenuList[0..] whole; its only caller builds the list in mode 0, so no flagged word was seen on that path.

## Notes

V: the sheets of the builders, row helpers and movers, and a 49-site table. The Outfitter carriers (g_EquipCandidates, g_EquipSet, the equipment words) are documented on their own records.

## Open questions

? whether any screen displays bit 12 or bit 13 of an ability entry; ? whether the demo/retail build differs in the ability-list modes.
