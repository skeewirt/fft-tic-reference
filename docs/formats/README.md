# File formats

Layouts of the game's file formats (described, never copied): headers, records, string pools.

20 records. Format of a record: [kinds/format.json](../../kinds/format.json). Data: [data/formats.jsonl](../../data/formats.jsonl).

| Name | Extension | Summary |
|---|---|---|
| [BattleResumeImage](BattleResumeImage.md) | `.sav` | The payload of a resume entry of `autoenhanced.png`. |
| [ConfigCategoryTable](ConfigCategoryTable.md) | `.nxd` | `configcategory.nxd` (nxd 249): the tabs of the settings screens; `config_items` are the rows of a tab and `name_text` its title. |
| [ConfigItemTable](ConfigItemTable.md) | `.nxd` | `configitem.nxd` (nxd 250): one row per setting of the settings screens. |
| [ConfigScreenLayout](ConfigScreenLayout.md) | `.uib` | `ffto_config_enhanced_ver02.uib` and `ffto_config_parts.uib` (pack 0008): the layout of the settings screen and its row, switch, select and slider parts. |
| [EffectSoundTracks](EffectSoundTracks.md) |  | An effect file names its sounds in three places: three sound tracks in section 7 say when, a slot list in section 6 says which value, and section 8 gives the cue base. |
| [ItemHelpToken](ItemHelpToken.md) |  | The 0x6800-tagged text id that asks for an item's help string: kind 13, index = item id. |
| [ItemIconPath](ItemIconPath.md) | `.utexpt with .tex` | The two per-item picture paths: a detail picture (Icon table row 12) and a list picture (row 13), both formatted from the item id and both texture-parts URIs. |
| [ManualSaveEntry](ManualSaveEntry.md) | `.bin` | The `fftsave.bin` entry of `enhanced.png` (and of `classic.png`): one flat image of the 50-slot save cache, 50 x 40,164 bytes behind a 16-byte header. |
| [NxdMultiKeyIndex](NxdMultiKeyIndex.md) | `.nxd` | The index of a double or triple keyed nxd file (header byte 8 = 2 or 3): sets by key1, per set an array (double) or children by key2 with their leaves (triple), and one flat entry table of every row sorted by the key ... |
| [NxdSingleKeyHeader](NxdSingleKeyHeader.md) | `.nxd` | The header bytes of an nxd file that the game's loader (NxdTable_BindRows) reads for a single-key table, and the contiguous-keys flag that decides whether a key is read by position or searched. |
| [NxdSingleKeyRows](NxdSingleKeyRows.md) | `.nxd` | The row area of a single-key nxd file (header byte 8 = 1, byte 9 = 1 or 2): the entry table, the rows and the string pool, and how a row refers to its strings and arrays. |
| [ResumeEntry](ResumeEntry.md) | `.sav` | One entry of `autoenhanced.png`: a 16-byte entry header, a 340-byte payload header, then a body that is either the 40,164-byte save work copy (kind 0, the world and main form) or a 668,112-byte battle snapshot followe... |
| [SavePngContainer](SavePngContainer.md) | `.png` | A game save file: an ordinary PNG whose private `ffTo` chunk carries a `UMIF` container. |
| [SoundBankSab](SoundBankSab.md) |  | sound/common/sound.sab (0006.pac, 78 MB, stored uncompressed): a SEAD sound bank ('sabf' version 2) whose 690 sounds are the ids SoundCue_Play accepts (0..0x2B1); the audio is CRI HCA, not encrypted. |
| [SpriteSheetEntries](SpriteSheetEntries.md) | `(g2d entries)` | The sprite data of a unit look: two HD sheet entries, the classic sprite file and its palette rows. |
| [tec](tec.md) | `.tec` | Shader technique file (for example uirender.tec): the DXBC shader containers of a technique, its programs, sampler presets and the binding tables that tie each shader's registers to engine names. |
| [TextId](TextId.md) |  | A 16-bit text id in two fields: the top 5 bits select one of 32 string pools, the low 11 bits index the strings inside that pool. |
| [TexturePartFile](TexturePartFile.md) | `.utexpt` | The part file that names the texture a UI image part shows (ui/ffto/icon/<kind>/textureparts/<name>.utexpt). |
| [TitleMenuLayout](TitleMenuLayout.md) | `.uib` | `ui/ffto/title/ffto_title_enhanced.uib` (pack 0008), the layout of the Enhanced title menu: nine components, of which `Menu` carries the row layouts the add-on plays by name. |
| [TitleScreenLayout](TitleScreenLayout.md) | `.uib` | `ffto_title_enhanced.uib` (pack 0008): the title screen behind the menu: backdrop, logo, version, copyright and the `Menu` component with its six buttons. |
