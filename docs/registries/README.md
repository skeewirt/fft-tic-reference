# Registries

Name-to-id tables the engine builds at runtime (sampler, texture and constant-buffer slots, ...): every entry with its id, its value and its meaning.

12 records. Format of a record: [kinds/registry.json](../../kinds/registry.json). Data: [data/registries.jsonl](../../data/registries.jsonl).

| Name | Area | Summary |
|---|---|---|
| [AbilityAuxFlagBits](AbilityAuxFlagBits.md) | [Ability data](../areas/ability-data.md) | The meaning of the bits of exe.ability.aux flags3 (byte +3) and flags4 (u32 at +4) as named here: flags3 holds the ability type in bits 0..4 and three flags in bits 5..7, flags4 the AI behaviour flags, one bit each. |
| [AbilityTypes](AbilityTypes.md) | [Ability data](../areas/ability-data.md) | The ability type nibble in the low five bits of exe.ability.aux flags3, with names. |
| [BattleMsgKindBase](BattleMsgKindBase.md) | [Battle](../areas/battle.md) | The message-id base per descriptor kind for class 0 subtype 2: id = 1000 x kind + (word & 0x7FF). |
| [ItemCategories](ItemCategories.md) | [Items and shops](../areas/items.md) | The item categories: the stock first-id thresholds of Item_FindCategoryIndex, the record kind of each category (which sub-record table it has) and the menu group sub_1402890C0 gives it. |
| [ItemClassNumbers](ItemClassNumbers.md) | [Items and shops](../areas/items.md) | The item class numbers (item class n is allowed to a job when bit 7 - n % 8 of byte n / 8 of its exe.job equip_flags is set; the class is the equip_category of the item's exe.item row) with their names. |
| [JobIdSpace](JobIdSpace.md) | [Job data](../areas/job-data.md) | What a job id (the byte in save record +2 and work record +3) means to the code, and the job index the per-job arrays use for it. |
| [LayerPassKeys](LayerPassKeys.md) | [Graphics](../areas/graphics.md) | The pass constants OR-ed into the 64-bit sort key of the layer commands. |
| [NewUnitStartRows](NewUnitStartRows.md) | [Unit data](../areas/unit-data.md) | The four start rows that Unit_RollStartingStats reads: base and random span of the five stat accumulators in whole raw units, and the seven starting equipment words; a new unit's row is its kind (gender), never its job. |
| [SamplerSlots](SamplerSlots.md) | [Graphics](../areas/graphics.md) | The sampler names of the render device (31 live) and their slot ids. |
| [SpriteNumberTables](SpriteNumberTables.md) | [Graphics](../areas/graphics.md) | Every table the executable indexes by sprite number, with the row count, the bound the code applies. |
| [TextIdKinds](TextIdKinds.md) | [Data access](../areas/data.md) | The 32 text-id kinds: the 5 bits of a text id, their base (kind x 0x800) and the pool or source each selects. |
| [UIAnimCurves](UIAnimCurves.md) | [UI framework](../areas/ui-framework.md) | The easing curves of UI keyframes: curve id to blend function of the position t within a key interval (UIAnim_Curve). |
