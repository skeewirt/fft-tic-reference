# Registries

Name-to-id tables the engine builds at runtime (sampler, texture and constant-buffer slots, ...): every entry with its id, its value and its meaning.

30 records. Format of a record: [kinds/registry.json](../../kinds/registry.json). Data: [data/registries.jsonl](../../data/registries.jsonl).

| Name | Area | Summary |
|---|---|---|
| [AbilityAuxFlagBits](AbilityAuxFlagBits.md) | [Ability data](../areas/ability-data.md) | The meaning of the bits of exe.ability.aux flags3 (byte +3) and flags4 (u32 at +4) as named here: flags3 holds the ability type in bits 0..4 and three flags in bits 5..7, flags4 the AI behaviour flags, one bit each. |
| [AbilityTypes](AbilityTypes.md) | [Ability data](../areas/ability-data.md) | The ability type nibble in the low five bits of exe.ability.aux flags3, with names. |
| [AchievementNotificationTypes](AchievementNotificationTypes.md) | [UI framework](../areas/ui-framework.md) | The type number of each achievement notification class: the virtual function at +8 of the notification's vtable returns it, and the achievement classes compare it in their match functions. |
| [BattleMsgKindBase](BattleMsgKindBase.md) | [Battle](../areas/battle.md) | The message-id base per descriptor kind for class 0 subtype 2: id = 1000 x kind + (word & 0x7FF). |
| [BattleVoiceSuppressReason](BattleVoiceSuppressReason.md) | [Battle](../areas/battle.md) | The result of BattleVoice_IsSuppressed: 0 speak, or the reason a line is not spoken. |
| [ClassicSubtitleState](ClassicSubtitleState.md) | [UI framework](../areas/ui-framework.md) | The state names of the classic-movie subtitle window and the UIClassicSubtitles line_layout value that picks each. |
| [CreditLineType](CreditLineType.md) | [UI framework](../areas/ui-framework.md) | The line types of UICreditRow (line_type) and the builder CreditRoll_Step calls for each. |
| [GuideIconGlyph](GuideIconGlyph.md) | [UI framework](../areas/ui-framework.md) | The guide icon numbers (UIButtonGuide guide_icon / guide_icon_2) and the glyph GuideIcon_ToGlyph draws for them. |
| [InputContext](InputContext.md) | [Input](../areas/input.md) | The input contexts an action row can belong to: the row's mask against the module's context mask. |
| [ItemCategories](ItemCategories.md) | [Items and shops](../areas/items.md) | The item categories: the stock first-id thresholds of Item_FindCategoryIndex, the record kind of each category (which sub-record table it has) and the menu group sub_1402890C0 gives it. |
| [ItemClassNumbers](ItemClassNumbers.md) | [Items and shops](../areas/items.md) | The item class numbers (item class n is allowed to a job when bit 7 - n % 8 of byte n / 8 of its exe.job equip_flags is set; the class is the equip_category of the item's exe.item row) with their names. |
| [JobIdSpace](JobIdSpace.md) | [Job data](../areas/job-data.md) | What a job id (the byte in save record +2 and work record +3) means to the code, and the job index the per-job arrays use for it. |
| [KeyBindingFlag](KeyBindingFlag.md) | [Input](../areas/input.md) | The flag bits of a keyboard binding dword of an action row (low 16 bits = key code), set by InputRows_ApplyKeyBindings from the UIKeyAssign flag bytes. |
| [LayerPassKeys](LayerPassKeys.md) | [Graphics](../areas/graphics.md) | The pass constants OR-ed into the 64-bit sort key of the layer commands. |
| [MovieControllerFlag](MovieControllerFlag.md) | [UI framework](../areas/ui-framework.md) | The movie controller flag bits Movie_Start sets from the MovieData row (MovieController +24). |
| [NewUnitStartRows](NewUnitStartRows.md) | [Unit data](../areas/unit-data.md) | The four start rows that Unit_RollStartingStats reads: base and random span of the five stat accumulators in whole raw units, and the seven starting equipment words; a new unit's row is its kind (gender), never its job. |
| [SamplerSlots](SamplerSlots.md) | [Graphics](../areas/graphics.md) | The sampler names of the render device (31 live) and their slot ids. |
| [SpriteNumberTables](SpriteNumberTables.md) | [Graphics](../areas/graphics.md) | Every table the executable indexes by sprite number, with the row count, the bound the code applies. |
| [TextIdKinds](TextIdKinds.md) | [Data access](../areas/data.md) | The 32 text-id kinds: the 5 bits of a text id, their base (kind x 0x800) and the pool or source each selects. |
| [TextLanguageCodes](TextLanguageCodes.md) | [Data access](../areas/data.md) | The text language codes the game keeps at `g_LanguageInfo`+8, with the language pack and the name suffix each one selects. |
| [TextTagName](TextTagName.md) | [Data access](../areas/data.md) | The first 40 records of the UI text engine's tag-name table (16 bytes each: a name pointer and a flag dword). |
| [TitleMenuEntryKinds](TitleMenuEntryKinds.md) | [UI framework](../areas/ui-framework.md) | The six kinds of row of the Enhanced title menu: the kind byte stored in each row, the text id of its label (UI table, nxd id 19) and what choosing it does. |
| [TitleModeSelectButtons](TitleModeSelectButtons.md) | [UI framework](../areas/ui-framework.md) | The button ids of the mode select screen as `UILauncher_OnMenuAction` handles them. |
| [UIAddonRows](UIAddonRows.md) | [UI framework](../areas/ui-framework.md) | Rows of the screen table (`uiaddon.nxd`, nxd id 24) that the title screens use: each row's `path` names the layout file a screen loads. |
| [UIAnimCurves](UIAnimCurves.md) | [UI framework](../areas/ui-framework.md) | The easing curves of UI keyframes: curve id to blend function of the position t within a key interval (UIAnim_Curve). |
| [UIButtonGuideKeysOfGeneralOptions](UIButtonGuideKeysOfGeneralOptions.md) | [UI framework](../areas/ui-framework.md) | The guide bar keys (`UIButtonGuide` rows, UI table 33) the settings screen uses, with the text id of each sub-row; 'right' marks sub-rows drawn on the right (byte +37 `Unknown25`). |
| [UIDialogRowsOfSettings](UIDialogRowsOfSettings.md) | [UI framework](../areas/ui-framework.md) | The UIDialog rows (nxd 34, `UITable_GetRow(34, row)`) the settings screens and neighbours use, and the UI texts they quote. |
| [UISoundIdsOfSettings](UISoundIdsOfSettings.md) | [UI framework](../areas/ui-framework.md) | The UI sound ids (`sub_1400F4BCC(_, id)`, UI table 0x45) the settings screen plays. |
| [UnitEventFlagBit](UnitEventFlagBit.md) | [Unit data](../areas/unit-data.md) | The bits of the unit flag word at battle unit +504, which the battle build stores from the entry override row: one bit per flag byte (OverrideEntryData +0x8E..+0x97 and +0x99), plus bit 11 set by the equipment build. |
| [UnitIdentityIds](UnitIdentityIds.md) | [Unit data](../areas/unit-data.md) | A unit is identified by its marker (save record +0, the character template), not by its job (+2): the job changes, the marker stays. |
