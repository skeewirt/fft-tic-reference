# Items and shops

Item records and categories, and the shops.

Functions: 103, Structures: 28, Globals: 29, Registries: 2, Flows: 2, Observed behaviours: 9, Tables: 33.

## Functions (103)

| Name | Address | Purpose |
|---|---|---|
| [EquipDetail_BuildCategoryLines](../functions/EquipDetail_BuildCategoryLines.md) | `0x1400F94DC` | Builds the text of the equipment detail category lines (UIStatusEffectCategory, nxd 56) for the equipment attribute record in the third argument. |
| [Inventory_AddCount](../functions/Inventory_AddCount.md) | `0x1402847F8` | Adds a signed delta to the owned count of one item id and returns the new count, or zero when the id is outside the accepted range. |
| [Inventory_AddWithOverflow](../functions/Inventory_AddWithOverflow.md) | `0x140101058` | Adds to an item's owned count with the game's 99 cap, sells the excess for gil, and appends a four-field record of the transaction to a caller-supplied vector. |
| [Inventory_RebuildOrders](../functions/Inventory_RebuildOrders.md) | `0x1402BB3EC` | Rebuilds the five item order lists and the derived menu state after a load or a party change: it picks the owning unit, syncs every group and refreshes the list globals. |
| [Inventory_ReturnItem](../functions/Inventory_ReturnItem.md) | `0x14030CEA4` | Puts one item back into the party inventory: the refund step for a use that was cancelled or resolved away. |
| [Inventory_SellOverflow](../functions/Inventory_SellOverflow.md) | `0x1402846C0` | Sells down every inventory count above 99 and adds the gil, which is the overflow rule the rest of the item path relies on. |
| [Item_CategoryFirstId](../functions/Item_CategoryFirstId.md) | `0x1402B8C0C` | Returns the first item id of the category (type) that contains the given id, so a caller can index a sub-record table from its start; 0 when the id is rejected. |
| [Item_CompareSortOrder](../functions/Item_CompareSortOrder.md) | `0x14030E774` | qsort comparator of two item-id bytes: -1 / 0 / 1 from the Item row dword +0x28 (column sort_order), smaller first. |
| [Item_CountEquippedByParty](../functions/Item_CountEquippedByParty.md) | `0x1402874D8` | Counts how many party units hold a given item id in their five equipment words. |
| [Item_CountTotal](../functions/Item_CountTotal.md) | `0x140287530` | Returns everything the party owns of an item: the inventory count plus the number equipped by the party. |
| [Item_FindCategoryIndex](../functions/Item_FindCategoryIndex.md) | `0x1402B8BCC` | Turns an item id into its category index: the number of leading entries of the 14-word first-id array (`g_ItemCategoryFirstId`) that are <= the id. |
| [Item_GetEquipPalette](../functions/Item_GetEquipPalette.md) | `0x1402B8E60` | Returns the palette-selector row of an item, chosen by the item's equipment category, or null when the item has no palette. |
| [Item_GetMenuField](../functions/Item_GetMenuField.md) | `0x140285A98` | Returns the one-byte sub-record field an item list shows for an item: the weapon power, the shield or armour byte, or the accessory field, chosen by the item menu category. |
| [Item_GetRecord](../functions/Item_GetRecord.md) | `0x1402B8C44` | Returns the 12-byte record of an item. |
| [Item_IsInCategory](../functions/Item_IsInCategory.md) | `0x1402B8EE8` | Tests whether an item belongs to a given menu category, accepting the matching category or one exactly seven apart. |
| [Item_IsOwned](../functions/Item_IsOwned.md) | `0x140100F78` | Answers whether the party owns an item, either in the inventory or equipped on one of the 54 units. |
| [Item_IsValidId](../functions/Item_IsValidId.md) | `0x1402B8EBC` | The stock validity test for an item id: one contiguous low range plus a five-id high range. |
| [Item_SellPrice](../functions/Item_SellPrice.md) | `0x1402874A8` | Returns the gil a shop pays for one unit of an item: half its record price, with a floor of one. |
| [ItemIcon_FormatLargePath](../functions/ItemIcon_FormatLargePath.md) | `0x1400FC0D8` | Writes the texture-parts path of an item's large icon: Icon row 12 ('equip_item/textureparts/ei_%03d_uitx') formatted with the item id. |
| [ItemIcon_FormatSmallPath](../functions/ItemIcon_FormatSmallPath.md) | `0x1400FC14C` | Writes the texture-parts path of an item's small icon: Icon row 13 ('equip_item_s/textureparts/ei_s_%03d_uitx') formatted with the item id. |
| [ItemOrder_FilterList](../functions/ItemOrder_FilterList.md) | `0x140285DF0` | Reorders a 0xFFFF-terminated item list by a saved order list, dropping every entry the order list does not name. |
| [ItemOrder_Remove](../functions/ItemOrder_Remove.md) | `0x140285ED8` | Removes one id from a saved order list by shifting the entries after it one place to the left. |
| [ItemOrder_SyncGroup](../functions/ItemOrder_SyncGroup.md) | `0x140285F80` | Brings the saved order list of one menu group in line with what the party owns: a newly owned id is put at the front, an id that is no longer owned is removed, and every other entry keeps its place. |
| [ItemTable_GetName](../functions/ItemTable_GetName.md) | `0x1402B892C` | Returns the display name of an item from its Item-en row (nxd table 45), or null when the row is missing. |
| [ItemTable_GetRowById](../functions/ItemTable_GetRowById.md) | `0x1402B889C` | Returns the Item-en row for an item id through the shared NXD table interface, or null when the row is absent. |
| [Party_AnyItemBelow99](../functions/Party_AnyItemBelow99.md) | `0x1402D6688` | Answers whether any item held by the party has reached a high count. |
| [PoachersDen_AddStock](../functions/PoachersDen_AddStock.md) | `0x140287564` | Adds a signed delta to the Poachers' Den stock count of one item id and returns the resulting count, clamped to the byte range the store uses; the shop list builder calls it with a zero delta, so in the shop path it i... |
| [PoachList_Build](../functions/PoachList_Build.md) | `0x1401AFFC4` | Builds the poacher shop's list: one 48-byte entry for each poach id (1..96) with a non-zero held count. |
| [PoachRow_SetMonsterIcon](../functions/PoachRow_SetMonsterIcon.md) | `0x1402A4508` | Sets the monster icon of a poacher list row. |
| [PoachSell_FillRow](../functions/PoachSell_FillRow.md) | `0x1401B2140` | Fills one row of the poacher sell list. |
| [PoachSell_ShowTotal](../functions/PoachSell_ShowTotal.md) | `0x1401B23A0` | Shows the sale total of the poacher sell screen. |
| [PoachTable_GetRowById](../functions/PoachTable_GetRowById.md) | `0x1402B8A78` | Returns the PoachItem-en row for a poach type through the shared NXD table interface. |
| [PoachTip_Fill](../functions/PoachTip_Fill.md) | `0x14029BE00` | Fills the poach help tip. |
| [Shop_BuildItemList](../functions/Shop_BuildItemList.md) | `0x140288E54` | Builds the item id list of one shop or of the Poachers' Den into a caller-supplied buffer, applying the shop mask, the story-progress gate, a menu-category filter and an optional equipment check, and returns the numbe... |
| [Shop_GetUiRowId](../functions/Shop_GetUiRowId.md) | `0x1402ACA48` | Maps a shop number to the UI table row that holds its name and description: the two special shops get fixed rows and every ordinary shop uses the common row. |
| [Shop_Open](../functions/Shop_Open.md) | `0x1402C35FC` | Opens the shop screen for a shop number: it stores the id, resolves the real shop from the event variable when the id is not special, builds the list and the panels and starts the shop task. |
| [ShopEntry_Fill](../functions/ShopEntry_Fill.md) | `0x14036B2D0` | Fills the 40-byte shop list entry of list index `index`: id and counts (ShopEntry_InitFromList), price, flags; then stores it in the list gadget. |
| [ShopEntry_InitFromList](../functions/ShopEntry_InitFromList.md) | `0x14028B65C` | Starts a shop entry from list word `index` of word_141811470: the id (masked 0x3FF), the index and the equipped and owned counts. |
| [StatusLists_BuildOrder](../functions/StatusLists_BuildOrder.md) | `0x1400F8E94` | Once per run, builds the three display-order key lists the equipment detail lines use. |
| [sub_1400D6FB0](../functions/sub_1400D6FB0.md) | `0x1400D6FB0` | Adjusts the count of one poach type, clamps it, and keeps the two ordered poach lists in step when a type enters or leaves the collection. |
| [sub_1400ED3E8](../functions/sub_1400ED3E8.md) | `0x1400ED3E8` | Returns the equip screen's current slot selector: the byte at the UI object's `+0xF1C`, or 0 when the UI module is not up. |
| [sub_1400ED4BC](../functions/sub_1400ED4BC.md) | `0x1400ED4BC` | Returns the item screen's current list mode: the dword at the UI object's `+0x12EC`, or 0 when the module is not up. |
| [sub_1400FB93C](../functions/sub_1400FB93C.md) | `0x1400FB93C` | Fills a caller structure with an item's record and its category sub-record: the numbers the equip detail panel prints. |
| [sub_1400FB9F0](../functions/sub_1400FB9F0.md) | `0x1400FB9F0` | Classifies an item into the equipment slot group it belongs to, and writes the id and the group into a two-dword structure. |
| [sub_140134DA8](../functions/sub_140134DA8.md) | `0x140134DA8` | Resolves one row of a small UI table from the key held on a screen object and a mode index, and returns the row's dword at `+0x0C`. |
| [sub_140153CA0](../functions/sub_140153CA0.md) | `0x140153CA0` | Binds one item or ability to a UI cell: it sets the cell's icon path and name from a 16-bit text id, reads the inventory count for an item, and records the cell state. |
| [sub_1401ABE14](../functions/sub_1401ABE14.md) | `0x1401ABE14` | Rebuilds the row list of the Poachers' Den screen from the saved poach ordering, taking a vector of 40-byte entry records as its input. |
| [sub_1401AEEF0](../functions/sub_1401AEEF0.md) | `0x1401AEEF0` | Refreshes the equip and possession detail panel for one item, including its shop-new flag, and rebuilds the panel's text and icon slots. |
| [sub_140278FEC](../functions/sub_140278FEC.md) | `0x140278FEC` | Inventory count plus the copies worn by roster units and by the battle units. |
| [sub_140285B10](../functions/sub_140285B10.md) | `0x140285B10` | Sorts a 0xFFFF-terminated item list in place by one of eight preset field orders. |
| [sub_140285F2C](../functions/sub_140285F2C.md) | `0x140285F2C` | Copies the shared display list into the saved order list of one menu group, so that the order the player left the menu list in becomes the stored order. |
| [sub_140286070](../functions/sub_140286070.md) | `0x140286070` | The equipment-order twin of the item synchroniser: it applies the owned/not-owned rule to the equipment order list of one group. |
| [sub_140286160](../functions/sub_140286160.md) | `0x140286160` | Applies the owned/not-owned rule to the obtain-order list, the single list that records the order in which items were first acquired. |
| [sub_140286228](../functions/sub_140286228.md) | `0x140286228` | Sorts the shared display list by one chosen field, or rebuilds it in obtain order. |
| [sub_140286C8C](../functions/sub_140286C8C.md) | `0x140286C8C` | Fills an item descriptor from the record table and the sub-record that matches the item's category. |
| [sub_1402875A4](../functions/sub_1402875A4.md) | `0x1402875A4` | The alternate candidate filler: it builds the five equip candidates from the equipment inventory list (mode 3, no bit-14 marks), sorts each category's stack list and copies the chosen ids into the output. |
| [sub_140287D9C](../functions/sub_140287D9C.md) | `0x140287D9C` | Builds the Outfitter's candidate list for the selected unit and shop: five category lists are merged, ordered, and the first four output words are marked with bit 15 when they differ from the live and override words. |
| [sub_1402890C0](../functions/sub_1402890C0.md) | `0x1402890C0` | The menu group of an item from its category. |
| [sub_14028B180](../functions/sub_14028B180.md) | `0x14028B180` | Compares two item ids by one named record field and returns a signed ordering value. |
| [sub_14028B354](../functions/sub_14028B354.md) | `0x14028B354` | Produces the numeric sort key of one item for one field. |
| [sub_14028B510](../functions/sub_14028B510.md) | `0x14028B510` | Marks the items sold in any open shop. |
| [sub_1402B8C74](../functions/sub_1402B8C74.md) | `0x1402B8C74` | Returns the 8-byte weapon sub-record (I: range, attack flags, formula, -, power, evade, element, status effect), or null when the item is not of this kind. |
| [sub_1402B8CD4](../functions/sub_1402B8CD4.md) | `0x1402B8CD4` | Returns the 2-byte shield sub-record (copied into the unit's evade group, I: physical / magic evade), or null when the item is not of this kind. |
| [sub_1402B8D3C](../functions/sub_1402B8D3C.md) | `0x1402B8D3C` | Returns the 2-byte head / body sub-record (added to the unit's max HP / MP, capped 999: Unit_ApplyEquipment), or null when the item is not of this kind. |
| [sub_1402B8DA0](../functions/sub_1402B8DA0.md) | `0x1402B8DA0` | Returns the 2-byte accessory sub-record (copied into the unit's evade group), or null when the item is not of this kind. |
| [sub_1402B8E04](../functions/sub_1402B8E04.md) | `0x1402B8E04` | Returns the 3-byte usable-item sub-record (I: formula, amount, status record index into the 6-byte table at 0x14080FBA0), or null when the item is not of this kind. |
| [sub_1402C60E4](../functions/sub_1402C60E4.md) | `0x1402C60E4` | Reconciles a unit's equipment words with the inventory: every equipped item is counted, duplicates beyond the cap are sold, and the unit's slots are cleared afterwards. |
| [sub_1402C8010](../functions/sub_1402C8010.md) | `0x1402C8010` | Sells the equipment a unit owns beyond the 99-per-item cap, the equip-side twin of the inventory overflow pass. |
| [sub_1402C80D8](../functions/sub_1402C80D8.md) | `0x1402C80D8` | Counts the copies of an item a unit has equipped, used by the equip screens to show whether another copy is available. |
| [sub_1402C9F78](../functions/sub_1402C9F78.md) | `0x1402C9F78` | Takes a snapshot of the inventory counts that the battle code reads while the item menu is open. |
| [sub_1402EEC2C](../functions/sub_1402EEC2C.md) | `0x1402EEC2C` | Sums the prices of the five items a party unit has equipped and adds a fixed base amount. |
| [sub_14030CF38](../functions/sub_14030CF38.md) | `0x14030CF38` | Adds an item's sale value to the gil total: a quarter of the item price, added to scene variable 44 and clamped. |
| [sub_14031EF70](../functions/sub_14031EF70.md) | `0x14031EF70` | Initialises the item order state at the start of a game: it terminates the five saved item order lists, clears the whole equipment order block, terminates its five lists, and re-creates the sort-field lists the menu s... |
| [sub_140332C54](../functions/sub_140332C54.md) | `0x140332C54` | A shop row helper: it returns the party's total holding of the item shown in a shop list row, with a flag bit for whether it can be equipped. |
| [sub_140332C8C](../functions/sub_140332C8C.md) | `0x140332C8C` | The equipped-count twin of the shop row helper: it returns how many copies of the row's item the party has equipped, with the same flag bit. |
| [sub_140332CD0](../functions/sub_140332CD0.md) | `0x140332CD0` | Fills the shop row's category text from the item in the global shop list. |
| [sub_140332D48](../functions/sub_140332D48.md) | `0x140332D48` | Draws the item icon for a shop list row. |
| [sub_140333974](../functions/sub_140333974.md) | `0x140333974` | A shop list gadget handler: it edits the shop's displayed list and emits the message token for the item it acts on. |
| [sub_1403348A0](../functions/sub_1403348A0.md) | `0x1403348A0` | Item-menu command handler: it reacts to the current menu command read from the UI core, opens the shop or the list, and advances the menu state. |
| [sub_140334A48](../functions/sub_140334A48.md) | `0x140334A48` | Refreshes the shop's equip-detail panel: it builds the shop row entries for the selected unit, synchronises the item order group and updates the counts shown beside each row. |
| [sub_140335604](../functions/sub_140335604.md) | `0x140335604` | Draws a shop row's text: it resolves the row's item id and passes it, with the row's text context, to the draw call. |
| [sub_140338060](../functions/sub_140338060.md) | `0x140338060` | Fills the shop menu list: it counts the shop's entries and appends one UI list cell per entry. |
| [sub_14033FB84](../functions/sub_14033FB84.md) | `0x14033FB84` | Re-initialises a block of small per-entity records and clears a 0xA0-byte area beside them; it is called from the main loop. |
| [sub_140344B68](../functions/sub_140344B68.md) | `0x140344B68` | World-map / shop update (large); the part studied decides whether a shop has new items. |
| [sub_140345FE4](../functions/sub_140345FE4.md) | `0x140345FE4` | Opens the shop: it resets the three shop counters, reads the shop id, selects its 0x5C-byte record and starts the shop task. |
| [sub_140346524](../functions/sub_140346524.md) | `0x140346524` | Clears the shop "new" badges and the poach "new" marks after the player has been through a shop or the den. |
| [sub_14036A924](../functions/sub_14036A924.md) | `0x14036A924` | Returns the party's total holding of the item in the currently selected shop list row. |
| [sub_14036A95C](../functions/sub_14036A95C.md) | `0x14036A95C` | Returns how many copies of the selected shop row's item the party has equipped. |
| [sub_14036A994](../functions/sub_14036A994.md) | `0x14036A994` | Returns the price of the item in a shop list row, with the list's cannot-equip flag reported separately. |
| [sub_14036A9D8](../functions/sub_14036A9D8.md) | `0x14036A9D8` | Opens the shop's buy screen: it builds the shop's item list from the current shop number, fills the row entries in buy mode and binds the list to its gadget and callbacks. |
| [sub_14036AC74](../functions/sub_14036AC74.md) | `0x14036AC74` | Takes the shop row at the current selection index and makes it the active item of the shop's detail and confirmation panels. |
| [sub_14036B5D0](../functions/sub_14036B5D0.md) | `0x14036B5D0` | Refills the shop list's 40-byte row entries from the existing list buffer without rebuilding the item list, used after a change that leaves the ids in place. |
| [sub_14036B71C](../functions/sub_14036B71C.md) | `0x14036B71C` | Shop menu command handler: a switch on the command word drives buy, sell, equip and exit, and updates the shop list and the inventory. |
| [sub_14036C3EC](../functions/sub_14036C3EC.md) | `0x14036C3EC` | Builds the item list for one shop tab, choosing between the shop's stock list and the party's inventory depending on a flag, and returns the number of ids produced. |
| [sub_14036C468](../functions/sub_14036C468.md) | `0x14036C468` | Returns the sell price of the shop row the player has selected, for the sell confirmation panel. |
| [sub_14036C49C](../functions/sub_14036C49C.md) | `0x14036C49C` | Opens the shop's sell screen: it builds the tab-zero list from the party inventory, fills the entries in sell mode and binds the list for the sell panel. |
| [sub_14036E5DC](../functions/sub_14036E5DC.md) | `0x14036E5DC` | The shop screen's refresh: it decides which of the thirty shop slots are open, rebuilds a five-category list for each one to learn which item categories it can show, and redraws the shop gadget and its rows. |
| [sub_140393250](../functions/sub_140393250.md) | `0x140393250` | The item screen's row-icon callback: it maps one list index to the item record's category byte and publishes the two palette bytes and the fixed icon state the row draw reads. |
| [sub_1403932C8](../functions/sub_1403932C8.md) | `0x1403932C8` | The item screen's second row-icon callback: it takes one list index, masks the table word to an item id and hands it to `ItemIcon_Set`. |
| [sub_140396174](../functions/sub_140396174.md) | `0x140396174` | Copies the 261 inventory counts to byte_143C52740 and adds every item worn by a used roster entry. |
| [sub_140396748](../functions/sub_140396748.md) | `0x140396748` | A second copy of the order-list filter, working on the possession list instead of the shared display list. |
| [sub_14039684C](../functions/sub_14039684C.md) | `0x14039684C` | A second synchroniser for the saved item order lists. |
| [sub_140396FEC](../functions/sub_140396FEC.md) | `0x140396FEC` | Builds the item screen's 256-word list `word_141D32F00` for one category: it walks the item-id space, keeps the owned ids of the category, marks preview-unequippable entries with bit 14, terminates the list, and optio... |

## Structures (28)

| Name | Size (bytes) | Summary |
|---|---|---|
| [CategoryIconCell](../structs/CategoryIconCell.md) | 2 | One row of the ItemCategoryIconCells table. |
| [EquipmentOrderListPointer](../structs/EquipmentOrderListPointer.md) | 8 | One row of the EquipmentOrderLists table. |
| [EquipSetBlock](../structs/EquipSetBlock.md) | 64 | The equip screen's computed set at 0x141876C40: stat deltas at +0x00..+0x23, the five candidate equipment words at +0x24..+0x2D, a five-word display array at +0x2E..+0x37, and unclassified words at +0x38..+0x3F. It is... |
| [InflictRecordRow](../structs/InflictRecordRow.md) | 6 | One added-effect record. |
| [ItemAccessoryRow](../structs/ItemAccessoryRow.md) | 2 | Accessory sub-record. |
| [ItemArmorRow](../structs/ItemArmorRow.md) | 2 | Armor sub-record. |
| [ItemAttributeRow](../structs/ItemAttributeRow.md) | 26 | Equipment attribute record. |
| [ItemCategoryFirstIdRow](../structs/ItemCategoryFirstIdRow.md) | 2 | First item id of one category. |
| [ItemCategoryTypeRow](../structs/ItemCategoryTypeRow.md) | 4 | Record kind of one category. |
| [ItemChemistRow](../structs/ItemChemistRow.md) | 3 | Chemist item sub-record. |
| [ItemEquipPaletteRow](../structs/ItemEquipPaletteRow.md) | 2 | Palette selector of one item. |
| [ItemKindFirstCategoryRow](../structs/ItemKindFirstCategoryRow.md) | 4 | First category of one kind. |
| [ItemNewFlagBlock](../structs/ItemNewFlagBlock.md) | 1007 | The block at g_ItemNewFlags: the shop new-item flags first, then the four Poachers' Den (poach) arrays. |
| [ItemOrderLists](../structs/ItemOrderLists.md) |  | The ten saved item order lists: 16-bit words in static storage, no header and no length word. |
| [ItemRecord](../structs/ItemRecord.md) | 12 | The 12-byte record of an item (Item_GetRecord): icon, level, equipment slot bits, equipment category, attribute index, price and the story progress it is sold from. |
| [ItemShieldRow](../structs/ItemShieldRow.md) | 2 | Shield sub-record. |
| [ItemShopMaskRow](../structs/ItemShopMaskRow.md) | 2 | Shop availability of one item. |
| [ItemWeaponRecord](../structs/ItemWeaponRecord.md) | 8 | The 8-byte weapon sub-record of an item whose category kind is 0 or 5 (sub_1402B8C74). |
| [MenuListWord](../structs/MenuListWord.md) | 2 | One entry of g_MenuList, the array the shop, equip, item and ability screens reuse: the id in bits 0..9, bit 14 "cannot equip / cannot learn / current", and the list-kind-specific bits 12 and 13. |
| [NxdDataBookRow](../structs/NxdDataBookRow.md) | 44 | One row of the nxd.book table (English text table; the other languages share the layout). |
| [NxdDataItemRow](../structs/NxdDataItemRow.md) | 48 | One row of the nxd.item table (English text table; the other languages share the layout). |
| [NxdDataPoachItemRow](../structs/NxdDataPoachItemRow.md) | 56 | One row of the nxd.poach_item table (English text table; the other languages share the layout). |
| [NxdDataZodiacStoneOwnerTimelineRow](../structs/NxdDataZodiacStoneOwnerTimelineRow.md) | 16 | One row of the nxd.zodiac_stone_owner_timeline table (data table). |
| [NxdDataZodiacStoneRow](../structs/NxdDataZodiacStoneRow.md) | 40 | One row of the nxd.zodiac_stone table (English text table; the other languages share the layout). |
| [PartyHandWord](../structs/PartyHandWord.md) | 2 | One equipment slot of a party unit: the item id in bits 0..9 and bit 15 as the Outfitter-session pending flag. |
| [PoachListEntry](../structs/PoachListEntry.md) | 48 | One entry of the poacher list that PoachList_Build fills: a poach id the party holds. |
| [ShopEntry](../structs/ShopEntry.md) | 40 | One entry of a shop item list (buy, sell or equip), built per list index by ShopEntry_Fill from word_141811470 and drawn by ShopItemList_DrawRow. |
| [ShopRowCallbackTable](../structs/ShopRowCallbackTable.md) | 56 | The seven qword row handlers at 0x141876AD0..0x141876B00 that the list gadget calls per visible row; the shop, equip and item screens install different functions in the same slots. |

## Globals (29)

| Name | Address | Type | Summary |
|---|---|---|---|
| [dword_143D1AC68](../globals/dword_143D1AC68.md) | `0x143D1AC68` | `int32` | Running price accumulator of an Outfitter equip visit: a positive charge for equipment bought or applied during the visit, added to gil and zeroed by the commit handler. |
| [g_AbilityKind1_ItemByAbility](../globals/g_AbilityKind1_ItemByAbility.md) | `0x140785E18` | `uint8[14]` | The Item-command table: 14 bytes, ability 368 + i maps to item 240 + i (items 240..253). |
| [g_AbilityKind2_ThrowCategory](../globals/g_AbilityKind2_ThrowCategory.md) | `0x140789290` | `uint8[12]` | The Throw table: 12 equip-category bytes, ability 382 + i maps to one category. |
| [g_EquipCandidates](../globals/g_EquipCandidates.md) | `0x141876C64` | `uint16[5]` | The five candidate equipment words of the equip screen's preview; filled by the picker or zeroed, then read by the caller after the call. |
| [g_EquipOrderGroup](../globals/g_EquipOrderGroup.md) | `0x140D407BA` | `uint8` | The equip screen's order-group byte; cleared when the player picks a row, so the list order follows the chosen row. |
| [g_EquipScreenInitFlag](../globals/g_EquipScreenInitFlag.md) | `0x14184A643` | `uint8` | One-shot setup byte of the equip screen's row-selection path. |
| [g_EquipSet](../globals/g_EquipSet.md) | `0x141876C40` | `?` | The equip-set structure the preview picker fills and passes to sub_140287354 together with the candidate buffer and the unit's live equipment words. |
| [g_HelpIdSlot](../globals/g_HelpIdSlot.md) | `0x1418736B4` | `int32` | The item help-id slot of the shop detail panel: 0x6800 plus the per-item help word when the table word is non-zero, -1 when the item has no help. |
| [g_InventoryCounts](../globals/g_InventoryCounts.md) | `0x1411A7C00` | `uint8[261]` | The party's inventory: one count per item id 0..260, saved with the game. |
| [g_InventorySnapshot](../globals/g_InventorySnapshot.md) | `0x143C52740` | `uint8[261]` | Inventory counts plus every item worn by a used roster entry, built by sub_140396174 (261 counts). |
| [g_ItemAttributeTable](../globals/g_ItemAttributeTable.md) | `0x14080FEA0` | `uint8[85][26]` | The equipment attribute records: 85 rows of 26 bytes, selected by the item record attribute index. |
| [g_ItemNewFlags](../globals/g_ItemNewFlags.md) | `0x1411A7810` | `uint8[261][2]` | Two flag bytes per item id 0..260, set at a new game; I: the shop 'new item' badges (byte 1 cleared when the item is first sold, byte 0 when it is first obtained). |
| [g_ItemShopMask](../globals/g_ItemShopMask.md) | `0x14067F890` | `uint8[512]` | Which shops sell which item: two bytes per item id 0..0xFF, a mask word whose bit for shop s is 0x8000 >> s. |
| [g_ListSelectedRow](../globals/g_ListSelectedRow.md) | `0x141876B50` | `uint16` | The list gadget's selected-row word as bound by the shop screens. |
| [g_ListSelectedRowIndex](../globals/g_ListSelectedRowIndex.md) | `0x141876B54` | `uint16` | The selected row index the shop row helpers read; the shop list entry at that row is the one they price, count and copy. |
| [g_MenuList](../globals/g_MenuList.md) | `0x141811470` | `uint16[256]` | The display list shared by the shop and the equip screens: up to 256 packed words, 0xFFFF-terminated, rebuilt whenever a screen opens and never saved. |
| [g_PoachCount](../globals/g_PoachCount.md) | `0x1411A7A1A` | `uint8[97]` | Poach count per type, 97 bytes based at the badge block plus 522; the poach add routine clamps each byte to 99. |
| [g_PoachDirty](../globals/g_PoachDirty.md) | `0x1411A7283` | `uint8` | Byte the poach badge routine sets to record that a type's new flag changed, so the den screen refreshes. |
| [g_PoachersDenStock](../globals/g_PoachersDenStock.md) | `0x1411A7700` | `uint8[261]` | Poachers' Den stock: one count per item id 0..260 (PoachersDen_AddStock adds to it, clamped 0..255); the shop list builder Shop_BuildItemList lists the ids with stock when the shop id is 100 or above. |
| [g_PoachNewFlags](../globals/g_PoachNewFlags.md) | `0x1411A7B3D` | `uint16[97]` | Two new-flag bytes per poach type at the badge block plus 813; a new game fills them with 0x0101 and the badge routine clears the high byte. |
| [g_PoachOrder](../globals/g_PoachOrder.md) | `0x1411A7A7B` | `uint8[97]` | The player-visible order of collected poach types, 97 bytes at the badge block plus 619; maintained together with the sort list. |
| [g_PoachSort](../globals/g_PoachSort.md) | `0x1411A7ADC` | `uint8[97]` | The user reordering of the poach types, 97 bytes at the badge block plus 716. |
| [g_SelectedShopIndex](../globals/g_SelectedShopIndex.md) | `0x141811684` | `uint16` | The selected shop number the shop screens pass to Shop_BuildItemList and sub_1402D7640. |
| [g_SelectedUnitIndex](../globals/g_SelectedUnitIndex.md) | `0x141811428` | `uint16` | The selected unit index the item, shop and equip screens read as their unit argument (sub_140287D9C, sub_1402D7640, sub_1403331F8, sub_140333FE0, sub_140366FE0). |
| [g_SellScreenActive](../globals/g_SellScreenActive.md) | `0x141874A14` | `uint16` | Non-zero while the sell screen owns a list; the row price helper returns 0 without reading the list while it is zero. |
| [g_ShopModeGate](../globals/g_ShopModeGate.md) | `0x1407D453C` | `uint32` | Global mode word that gates the shop and den badge refresh; the badge routine runs only while it is non-zero. |
| [g_ShopOrderGroup](../globals/g_ShopOrderGroup.md) | `0x140D408E7` | `uint8` | The buy and sell screens' current order-group byte; cleared when a screen's list is first bound so the list starts in its default order. |
| [g_ShopRowCallbacks](../globals/g_ShopRowCallbacks.md) | `0x141876AD0` | `ptr[?]` | The buy screen's row handler table (0x141876AD0 through 0x141876B00): one handler per row column, filled at first entry to the screen. |
| [g_ShopScreenInitFlag](../globals/g_ShopScreenInitFlag.md) | `0x14184A641` | `uint8` | One-shot setup byte of the buy and sell screens: the first entry builds the rows, later entries keep the existing list and scroll position. |

## Registries (2)

| Name | Summary |
|---|---|
| [ItemCategories](../registries/ItemCategories.md) | The item categories: the stock first-id thresholds of Item_FindCategoryIndex, the record kind of each category (which sub-record table it has) and the menu group sub_1402890C0 gives it. |
| [ItemClassNumbers](../registries/ItemClassNumbers.md) | The item class numbers (item class n is allowed to a job when bit 7 - n % 8 of byte n / 8 of its exe.job equip_flags is set; the class is the equip_category of the item's exe.item row) with their names. |

## Flows (2)

| Name | Summary |
|---|---|
| [EquipSessionFlagFlow](../flows/EquipSessionFlagFlow.md) | The Outfitter/equip session: build candidates, buy or apply a slot word with bit 15, then commit (strip the bit, charge the price, save) or cancel (restore the override). |
| [ItemMenuListLifecycle](../flows/ItemMenuListLifecycle.md) | Where a shop or equip list word is written, reordered and read: one producer fills g_MenuList for the screen, the saved-order filter rewrites it right after a mode-1 build, and seven functions read single words back, ... |

## Observed behaviours (9)

| Name | Scope | Summary |
|---|---|---|
| [EquipListsDropRowsAUnitCannotEquip](../behaviors/EquipListsDropRowsAUnitCannotEquip.md) | engine (equip lists) | The Outfitter Fitting list and the Status screen's equipment list leave out the items the unit cannot equip; they do not show them greyed. |
| [EquipSessionFlagLifecycle](../behaviors/EquipSessionFlagLifecycle.md) | the five party equipment words, the override array and the candidate array during an Outfitter or shop session | Bit 15 marks a slot changed in the current session and priced into dword_143D1AC68; bit 14 is a list-entry 'cannot equip' mark. |
| [ItemCommandRelation](../behaviors/ItemCommandRelation.md) | how the Item command and Throw turn an item id into an ability id and back | An Item-command use is an item id plus a paired ability id: the table maps abilities 368..381 to items 240..253, while at use the engine computes ability = item + 0x80 and the current-action builder computes item = ab... |
| [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md) | the shop lists and the equipment detail panel for an item id | What a shop row and the detail panel show for an item, all keyed by the item id: name and description from the Item-en row, price from the item record, icon files named by the id. |
| [ItemIdSpace](../behaviors/ItemIdSpace.md) | the item functions and every bound on an item id | Item ids are u16 wherever they are stored for units (roster, party, battle and preview records), but the code bounds them in three ways: the item functions serve 0..0x104 (two stock record arrays split at 0x100), abou... |
| [ItemMenuListWordMarkOverlapsLargeIds](../behaviors/ItemMenuListWordMarkOverlapsLargeIds.md) | engine (shop and equip list) | A shop or equip list word holds the item id in its low bits and the 'cannot equip' mark in bit 14; an item id can be up to 15 bits wide, so for an id of 16,384 and above the id's own bit 14 and the mark are the same bit. |
| [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md) | g_MenuList and the three list kinds that reuse it (shop, equip, ability), plus the job list | The two high bits of the 16-bit list words are per-list-kind state, not part of the id: bit 14 is cannot-equip / cannot-learn / current, bit 15 is not written to g_MenuList at all but marks the equip-candidate buffers. |
| [OrderInsideItemGroup](../behaviors/OrderInsideItemGroup.md) | the order of item ids inside one menu group (the item menu, the equip screen and the shop list) | Three rules decide the order, in this priority: the saved order list is the order, membership maintenance inserts a newly owned id at the front and removes a lost one, and an explicit sort replaces the order with a fi... |
| [OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag](../behaviors/OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag.md) | engine (Outfitter preview) | The Outfitter preview builder, the equip-clear price step and the equip commit each reduce a party hand word to an item id with an AND that must strip the session flag (bit 15); an AND whose mask keeps bit 15 turns th... |

## Tables (33)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [EquipmentOrderListPointers](../tables/EquipmentOrderListPointers.md) | Executable |  | 4 rows of 8 bytes | Pointers to the four saved equipment order lists; the next eleven pointers of the run belong to other lists. |
| [InflictRecords](../tables/InflictRecords.md) | Executable |  | 128 rows of 6 bytes | Statuses an attack, item or ability inflicts or cures. |
| [InventoryCounts](../tables/InventoryCounts.md) | Executable memory (saved with the game) |  | 261 entries of 1 byte | The party's inventory: one count per item id 0..260, saved with the game. |
| [Item](../tables/Item.md) | NXD file | 45 |  | The item rows (the Item-en table), read through ItemTable_GetRow and ItemTable_GetRowById and used by the text resolver for the category 'Item'. The item records the game keeps in the executable are a separate table. |
| [ItemAccessoryRecords](../tables/ItemAccessoryRecords.md) | Executable |  | 32 records of 2 bytes (ids 0xD0..0xEF) | Accessory evade values. |
| [ItemAccessoryRecordsHigh](../tables/ItemAccessoryRecordsHigh.md) | Executable |  | 1 record of 2 bytes (id 0x104) | Accessory sub-record of item 260. |
| [ItemArmorRecords](../tables/ItemArmorRecords.md) | Executable |  | 64 records of 2 bytes (ids 0x90..0xCF) | Head and body armor HP and MP bonuses. |
| [ItemArmorRecordsHigh](../tables/ItemArmorRecordsHigh.md) | Executable |  | 2 records of 2 bytes (ids 0x102, 0x103) | Armor sub-records of items 258 and 259. |
| [ItemAttributes](../tables/ItemAttributes.md) | Executable |  | 85 rows of 26 bytes | Equipment attribute records: stat, move and jump bonuses, status groups and elements an item adds to its wearer. |
| [ItemCategoryFirstIds](../tables/ItemCategoryFirstIds.md) | Executable |  | 14 rows of 2 bytes | First item id of every category: Item_FindCategoryIndex returns the last category whose first id is not above the item id (entries 1..12 are compared). |
| [ItemCategoryIconCells](../tables/ItemCategoryIconCells.md) | Executable |  | 40 rows of 2 bytes (rows 0..36 used) | Texture position of the category icon drawn beside each shop item row. |
| [ItemCategoryTypes](../tables/ItemCategoryTypes.md) | Executable |  | 14 rows of 4 bytes | Record kind of each category: which sub-record table an item of the category has. |
| [ItemChemistRecords](../tables/ItemChemistRecords.md) | Executable |  | 16 records of 3 bytes (ids 0xF0..0xFF) | Formula, amount and inflict index of the chemist items (the Item-command items 240..253 and two more). |
| [ItemEquipPalettes](../tables/ItemEquipPalettes.md) | Executable |  | 145 records of 2 bytes (ids 0..0x8F) | Palette selectors of weapons and shields. |
| [ItemEquipPalettesHigh](../tables/ItemEquipPalettesHigh.md) | Executable |  | 2-byte rows, count not established | Palette selectors read by Item_GetEquipPalette for the kinds 4 and 5. |
| [ItemKind6Records](../tables/ItemKind6Records.md) | Executable |  | 0 records (empty range) | Base of the kind 6 sub-records. |
| [ItemKind9Records](../tables/ItemKind9Records.md) | Executable |  | 0 records (empty range) | Base of the kind 9 sub-records. |
| [ItemKindFirstCategories](../tables/ItemKindFirstCategories.md) | Executable |  | 10 rows of 4 bytes | First category of each record kind. |
| [ItemNewFlags](../tables/ItemNewFlags.md) | Executable memory (saved with the game) |  | 261 rows of 2 entries of 1 byte | Two flag bytes per item id 0..260, set at a new game; I: the shop 'new item' badges (byte 1 cleared when the item is first sold, byte 0 when it is first obtained). |
| [ItemRecords](../tables/ItemRecords.md) | Executable |  | 261 records of 12 bytes | The item records the executable keeps for equipment and chemist data. |
| [ItemShieldRecords](../tables/ItemShieldRecords.md) | Executable |  | 16 records of 2 bytes (ids 0x80..0x8F) | Shield evade values. |
| [ItemShopMask](../tables/ItemShopMask.md) | Executable |  | 256 rows of 2 bytes | Which shops sell which item: a mask word whose bit for shop s is 0x8000 >> s. |
| [ItemWeaponRecords](../tables/ItemWeaponRecords.md) | Executable |  | 128 records of 8 bytes (ids 0..0x7F) | Weapon sub-records of the first 128 items; two more in ItemWeaponRecordsHigh. |
| [ItemWeaponRecordsHigh](../tables/ItemWeaponRecordsHigh.md) | Executable |  | 2 records of 8 bytes (ids 0x100, 0x101) | Weapon sub-records of items 256 and 257. |
| [NxdDataBook](../tables/NxdDataBook.md) | NXD file | 148 | 5 rows of 44 bytes, text in 7 languages | The five lore books: titles, descriptions, icon and sound references. |
| [NxdDataZodiacStone](../tables/NxdDataZodiacStone.md) | NXD file | 119 | 27 rows of 40 bytes, text in 7 languages | Zodiac stones keyed by stone and variant: condition link, owner timeline, name, summary, description and icons. |
| [NxdDataZodiacStoneOwnerTimeline](../tables/NxdDataZodiacStoneOwnerTimeline.md) | NXD file | 238 | 11 rows of 16 bytes | Zodiac stone owner timelines (11). |
| [PoachCount](../tables/PoachCount.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | Poach count per type, 97 bytes based at the badge block plus 522; the poach add routine clamps each byte to 99. |
| [PoachersDenStock](../tables/PoachersDenStock.md) | Executable memory (saved with the game) |  | 261 entries of 1 byte | Poachers' Den stock: one count per item id 0..260 (PoachersDen_AddStock adds to it, clamped 0..255); the shop list builder Shop_BuildItemList lists the ids with stock when the shop id is 100 or above. |
| [PoachItem](../tables/PoachItem.md) | NXD file | 236 |  | The poach rows (the PoachItem-en table), read through PoachTable_GetRowById. |
| [PoachNewFlags](../tables/PoachNewFlags.md) | Executable memory (saved with the game) |  | 97 entries of 2 bytes | Two new-flag bytes per poach type at the badge block plus 813; a new game fills them with 0x0101 and the badge routine clears the high byte. |
| [PoachOrder](../tables/PoachOrder.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | The player-visible order of collected poach types, 97 bytes at the badge block plus 619; maintained together with the sort list. |
| [PoachSort](../tables/PoachSort.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | The user reordering of the poach types, 97 bytes at the badge block plus 716. |
