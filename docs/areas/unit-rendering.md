# Unit rendering

Unit preview, sprite records, CharaRender/CharaSlot, palettes and renderer pages.

Functions: 38.

## Functions (38)

| Name | Address | Purpose |
|---|---|---|
| [CharaAnim_ReadStep](../functions/CharaAnim_ReadStep.md) | `0x1400CC6C0` | Reads one step of an animation from the unit's sequence table: row (animation id, step) -> opcode, value and delay. |
| [CharaAnim_Step](../functions/CharaAnim_Step.md) | `0x1400CC994` | Advances the slot's classic SEQ animation by one command and, for a frame command, makes sure its atlas texture is loaded (CharaRender_LoadCheck). |
| [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md) | `0x14026E750` | Fills a 256-colour palette (16 palettes of 16 colours) for a sprite shape from the shape's classic sprite file, then lets the shape's colour-override rows adjust it. |
| [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md) | `0x1400CE204` | Builds the unit's atlas texture: loads the shape's sprite file from the FFT pack, applies the 16-colour palette (with optional colour offsets), and expands the 4-bit pixels into a 512 x 512 RGBA texture. |
| [CharaRender_DrawFrame](../functions/CharaRender_DrawFrame.md) | `0x1400CD458` | Renders one unit slot's current animation frame into its 256 x 256 target: builds the atlas textures and LUT cell on demand, turns the frame's rectangles into quads and submits them twice (outline pass, then colour pa... |
| [CharaRender_FrameCacheUpdate](../functions/CharaRender_FrameCacheUpdate.md) | `0x1400CD22C` | Keeps the 44-byte frame cache entry of a slot in step with the current request (shape, palettes, frame, flags): a changed request invalidates the atlases or the whole frame. |
| [CharaRender_InitTargets](../functions/CharaRender_InitTargets.md) | `0x1400CCEC0` | Creates the per-slot render targets and vertex buffers (256 slots) and stores the target geometry used by the draw. |
| [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md) | `0x1400CBFD0` | Looks up the per-shape rows that drive a unit's shadow size and LUT region: shape row -> shadow-size row and LUT-parameter row. |
| [CharaRender_LutUvForQuad](../functions/CharaRender_LutUvForQuad.md) | `0x1400CBCE8` | Computes the LUT texture coordinates at the four corners of a unit quad: the sprite is laid over a small region of the LUT sheet (width/height from CharShapeLUTParam) at the slot's LUT cell. |
| [CharaRender_PlaceSlotImage](../functions/CharaRender_PlaceSlotImage.md) | `0x1400ED7CC` | Points the slot's UI image node at the unit's render texture and sizes/positions it: size = texture size x (slot scale +60 / entry scale +12), offset from the entry's anchor. |
| [CharaRender_RegisterSlot](../functions/CharaRender_RegisterSlot.md) | `0x1400ED9F8` | Registers a UI image node as the display for one unit render slot and applies the first sprite request. |
| [CharaRender_SetSlotRequest](../functions/CharaRender_SetSlotRequest.md) | `0x1400EDAE0` | Writes one unit-preview request (slot id, shape, palette, pose, flags) into the global unit renderer's 92-byte slot entry and restarts its animation when the request changed. |
| [CharaRender_SubmitQuads](../functions/CharaRender_SubmitQuads.md) | `0x1403CF370` | Binds the atlas (slot 0) and the LUT texture (slots 1..3), sets sampler words and pass constants, copies the quad vertices into the vertex ring and queues the draw. |
| [CharaRenderer_Init](../functions/CharaRenderer_Init.md) | `0x1400D4648` | Builds the unit renderer: allocates its sub-objects, loads the textures it needs and creates the 256 slot targets. |
| [CharaRenderer_Update](../functions/CharaRenderer_Update.md) | `0x1400D4CB0` | Per-frame update of the unit renderer: retires finished job records, ticks the sub-systems and animates and draws every live slot. |
| [CharaSlot_Reset](../functions/CharaSlot_Reset.md) | `0x1400CC5DC` | Clears a slot's animation state and releases its frame-cache entry so the next request rebuilds it. |
| [CharaSlot_SetParams](../functions/CharaSlot_SetParams.md) | `0x1400CCBA0` | Stores a slot's sprite parameters and restarts its animation sequence when any of them changed. |
| [CharClut_ApplyToPalette](../functions/CharClut_ApplyToPalette.md) | `0x14026C530` | Applies the CharCLUT rows of one key to a palette: each enabled row replaces one 16-colour block with colours given as 8-bit RGB triples. |
| [CharShape_ApplyClut](../functions/CharShape_ApplyClut.md) | `0x14026C7AC` | Looks up the shape's row in the CharShape table and, if the row names a colour-override set, applies it to the palette. |
| [ItemSprite_LoadPalettes](../functions/ItemSprite_LoadPalettes.md) | `0x14026A358` | Loads the two palettes of the unit's equipped weapon or shield into the sprite state, and records the item id and an equipment category with them. |
| [PreviewUnit_BuildRecord](../functions/PreviewUnit_BuildRecord.md) | `0x1400FB164` | Normal-play builder of a unit's sprite record: creates the preview unit, resolves its shape and palette, fills the record and applies the alternate row (table 0x112). |
| [PreviewUnit_BuildSpriteRecord](../functions/PreviewUnit_BuildSpriteRecord.md) | `0x1400FB038` | Builds a sprite record from preview-table entry `previewIndex` (<= 0x14), resolving shape/palette and applying the entry's flag-driven overrides. |
| [PreviewUnit_ResolveShape](../functions/PreviewUnit_ResolveShape.md) | `0x1400FCAB0` | Resolves shape/palette for entry `idx` (<= 0x14) of the 21-entry preview table g_BattleUnitTable (stride 512). |
| [Rgb555ToRgba8888](../functions/Rgb555ToRgba8888.md) | `0x14041DC34` | Converts PSX RGB555 palette entries to RGBA8888 the way the engine does: each 5-bit channel times 8 (max 248, NOT 255), alpha 0xFF (0x80 for a set bit 15 when keepSemi). |
| [SpriteId_ToShape](../functions/SpriteId_ToShape.md) | `0x140274028` | Maps a scene sprite id (the value Unit_GetSpriteSetId hands to event and scene code) to a sprite shape number. |
| [SpriteRecord_Fill](../functions/SpriteRecord_Fill.md) | `0x1400FB2A4` | Writes the sprite record fields and derives the pose id from the slot argument. |
| [SpriteRecord_SetPaletteBits](../functions/SpriteRecord_SetPaletteBits.md) | `0x1400FB328` | Sets frame/palette flag bits at record+12 and the selected palette index at +24 from small tables (word_140672CF8/D7A/D98). |
| [sub_140214134](../functions/sub_140214134.md) | `0x140214134` | Turns a unit id into a sprite shape and returns the shape's bit class through the out parameter. |
| [sub_140221798](../functions/sub_140221798.md) | `0x140221798` | Resolves the sprite shape of a battle unit from the live unit table. |
| [sub_140260CF0](../functions/sub_140260CF0.md) | `0x140260CF0` | Updates one unit render slot's transform: rotation, scale and placement from the unit's facing. |
| [sub_140266890](../functions/sub_140266890.md) | `0x140266890` | Copies a classic item-icon tile state into the unit's icon sprite record, so the unit's item overlay uses that tile. |
| [sub_14026A7B8](../functions/sub_14026A7B8.md) | `0x14026A7B8` | Refreshes a unit's sprite palette for the item it holds, branching on the unit's current pose/shape. |
| [sub_14026C2E8](../functions/sub_14026C2E8.md) | `0x14026C2E8` | Loads or refreshes the high-definition sprite entry for one render slot. |
| [sub_1402F74D8](../functions/sub_1402F74D8.md) | `0x1402F74D8` | Expands one 16-colour RGB555 palette into the two working palette forms a unit sprite slot uses. |
| [sub_1402F7594](../functions/sub_1402F7594.md) | `0x1402F7594` | Builds one 16-colour palette block for a sprite slot and records that the slot is ready, so later calls for the same slot return at once. |
| [Unit_BuildPreviewSpriteRecord](../functions/Unit_BuildPreviewSpriteRecord.md) | `0x1402C1D40` | Builds the sprite record for a party unit's preview. |
| [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md) | `0x1402C06D4` | Resolves a unit's sprite number for the event and scene code. |
| [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md) | `0x140278EDC` | Returns the sprite shape id for a unit/job pair (and a palette byte for special units). |
