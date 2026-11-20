# Graphics

The renderer: scene targets, glare/bloom, shader techniques and programs, sampler state, render contexts, the UI blur, layer effects and composite passes.

Functions: 170, Structures: 53, Globals: 14, Registries: 3, Shaders: 9, Shader programs: 4, Render targets: 8, File formats: 2, Flows: 6, Observed behaviours: 47, Tables: 48.

## Functions (170)

| Name | Address | Purpose |
|---|---|---|
| [AtlasShelf_Alloc](../functions/AtlasShelf_Alloc.md) | `0x1403B6D68` | Shelf (row) allocator for the layer atlas page: places a rectangle plus margin and returns the packed integer rectangle. |
| [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md) | `0x1401F2E4C` | The mid-battle join: runs Battle_AddJoinedUnit, then the look loader once per frame until it returns 0. |
| [BattleFormation_DrawUnits](../functions/BattleFormation_DrawUnits.md) | `0x140216EB4` | The battle formation draw (called from sub_140213F14): per unit index 0..20 it reads the CharShape row of the scene object's sprite byte for the draw height. |
| [BattleLoad_StepFresh](../functions/BattleLoad_StepFresh.md) | `0x1403044EC` | State machine of one battle scene load: prepares, builds the roster queue, loads every queued look through CharaPalette_ReloadForShape and starts the battle turn engine. |
| [BlendDesc_FromWords](../functions/BlendDesc_FromWords.md) | `0x140051284` | Unpacks packed render-target blend words into the Direct3D 12 blend description array of a pipeline state. |
| [Camera_UpdateMatrices](../functions/Camera_UpdateMatrices.md) | `0x1403A5674` | Per-frame update of a render camera (vftable faith::Graphics::Object::Camera slot at 0x140720AF8): rebuilds its view matrix, projection matrix, view-projection matrix, inverses, and sets a 'changed' flag when anything... |
| [Camera_UpdateSecondaryView](../functions/Camera_UpdateSecondaryView.md) | `0x1403A5ECC` | Tail of Camera_UpdateMatrices: builds the second view (the one belonging to the render target object at target+32), its view-projection and inverse, with the same epsilon dirty tracking. |
| [Camera_UploadSceneConstants](../functions/Camera_UploadSceneConstants.md) | `0x1403A6240` | Second camera vtable function (0x140720B00): updates the camera-relative origin, the double-buffered matrix history, and writes the 1040-byte scene constant block (matrices current and previous) into a mapped GPU cons... |
| [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md) | `0x14026FB28` | Step function that walks the look queue and, for each entry, loads its frame file, its sequence file and its classic sprite file, then builds the scene unit; returns 0 when the queue is done, 1 or 2 while work remains. |
| [CharaRenderer_GlareChain](../functions/CharaRenderer_GlareChain.md) | `0x1400D1018` | Runs the glare (bloom) passes on the unit renderer's scene target: bright-pass (shader id 1035 GLARE_BRIGHT), blur (1036 GLARE_BLUR) and the composite. |
| [CharaRenderer_PostFrame](../functions/CharaRenderer_PostFrame.md) | `0x1402567E0` | End-of-frame pass of the unit (chara) renderer: runs the glare chain when enabled, then the post/resolve steps. |
| [ClutFade_SetTarget](../functions/ClutFade_SetTarget.md) | `0x1402F4944` | Gives one row of a palette bank (or all 16 rows) a new colour to move to, at once or as a timed fade. |
| [ClutManager_Update](../functions/ClutManager_Update.md) | `0x1402F5F78` | The palette manager's step, once a frame from the battle loop: colour cycles, three screen-colour fades and the timed fades of the 14 palette banks. |
| [ClutManager_Upload](../functions/ClutManager_Upload.md) | `0x1402F7964` | Copies the palette manager's final image into the emulated video memory when it changed. |
| [ComponentDrawContext_ComputeMatrix](../functions/ComponentDrawContext_ComputeMatrix.md) | `0x14040A914` | Gives ComponentDrawContext_Build the component's local 2 x 3 matrix and a two-float scale; when comp+540 = 1 it scales the matrix by the ratio of two sizes, otherwise it copies both straight from the property block. |
| [CustomResourceHandle_Ctor](../functions/CustomResourceHandle_Ctor.md) | `0x1403BA5B4` | Constructor of the base 'custom' resource handle: runs the base ResourceHandle constructor, sets the CustomResourceHandle vtable and clears its extra fields. |
| [DepthStencilDesc_FromWord](../functions/DepthStencilDesc_FromWord.md) | `0x140051438` | Unpacks the packed depth-stencil word of a pipeline state into the Direct3D 12 depth-stencil description. |
| [FaceNumber_Remap](../functions/FaceNumber_Remap.md) | `0x1400F8338` | Replaces a few face numbers by the face the UI shows for them; every other number passes unchanged. |
| [FaceTexture_FormatName](../functions/FaceTexture_FormatName.md) | `0x1400FC22C` | Formats the texture name of a face: the format string of UI texture path row 4 with the face number and the colour. |
| [FaceWidget_SetFace](../functions/FaceWidget_SetFace.md) | `0x14028FF34` | Points a face widget at the texture of a face number and colour, and restarts its blink. |
| [FrequentUtilRenderer_Construct](../functions/FrequentUtilRenderer_Construct.md) | `0x1403AA900` | Constructor of the FrequentUtilRenderer (copy, blur, mip-generation and model-buffer utility passes): sets its vtable and resets all fields. |
| [FrequentUtilRenderer_CreateResources](../functions/FrequentUtilRenderer_CreateResources.md) | `0x1403AAA84` | FrequentUtilRenderer set-up: loads shader/FrequentUtil.tec, creates six small constant buffers, loads 16 blue-noise textures, builds a 36-index buffer, looks up 18 texture slots and 10 constant-buffer slots, then crea... |
| [GaussianKernel_Build](../functions/GaussianKernel_Build.md) | `0x1403ABD50` | Builds the normalised one-sided 64-entry Gaussian weight table for the UI blur and returns the tap count. |
| [GraphicsRenderer_AppendShaderRecord](../functions/GraphicsRenderer_AppendShaderRecord.md) | `0x1403AA8BC` | Renderer vtable slot 8 (shared by SDFFontRenderer and FrequentUtilRenderer): appends a 16-byte record {r+24, 0} (the renderer's shader) to a caller-supplied vector. |
| [GUILayer_ApplyEffects](../functions/GUILayer_ApplyEffects.md) | `0x1403B6204` | Runs the enabled effect passes of one finished layer in a fixed order, ping-ponging between two scratch render targets, then draws the layer's own pixels and finally the +178 effect group. |
| [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md) | `0x1403B4C2C` | Draws the layer's own pixels onto its parent with the layer blend mode (the pass after the +176 / +177 effects). |
| [GUILayer_BlurEffect](../functions/GUILayer_BlurEffect.md) | `0x1403B6640` | Whole-layer blur (the effect with radius at layer+500): copies the layer region, blurs it with UIBlur_Run and blits the result. |
| [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md) | `0x1403B4990` | Second step of the +177 (drop shadow) effect group: blurs the silhouette in RT 3 by the radius at layer+188, then draws it onto the layer's target with selector #10 program 1, which darkens the target by the shadow st... |
| [GUILayer_Composite](../functions/GUILayer_Composite.md) | `0x1403B59D4` | Packs the commands of one finished offscreen layer for the frame: the clears of its atlas page, the effect passes and the blit of the layer onto its parent target. |
| [GUILayer_CopyOffsetRegion](../functions/GUILayer_CopyOffsetRegion.md) | `0x1403B6028` | Used when layer byte +487 is set: copies the layer's rectangle from target slot 30 into render target 26 (the first scratch), standing in for the effect ping-pong start. |
| [GUILayer_CopyToTarget](../functions/GUILayer_CopyToTarget.md) | `0x1403B4800` | First step of the +177 (drop shadow) effect group: draws the layer's current scratch render target RT[srcRT] into slot 3 of the layer target's slot table with selector #10, program 0, clipped to a rectangle (a silhoue... |
| [GUILayer_EffectPass0](../functions/GUILayer_EffectPass0.md) | `0x1403B5818` | First layer-effect pass of GUILayer_ApplyEffects (run when the layer's props flag +489 is set): sets up one render command that binds two layer textures and a shader selector and queues a 96-byte command. |
| [GUILayer_FillQuadBuffers](../functions/GUILayer_FillQuadBuffers.md) | `0x1403B12CC` | Writes the layer's rectangle as quads into the eight per-layer vertex buffers of the UI renderer, slot index layer+8 (4 vertices per layer). |
| [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md) | `0x1403B4EA8` | Glow composite: blurs the layer by the glow radius and draws the result with the glow shader permutation selected by the mode field. |
| [GUILayer_PackAtlasRect](../functions/GUILayer_PackAtlasRect.md) | `0x1403B6A78` | Decides where a layer's pixels live in the layer atlas pages, allocates the integer rectangle there and rewrites the layer rectangle (+208..+220) and its offsets (+224..+236) to the packed position. |
| [HdGroup_BuildPiece](../functions/HdGroup_BuildPiece.md) | `0x1403D0F8C` | Builds one texture of a sheet group: a rectangle of the group's sheet pixels, expanded through a converted palette into 32-bit texels. |
| [HdLayer_BindSheetTexture](../functions/HdLayer_BindSheetTexture.md) | `0x14041D670` | Binds a sprite sheet texture id of the battle HD layer to the g2d entry that the sheet slot table holds. |
| [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md) | `0x140415D30` | The battle HD layer's texture pass: for every draw record of the frame it finds or builds the texture of its sheet piece and palette, and writes the texture id into the record. |
| [LayerBinds_Push](../functions/LayerBinds_Push.md) | `0x1403A83B0` | Appends a (slot, resource) pair to the binder's per-layer (mode 1) or per-target (mode 2) vectors; the pairs are replayed into a render command by LayerBinds_Replay. |
| [LayerBinds_RecordAllLayers](../functions/LayerBinds_RecordAllLayers.md) | `0x1403A82A8` | Walks every live render layer and records the per-layer shader-resource binds for those flagged as recordable. |
| [LayerBinds_RecordLayer](../functions/LayerBinds_RecordLayer.md) | `0x1403A8354` | Records two bind entries for one layer: the per-group constant buffer and, if the layer has a render target, that target's buffer. |
| [LayerBinds_Replay](../functions/LayerBinds_Replay.md) | `0x1403A8468` | Copies the recorded bind lists of a layer into a render command: resource pointers into cmd+328+8*slot, texture handles into cmd+1608+8*slot, and 31-bit constants into cmd+5704+4*slot. |
| [LookPool_ClaimForSprite](../functions/LookPool_ClaimForSprite.md) | `0x140268FF4` | Finds or claims the look pool record for a sprite number and returns its index, or 0xFFFF when all 15 records are in use. |
| [LookPool_ResetForBattleLoad](../functions/LookPool_ResetForBattleLoad.md) | `0x14026F5CC` | Clears the scene-unit in-use flags and the look pool claims before a battle load, and resets the load state machine. |
| [LookQueue_Add](../functions/LookQueue_Add.md) | `0x1403041A4` | Appends one entry to the 16-entry look load queue that CharaPalette_ReloadForShape later turns into scene units. |
| [ModelSkeleton_BuildBoneLinks](../functions/ModelSkeleton_BuildBoneLinks.md) | `0x1403BD428` | Builds the list of bone links of a loaded model by matching its bone names against the 33 bone name pairs. |
| [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md) | `0x140089280` | Turns a shader resource name (constant buffer, texture or sampler) into a small dense slot id, adding the name to the table the first time it is seen. |
| [Palette_ConvertToRgba](../functions/Palette_ConvertToRgba.md) | `0x14025EB10` | Converts a 16- or 256-colour palette of 15-bit words into 32-bit colours with alpha. |
| [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md) | `0x1402B5644` | Returns the classic-graphics face value of a save unit record: it finds the record's portrait code the way sub_14032AB3C does (marker, job byte, job row), from its own copy of the code words, and turns the code into t... |
| [Pixels_ExpandToRgba](../functions/Pixels_ExpandToRgba.md) | `0x14041DDB0` | Expands a block of 4-, 8-, 16- or 32-bit pixels into 32-bit texels. |
| [PortraitCode_FillCell](../functions/PortraitCode_FillCell.md) | `0x1402E16A8` | Turns a portrait code into the classic portrait atlas cell of a draw record and its colour, and returns the code's low byte. |
| [PostTarget_DrawFitted](../functions/PostTarget_DrawFitted.md) | `0x1403CB9C4` | Draws one textured quad from a render-target descriptor (136-byte entries at unk_142C819D0) into the current UI render target, fitted into the 16:9 area of the window, with the layer-composite selector #9 in permutati... |
| [RenderCommand_Allocate](../functions/RenderCommand_Allocate.md) | `0x140069A38` | Allocates one command of the given size from the context's current 8 KB command block, writes its type, and returns the pointer. |
| [RenderCommand_ClearTarget](../functions/RenderCommand_ClearTarget.md) | `0x140054C24` | Render-thread executor of the command type 0 that GUILayer_Composite and RenderContext_ResetFrame queue: clears one render target to the colour stored in the command. |
| [RenderCommand_Submit](../functions/RenderCommand_Submit.md) | `0x140069980` | Appends a finished command to the context's list as a {sort key, command pointer} pair; the list is later executed in key order (the sort itself was not read here). |
| [RenderContext_ResetFrame](../functions/RenderContext_ResetFrame.md) | `0x140087C50` | Start-of-frame reset of the renderer: clears the command-memory counters and puts every 6032-byte render context (the per-thread state the other sheets call the thread state) back to its default pipeline state, with e... |
| [RenderFrame_BeginStage4](../functions/RenderFrame_BeginStage4.md) | `0x1403A29E8` | Begins the fourth job stage: zeroes the work counter r+38072, resets and submits every record of array r+37992 (count r+38040, including the last), queues the fence r+39176 and sets r+44421. |
| [RenderFrame_FillLayerConstants](../functions/RenderFrame_FillLayerConstants.md) | `0x1403A7E48` | Once per frame (called from the frame update sub_1403A2774 on renderer+24760): for each render layer target, maps its per-layer constant buffer and fills it with the layer pixel size, 1/size, ratios to the back buffer... |
| [RenderFrame_Record](../functions/RenderFrame_Record.md) | `0x1403A2BA8` | Render-thread half of the frame: for each of the (up to) 4 submission rounds it builds the per-pass command batches (RenderPass_Build), runs the worker command loops, resets per-layer counters, and closes with the fin... |
| [RenderFrame_ResetFlags](../functions/RenderFrame_ResetFlags.md) | `0x1403A2388` | Atomically sets the 'started' flag r+38056 (dword index 9514) and, only if it was 0, clears the three neighbouring flags r+38060, +38064, +38068. |
| [RenderFrame_Update](../functions/RenderFrame_Update.md) | `0x1403A2774` | Main-thread half of the frame: latches per-frame flags, converts each pending timer's float seconds to a 1024-tick integer range, runs the pass sorting / stage 1-3 begin calls, then notifies every registered listener. |
| [RenderPass_Build](../functions/RenderPass_Build.md) | `0x1403A48CC` | Packs up to 16 draw layers per target into one 240-byte batch entry (and at most 64 layers per round, counter m+6607) for the command-recording jobs; returns 1 while more batches remain for the round, 0 at the end. |
| [RenderPass_PrepareViews](../functions/RenderPass_PrepareViews.md) | `0x1403A3CDC` | For each registered view / render target (count m+6575) it advances the double-buffered 20-byte size record (current / previous) from the target description, then calls _multtenpow12 on the global qword_143CD9B70. |
| [RenderPass_RunQueued](../functions/RenderPass_RunQueued.md) | `0x1403A4CD8` | Work-stealing loop that runs every queued layer object of the table m+14048: calls its vtable +64 with the per-group target pointer and then releases it (vtable +32). |
| [RenderPass_Sort](../functions/RenderPass_Sort.md) | `0x1403A3DCC` | Sorts and buckets the frame's draw layers (pointer table m+80, count word m+7252) into the 4 per-group arrays, counts them, updates texture-pool residency, and returns 1 when the frame has something to draw. |
| [RenderQueue_Flush](../functions/RenderQueue_Flush.md) | `0x1403A4308` | Resets every 264-byte job record of the pass array and re-submits it to the scheduler, then submits the trailing fence record and kicks the scheduler. |
| [RenderStage1_Begin](../functions/RenderStage1_Begin.md) | `0x1403A23B0` | Begins render stage 1: finishes the pending stage-0 fence, runs the stage-1 job array, then calls the stage-1 fence object and sets r+44418. |
| [RenderStage1_End](../functions/RenderStage1_End.md) | `0x1403A2498` | Ends render stage 1 when r+44418 is set: signals the last stage-1 job record and submits a callback pair to the scheduler. |
| [RenderStage1_SetGate](../functions/RenderStage1_SetGate.md) | `0x1403A248C` | One-line helper: InterlockedExchange(r+38060, 1). |
| [RenderStage2_Begin](../functions/RenderStage2_Begin.md) | `0x1403A2514` | Same pattern as RenderStage1_Begin for the second job array (r+37976, count r+38032, fence r+38632): resets and submits every record, sets r+44419 and kicks the scheduler. |
| [RenderStage2_SetGate](../functions/RenderStage2_SetGate.md) | `0x1403A25E8` | One-line helper: InterlockedExchange(r+38064, 1). |
| [RenderStage3_Begin](../functions/RenderStage3_Begin.md) | `0x1403A25F4` | Begins render stage 3: closes stage 2 if still open (signal its last record, wait on its fence), then submits the third job array (r+37984, count r+38036) and the fence at r+38904; sets r+44420. |
| [RenderStage3_End](../functions/RenderStage3_End.md) | `0x1403A26F8` | Twin of RenderStage1_End for stage 3: signals the last record of array r+37984 and submits callback sub_1403C5194, clears r+44420. |
| [RenderStage3_SetGate](../functions/RenderStage3_SetGate.md) | `0x1403A26EC` | One-line helper: InterlockedExchange(r+38068, 1). |
| [RenderState_PackCommand](../functions/RenderState_PackCommand.md) | `0x14003A2B0` | Packs the current pipeline state (blend words, flags, shader constants, texture bindings) into the 8 KB command chunks the render thread consumes and stamps the command with a state hash. |
| [RenderState_SeedCommands](../functions/RenderState_SeedCommands.md) | `0x1403A32F4` | Queues 79 tiny 8-byte render-state commands (type 38) on the thread's command list: one for each id in a fixed list, one for 44..59 and one for 79, 83, ... 281 step 4. |
| [RenderWorkers_RunCmd24](../functions/RenderWorkers_RunCmd24.md) | `0x1403A2AB0` | Work-stealing loop over the 4 per-pass worker objects: atomically takes the next index from r+38072 and calls vtable +24 on worker r+37920[i] while i < 4. |
| [RenderWorkers_RunCmd40](../functions/RenderWorkers_RunCmd40.md) | `0x1403A2B18` | Same loop as RenderWorkers_RunCmd24 with its own counter (r+38076) and worker vtable +40, passing arg through. |
| [RenderWorkers_RunCmd48](../functions/RenderWorkers_RunCmd48.md) | `0x1403A2B68` | Same loop with counter r+38080 and worker vtable +48. |
| [ResourceHandle_StateStep](../functions/ResourceHandle_StateStep.md) | `0x1403BA658` | Slot 7 of every faith::Graphics::*ResourceHandle class (Font, Model, Texture, Custom, AdditionalKerning): advances the handle's load state machine by one step. |
| [RootSignature_CreateWithSampler](../functions/RootSignature_CreateWithSampler.md) | `0x140042E64` | Builds one Direct3D 12 root signature (optional root constants, one SRV descriptor table, optional UAV descriptor table, at most one static sampler decoded from a sampler word), serialises and creates it on the device... |
| [Sampler_DescFromWord](../functions/Sampler_DescFromWord.md) | `0x140068D54` | Decodes a 32-bit packed sampler word (the words kept in the draw state at +5704 + 4 * slot) into a D3D12 static sampler description. |
| [SceneObject_FindByUnitIndex](../functions/SceneObject_FindByUnitIndex.md) | `0x140260ABC` | Walks the scene object list and returns the object whose battle unit record has the given unit index, or null. |
| [SceneUnit_ApplyStatusTint](../functions/SceneUnit_ApplyStatusTint.md) | `0x140269330` | Gives a scene unit its colours: a status tint chosen from the unit's flag dword, or the plain row with the ambient light when no tint flag is set. |
| [SceneUnit_ApplyStatusVisuals](../functions/SceneUnit_ApplyStatusVisuals.md) | `0x1401FAF54` | Applies a scene unit's status visual set / clear masks and redraws the pose. |
| [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md) | `0x14026EB74` | Builds the scene unit of one look queue entry: takes a scene-unit slot, claims the look pool record of the sprite, picks the palette row, loads the pool's palette and frames, sets the HD sheet slot and links the unit ... |
| [SceneUnit_EntryById](../functions/SceneUnit_EntryById.md) | `0x1402EFF34` | Returns a scene unit entry of the selector scenes (564 bytes each at 0x1408E6CB0) by its id, or null. |
| [SceneUnit_FillSpriteRecord](../functions/SceneUnit_FillSpriteRecord.md) | `0x1402C2520` | Builds a work record from the selector-scene unit entry named by the object's byte +180 and fills the object's sprite record (+188) with its preview shape. |
| [SceneUnit_LoadExtraPage](../functions/SceneUnit_LoadExtraPage.md) | `0x14026C2E8` | Gives a scene unit one of the two extra sprite pages for its second-sheet frames (special poses such as a punch) and points that page's HD sheet slot at the unit's second sheet entry. |
| [SceneUnit_SyncSpriteFromPool](../functions/SceneUnit_SyncSpriteFromPool.md) | `0x14026A1DC` | Keeps a scene unit's sprite byte in step with its look pool record, and switches to the four effect sprites 155 to 158 when the unit's effect flags ask for them. |
| [SceneUnit_TintOwnRow](../functions/SceneUnit_TintOwnRow.md) | `0x14026929C` | Picks the 16-colour row a scene unit is drawn with and passes it to UnitClut_TintRow with the caller's mode and offsets. |
| [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md) | `0x1401D46B0` | Copies the scene units, the scene list, the CLUT image and the CLUT manager to or from the battle capture. |
| [SDFFont_GetAdvance](../functions/SDFFont_GetAdvance.md) | `0x1403A9A9C` | Returns the scaled advance (x, y) of one character: per-axis renderer scale times the glyph record advance, or (0, 0) when the font is unavailable or the glyph is missing. |
| [SDFFontBatch_SortCompare](../functions/SDFFontBatch_SortCompare.md) | `0x1403A8FB0` | qsort comparator for the text batch list: orders 8-byte entries by their first dword, never returns 0. |
| [SDFFontRenderer_AccumulateBounds](../functions/SDFFontRenderer_AccumulateBounds.md) | `0x1403A9248` | Grows the current batch's 2D bounding box (r+7928..7940) by the four vertices of the quad that SDFFontRenderer_EmitGlyph just wrote. |
| [SDFFontRenderer_CloseBatch](../functions/SDFFontRenderer_CloseBatch.md) | `0x1403A8FBC` | Closes the glyph batch being built (all quads emitted since the last close) and starts a new one: stores its quad range, bounding box, node record and sort key in the batch table. |
| [SDFFontRenderer_Construct](../functions/SDFFontRenderer_Construct.md) | `0x1403A8694` | Constructor of the SDFFontRenderer: sets its vtable and resets every field (run state defaults, palette / vertex pointers, texture-slot ids) to its initial value. |
| [SDFFontRenderer_CreateResources](../functions/SDFFontRenderer_CreateResources.md) | `0x1403A87EC` | SDFFontRenderer set-up: fills the CPU palette array with 512 default entries, loads shader/SDFFont.tec, creates the palette buffer + its view, the constant buffer, the vertex / index buffers for the glyph quads, looks... |
| [SDFFontRenderer_EmitGlyph](../functions/SDFFontRenderer_EmitGlyph.md) | `0x1403A94C8` | Emits the quad of one glyph (position, atlas UV, node alpha, palette index, per-vertex factor g = atlasWidth / 8192) for the SDF text shader, and advances the pen. |
| [SDFFontRenderer_Flush](../functions/SDFFontRenderer_Flush.md) | `0x1403A9B20` | Uploads the frame's glyph quads and palette entries to the GPU and issues the batched SDF text draws; rewrites every palette entry into the form the pixel shader uses. |
| [SDFFontRenderer_GlyphIndex](../functions/SDFFontRenderer_GlyphIndex.md) | `0x1403A9474` | Maps the UTF-8 character at the pointer to the glyph slot of the current font: decodes the code point and looks it up in the font's 65536-entry u16 table; 0 means 'no glyph'. |
| [SDFFontRenderer_PrepareTechnique](../functions/SDFFontRenderer_PrepareTechnique.md) | `0x1403A9084` | SDFFontRenderer shader-ready check (vtable slot 7): when the SDFFont shader has finished loading, creates the technique and sets the 'renderer usable' flag. |
| [SDFFontRenderer_ReleaseResources](../functions/SDFFontRenderer_ReleaseResources.md) | `0x1403A8E6C` | SDFFontRenderer release (vtable slot 2): frees every GPU object and CPU buffer the set-up created and nulls the pointers. |
| [SDFFontRenderer_ResetFrame](../functions/SDFFontRenderer_ResetFrame.md) | `0x1403A9100` | Virtual slot that clears the per-frame emit counters so the next frame starts at quad / batch index 0. |
| [ShaderProgram_ApplyState](../functions/ShaderProgram_ApplyState.md) | `0x1403A39CC` | Binds one program: its shader objects into the thread state and the pipeline-state words (raster word, blend state word, the blend words of the render targets, blend-factor flags) from its 64-byte entry. |
| [ShaderSelector_Apply](../functions/ShaderSelector_Apply.md) | `0x14039EC9C` | Resolves the selector's current permutation index to a program table and applies the program with the given index (within that permutation) to the thread state. |
| [ShaderSelector_SetDigit](../functions/ShaderSelector_SetDigit.md) | `0x1403C4AA8` | Sets one mixed-radix digit of the selector's state dword (the permutation index that ShaderSelector_Apply uses) and marks the state dirty. |
| [SpriteShape_ToHdTexture](../functions/SpriteShape_ToHdTexture.md) | `0x14027411C` | Returns the HD texture id of a sprite shape number, or -1 when the shape has none. |
| [StdSort_LayersByKey](../functions/StdSort_LayersByKey.md) | `0x1403C2B00` | The introsort loop of MSVC's std::sort for an array of layer pointers keyed by the unsigned dword at layer+84 (the draw-order key); the final sort of UIRender_PrepareLayers, whose result is the order in which GUILayer... |
| [StdSort_LayersByOrder](../functions/StdSort_LayersByOrder.md) | `0x1403C2930` | The introsort loop of MSVC's std::sort for an array of layer pointers, keyed by the unsigned dword at layer+12 (the layer's order); UIRender_PrepareLayers sorts the collected layer list with it before it computes the ... |
| [StdSort_PartitionPtrByDword12](../functions/StdSort_PartitionPtrByDword12.md) | `0x1403C37EC` | Introsort partition step on an array of object pointers keyed by the dword at object+12: median-of-three (or Tukey ninther for more than 41 elements) pivot choice and three-way partition; returns the equal range [lo, ... |
| [StdSort_PartitionPtrByDword84](../functions/StdSort_PartitionPtrByDword84.md) | `0x1403C3AC8` | Same partition step as StdSort_PartitionPtrByDword12 with the key at object+84. |
| [StdSort_PopHeapHolePtrByDword12](../functions/StdSort_PopHeapHolePtrByDword12.md) | `0x1403C3EF4` | MSVC's heap 'pop with hole' step for the layer pointer array, key = dword at layer+12: moves the hole at index hole down to a leaf along the larger child, then sifts the value up from there. |
| [StdSort_PopHeapHolePtrByDword84](../functions/StdSort_PopHeapHolePtrByDword84.md) | `0x1403C3FA0` | The same heap step as StdSort_PopHeapHolePtrByDword12 with the key at layer+84. |
| [sub_14022AA88](../functions/sub_14022AA88.md) | `0x14022AA88` | Finds the look pool index of a battle unit through the scene-unit list and fills the image rectangle the turn panel uses for its small face; returns the pool index or -1. |
| [sub_14026E838](../functions/sub_14026E838.md) | `0x14026E838` | Battle side of the palette load: copies the classic file's palette into the unit's look pool record, applies the CharShape colour override keyed by the unit's sprite byte, and uploads the palette and frames for the slot. |
| [sub_14030476C](../functions/sub_14030476C.md) | `0x14030476C` | State machine of a battle scene load with a second roster build (the checkpoint or rematch path): resets the look pool, builds both rosters, loads their looks and starts the turn engine. |
| [sub_14032AB3C](../functions/sub_14032AB3C.md) | `0x14032AB3C` | Finds the portrait code of a save unit record (by its marker byte, job byte and job row) and fills a portrait draw record with it; returns the code's low byte, or -1 when the code carries bit 8 or 9. |
| [sub_14032ACE0](../functions/sub_14032ACE0.md) | `0x14032ACE0` | Builds the portrait draw records for one or two save units in a layout chosen by *mode, and returns the first unit's portrait code byte (sub_14032AB3C) or -1. |
| [sub_1403A855C](../functions/sub_1403A855C.md) | `0x1403A855C` | Constructor of a 25-qword object made of a leading zero qword and six 4-qword groups, each group = (allocator pointer, 0, 0, 0). |
| [sub_1403A85F0](../functions/sub_1403A85F0.md) | `0x1403A85F0` | Vector-deleting destructor for 272-byte objects: destroys one object, or an array whose element count is stored at a1 - 8, and optionally frees the memory. |
| [sub_1403B5170](../functions/sub_1403B5170.md) | `0x1403B5170` | One GUILayer effect pass (the +320 group in GUILayer_ApplyEffects' order): fills a draw command for a full-rect quad with the layer's source texture, picks a shader permutation by whether any of three 2-vectors is non... |
| [sub_1403BA778](../functions/sub_1403BA778.md) | `0x1403BA778` | Slot 8 of every resource handle class: calls virtual +144; when it returns >= 0 returns virtual +248, else the negative result. |
| [sub_1403BA7A0](../functions/sub_1403BA7A0.md) | `0x1403BA7A0` | Slot 9 of every resource handle class: calls virtual +256 then virtual +152 and clears the payload pointer / size at +96 / +104. |
| [sub_1403BA80C](../functions/sub_1403BA80C.md) | `0x1403BA80C` | Slot 13 of every resource handle class: calls virtual +168; when it returns >= 0 returns virtual +272(h, arg), else the negative result. |
| [sub_1403D0898](../functions/sub_1403D0898.md) | `0x1403D0898` | Initialises a 96-byte texture-create parameter block to defaults: dword +92 = 1, floats +8 / +84 / +88 = 1.0, the rest zero, and the two arrays of four ids (+96..+111) = 0xFF. |
| [sub_14041E05C](../functions/sub_14041E05C.md) | `0x14041E05C` | Builds the texture of one pending request record of the battle HD layer: a fixed sheet entry with the record's own palette, or pixels another routine prepared. |
| [TexHeader_TableSize](../functions/TexHeader_TableSize.md) | `0x1403BA9B0` | Size of the sub-image table of a TEX file header: returns (low dword = bytes of the table after the 40-byte header start, high dword = 40), or 0 for a header that is not version 4. |
| [TexHeader_ValidateCopy](../functions/TexHeader_ValidateCopy.md) | `0x1403BAA14` | Checks that a TEX header table fits and copies it: returns 0 on success, 2 for a wrong version, 3 for an entry count of 0 or above 255, 4 when the table is larger than the data available. |
| [TextureLoadInfo_Alloc](../functions/TextureLoadInfo_Alloc.md) | `0x1403BAABC` | Allocates and zero-initialises the 280-byte streaming state record of a texture load (the header copy, the image pointer array and the id array). |
| [TextureLoadInfo_Free](../functions/TextureLoadInfo_Free.md) | `0x1403BAB84` | Releases a TextureLoadInfo: releases its images, returns its ids to the id allocator, frees the arrays and the record, and clears *pp. |
| [TextureObj_Commit](../functions/TextureObj_Commit.md) | `0x1403D0B10` | Turns the pending source pixels into a GPU texture (or updates the existing one), then frees the source buffer and the loader object. |
| [TextureObj_Reset](../functions/TextureObj_Reset.md) | `0x1403D0C6C` | Resets a texture wrapper: frees pending source buffer and loader object, releases its entry in the global texture table and restores the default state. |
| [TextureObj_SetSource](../functions/TextureObj_SetSource.md) | `0x1403D0A80` | Gives a texture wrapper new source pixel data (pointer, size, bit depth): when the existing GPU texture has the same size and depth it is marked for update-in-place, otherwise it is reset. |
| [TextureResourceHandle_BuildDescriptors](../functions/TextureResourceHandle_BuildDescriptors.md) | `0x1403BAFE4` | For a TEX file whose entries carry per-slice records: builds the array of 96-byte upload descriptors (one for the inline payload and one per record) and hands it to the handle's consumer callback (state 1005 = finish). |
| [TextureResourceHandle_Create](../functions/TextureResourceHandle_Create.md) | `0x1403BAD34` | Allocates and constructs a faith::Graphics::TextureResourceHandle (144 bytes). |
| [TextureResourceHandle_CreateImage](../functions/TextureResourceHandle_CreateImage.md) | `0x1403BBC64` | Creates the GPU image for one 32-byte TEX header entry by its type (low 2 bits of dword 0): 0 -> sub_1400873D8, 1 -> sub_14008757C, 2 -> sub_1400876A8, 3 -> sub_140087834, each building a faith::Graphics::Texture plus... |
| [TextureResourceHandle_Dtor](../functions/TextureResourceHandle_Dtor.md) | `0x1403BAE44` | Scalar deleting destructor (vtable slot 0): resets the vtable to the Custom handle, runs the base destructor and frees the 144 bytes when bit 0 of flags is set. |
| [TextureResourceHandle_FinishLoad](../functions/TextureResourceHandle_FinishLoad.md) | `0x1403BAE84` | Last step of the TEX load (state 1005): moves the finished images from the load info into the handle and marks the handle ready. |
| [TextureResourceHandle_RegisterImages](../functions/TextureResourceHandle_RegisterImages.md) | `0x1403BBB78` | Slot 21 of TextureResourceHandle: when the handle's status dword (+80) is 1 (loaded), registers each of its images in the global image table under an id (allocating a fresh id when the stored one is 0xFFFF). |
| [TextureResourceHandle_StreamStep](../functions/TextureResourceHandle_StreamStep.md) | `0x1403BB25C` | Slot 17 of TextureResourceHandle: the incremental TEX file loader. |
| [TextureResourceHandle_Unload](../functions/TextureResourceHandle_Unload.md) | `0x1403BB9CC` | Slot 19 of TextureResourceHandle: releases the GPU images of the handle (count in the upper 13 bits of h+120) and their ids, then clears the count. |
| [TextureTable_Create32](../functions/TextureTable_Create32.md) | `0x1403D1528` | Creates a w x h 32-bit texture, copies the pixel rows into it and registers it in the global texture table; returns the table index (1..0x7FF) or 0. |
| [UIBlur_BlurPassOrCopy](../functions/UIBlur_BlurPassOrCopy.md) | `0x1403ACC64` | One Gaussian blur pass toward dstRT; when the kernel has 1 tap or less it degenerates to a plain copy. |
| [UIBlur_BlurPassSingle](../functions/UIBlur_BlurPassSingle.md) | `0x1403ACDBC` | Variant of UIBlur_BlurPassOrCopy that always draws: builds the Gaussian kernel and hands one textured pass to sub_1403AD710. |
| [UIBlur_CopyTarget](../functions/UIBlur_CopyTarget.md) | `0x1403ABEDC` | Draws a layer slot texture into a render target with a chosen filter index; the copy used between blur stages. |
| [UIBlur_DownsampleDispatch](../functions/UIBlur_DownsampleDispatch.md) | `0x1403B01F0` | Queues the tiled downsample of a rectangle by 2^levels (compute-style dispatch over 64-pixel tiles); the work done by UIBlur_DownsampleRegion. |
| [UIBlur_DownsampleRegion](../functions/UIBlur_DownsampleRegion.md) | `0x1403B4798` | Wrapper for the half-size path of UIBlur_Run: converts the target id into a level count, runs sub_1403B01F0 on the downsample object and returns the level count used. |
| [UIBlur_DrawPass](../functions/UIBlur_DrawPass.md) | `0x1403AD3A4` | Draws one direction of the separable Gaussian blur: uploads the cGaussianBlurPS constants (sigma, cutoff, tap count and the 64 weights), selects the shader permutation by tap count and records a draw command. |
| [UIBlur_DrawTexturedPass](../functions/UIBlur_DrawTexturedPass.md) | `0x1403AD710` | Queues one Gaussian blur draw of a layer slot texture into a render target, selecting the shader permutation from the tap count. |
| [UIBlur_Pass](../functions/UIBlur_Pass.md) | `0x1403ACAB8` | One blur step between two render targets: builds the kernel and runs the separable blur through sub_1403ACEBC, or plain-copies the target when the kernel is a single tap. |
| [UIBlur_Run](../functions/UIBlur_Run.md) | `0x1403B1A10` | Runs the layer blur for one effect radius: chooses a downscale level from the radius and runs separable Gaussian passes through the render-target chain. |
| [UIBlur_TapCount](../functions/UIBlur_TapCount.md) | `0x1403ACA7C` | Returns the tap count of the Gaussian kernel for (sigma, tail) and throws the weights away. |
| [UICommandRing_Flush](../functions/UICommandRing_Flush.md) | `0x1403ADF04` | Uploads the collected command stream into the ring's constant buffer, sets the base pipeline state and executes the batches. |
| [UICommandRing_Reset](../functions/UICommandRing_Reset.md) | `0x1403ADE60` | Resets the per-frame UI command ring: clears the write counters and re-initialises the 32 UIContext slots (80 bytes each). |
| [UIContext_SortCommands](../functions/UIContext_SortCommands.md) | `0x1403AE508` | Collects the 16-byte command records of one UIContext slot into a contiguous region of the command ring and stable-sorts them by the 64-bit key in the first qword. |
| [UIDraw_QuadFromTexelRect](../functions/UIDraw_QuadFromTexelRect.md) | `0x1403E0AC0` | Thunk-like helper for plain quads: converts a texel rectangle of a texture part into UVs and draws one quad with UIDraw_QuadTransformed. |
| [UIDraw_QuadTransformed](../functions/UIDraw_QuadTransformed.md) | `0x1403E0B80` | Emits one image quad: the rectangle rect = (x0, y0, x1, y1) mapped through the 2x3 matrix, with given UVs and one colour, as 4 vertices of 24 bytes. |
| [UILayer_Ctor](../functions/UILayer_Ctor.md) | `0x1403B0494` | Initialises a 592-byte UI layer object (the offscreen-layer record) to its defaults. |
| [UILayer_FillConstants](../functions/UILayer_FillConstants.md) | `0x1403B08AC` | Fills the layer shader's constant buffer from the layer object (matrices, colour transform, effect values, texture size reciprocals). |
| [UILayer_GetTarget](../functions/UILayer_GetTarget.md) | `0x1403B0838` | Returns the render target object a layer draws into: its own (layer+584) or else the renderer's current target. |
| [UIRender_AccumulateQuadBounds](../functions/UIRender_AccumulateQuadBounds.md) | `0x1403DF71C` | Grows the renderer's running screen bounding box with the four transformed corners of a quad just queued. |
| [UIRender_DrawLetterbox](../functions/UIRender_DrawLetterbox.md) | `0x1403B93BC` | When the output surface is a different size than the UI target, fills the border regions (letterbox / pillarbox bars) with selector program 0. |
| [UIRender_DrawOverlayQuads](../functions/UIRender_DrawOverlayQuads.md) | `0x1403B8F20` | Draws up to three textured rectangles registered at ui+8672 (48-byte records) over the base target with selector program 5. |
| [UIRender_PrepareLayers](../functions/UIRender_PrepareLayers.md) | `0x1403B85B0` | Per-frame layer setup: collects the used layers, finds overlaps, assigns draw order and atlas pages, then packs every layer's rectangle. |
| [UIRender_ResolveBase](../functions/UIRender_ResolveBase.md) | `0x1403B8BF4` | Copies the base (bottom) layer surface to the frame target once per frame, with the base-layer sort key. |
| [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md) | `0x1403B9844` | End-of-frame UI submission: composites every prepared layer, sorts the commands of all 32 contexts, merges them into one stream and executes it. |
| [UITexturePath_FromRow](../functions/UITexturePath_FromRow.md) | `0x1400FCA68` | Builds a UITextureParts path (that scheme followed by the row's text) from one row of UI table 0x8F. |
| [UnitClut_TintRow](../functions/UnitClut_TintRow.md) | `0x1402F7628` | The battle side's tint rule: turns one 16-colour palette row into a unit slot's colours in bank 3 of the palette manager. |
| [UnitClut_TintRowPlain](../functions/UnitClut_TintRowPlain.md) | `0x1402F78A4` | Calls UnitClut_TintRow with mode 8 (the channels as they are plus the offsets) for a row and a slot. |

## Structures (53)

| Name | Size (bytes) | Summary |
|---|---|---|
| [AtlasShelf](../structs/AtlasShelf.md) | 16 | The state of one layer atlas allocator (a shelf / row packer): the cursor in the current row, the start of the row, the height of the row and the page. |
| [BlendModeAlphaEntry](../structs/BlendModeAlphaEntry.md) | 1 | One row of the BlendModeAlpha table. |
| [BoneLinkPairsRow](../structs/BoneLinkPairsRow.md) | 16 | One row of the BoneLinkPairs table. |
| [ChannelExpandRow](../structs/ChannelExpandRow.md) | 1 | One row of GfxBitExpandTables. |
| [ClutBank](../structs/ClutBank.md) | 2450 | One of the 14 banks of the palette manager (g_ClutManager, from +8): 16 rows of 16 colours with a timer per row, the state of every colour and the bank's base rows. |
| [DissolveStep](../structs/DissolveStep.md) | 64 | One row of the DissolveOffsets table. |
| [FixedRampBlockRow](../structs/FixedRampBlockRow.md) | 16 | One row of EffectPoseBlendKeys. |
| [HdSheetGroup](../structs/HdSheetGroup.md) | 21144 | One of the 20 sheet groups of the battle HD layer (g_HdSheetGroups): a sheet entry kept in memory and the textures cut from it, one per piece and palette. |
| [ItemScreenPaletteRow](../structs/ItemScreenPaletteRow.md) | 2 | One row of the ItemScreenPalette table. |
| [LookPoolRecord](../structs/LookPoolRecord.md) | 13014 | One of the 15 sprite records at 0x140D005A0 (stride 0x32D6) that hold the loaded graphics of a look; records are shared by every unit that has the same sprite number. |
| [LookQueueEntry](../structs/LookQueueEntry.md) | 32 | One entry of the 16-entry load queue that Battle_BuildRosterTeam, Battle_AddJoinedUnit and the scene preview code fill (LookQueue_Add) and CharaPalette_ReloadForShape consumes; entry n starts at 0x141856728 + 32 * n, ... |
| [MapDrawIndexListRecord](../structs/MapDrawIndexListRecord.md) | 24 | One row of the MapDrawIndexLists table. |
| [NameSlotTable](../structs/NameSlotTable.md) |  | A name-to-slot table of the render device (constant buffers, textures, samplers): names hashed into a tree, each with a dense slot id. |
| [NxdDataDepthBiasRow](../structs/NxdDataDepthBiasRow.md) | 12 | One row of the nxd.depth_bias table (data table). |
| [NxdDataPostEffectDepthLUTRow](../structs/NxdDataPostEffectDepthLUTRow.md) | 40 | One row of the nxd.post_effect_depth_lut table (data table). |
| [NxdDataPostEffectDOFRow](../structs/NxdDataPostEffectDOFRow.md) | 28 | One row of the nxd.post_effect_dof table (data table). |
| [NxdDataPostEffectGlareRow](../structs/NxdDataPostEffectGlareRow.md) | 24 | One row of the nxd.post_effect_glare table (data table). |
| [NxdDataPostEffectLUTRow](../structs/NxdDataPostEffectLUTRow.md) | 20 | One row of the nxd.post_effect_lut table (data table). |
| [NxdDataPostEffectRow](../structs/NxdDataPostEffectRow.md) | 16 | One row of the nxd.post_effect table (data table). |
| [NxdDataRefinedBgAnimRow](../structs/NxdDataRefinedBgAnimRow.md) | 12 | One row of the nxd.refined_bg_anim table (data table). |
| [NxdDataRefinedBgMeshNodeInvisTypeRow](../structs/NxdDataRefinedBgMeshNodeInvisTypeRow.md) | 12 | One row of the nxd.refined_bg_mesh_node_invis_type table (data table). |
| [NxdDataRefinedBgMeshNodeRow](../structs/NxdDataRefinedBgMeshNodeRow.md) | 28 | One row of the nxd.refined_bg_mesh_node table (data table). |
| [NxdDataRefinedBgMeshPolygonCondRow](../structs/NxdDataRefinedBgMeshPolygonCondRow.md) | 20 | One row of the nxd.refined_bg_mesh_polygon_cond table (data table). |
| [NxdDataRefinedBgMeshPolygonRow](../structs/NxdDataRefinedBgMeshPolygonRow.md) | 24 | One row of the nxd.refined_bg_mesh_polygon table (data table). |
| [NxdDataRefinedBgSystemTextureRow](../structs/NxdDataRefinedBgSystemTextureRow.md) | 24 | One row of the nxd.refined_bg_system_texture table (data table). |
| [NxdDataRefinedBgTextureRow](../structs/NxdDataRefinedBgTextureRow.md) | 40 | One row of the nxd.refined_bg_texture table (data table). |
| [NxdDataRefinedBgUITextureFramesRow](../structs/NxdDataRefinedBgUITextureFramesRow.md) | 12 | One row of the nxd.refined_bg_ui_texture_frames table (data table). |
| [NxdDataRefinedBgUITextureRow](../structs/NxdDataRefinedBgUITextureRow.md) | 20 | One row of the nxd.refined_bg_ui_texture table (data table). |
| [NxdDataRefinedPermanentVFXRow](../structs/NxdDataRefinedPermanentVFXRow.md) | 12 | One row of the nxd.refined_permanent_vfx table (data table). |
| [NxdDataRefinedVFXCameraControlRow](../structs/NxdDataRefinedVFXCameraControlRow.md) | 20 | One row of the nxd.refined_vfx_camera_control table (data table). |
| [NxdDataRefinedVFXTextureRow](../structs/NxdDataRefinedVFXTextureRow.md) | 32 | One row of the nxd.refined_vfx_texture table (data table). |
| [PaletteFormat](../structs/PaletteFormat.md) | 16 | One row of the PaletteFormats table. |
| [PaletteIndexByteRow](../structs/PaletteIndexByteRow.md) | 1 | One row of GfxColourCubeIndexImage. |
| [PartyFaceIndexRow](../structs/PartyFaceIndexRow.md) | 1 | One face record index. |
| [PartyFaceRecordRow](../structs/PartyFaceRecordRow.md) | 12 | One portrait rectangle record. |
| [PortraitCodeRow](../structs/PortraitCodeRow.md) | 2 | One portrait code word. |
| [RenderContext](../structs/RenderContext.md) | 6032 | The per-thread draw state every pass fills before it packs a command: sort key, clip rectangle, render target, blend and raster words, vertex/index buffers and three binding tables (constant buffers, textures, sampler... |
| [Renderer](../structs/Renderer.md) |  | The renderer object (global g_Renderer): output size, the render-target table and the per-type target slot tables, and the UI manager. |
| [RgbaColourRow](../structs/RgbaColourRow.md) | 4 | One row of GfxColourCubePalette. |
| [SceneSpriteFaceRow](../structs/SceneSpriteFaceRow.md) | 4 | One face number. |
| [SceneUnitSlot](../structs/SceneUnitSlot.md) | 1352 | One of the 16 scene-unit records at 0x140D30038 (stride 0x548) that SceneUnit_BuildFromQueueEntry builds for a queued unit; the code addresses it by the pointer it returns, the in-use dword sits 8 bytes before that po... |
| [ShopScreenPaletteRow](../structs/ShopScreenPaletteRow.md) | 2 | One row of the ShopScreenPalette table. |
| [SlotPermutationRow](../structs/SlotPermutationRow.md) | 16 | One row of SceneSlotPermutations. |
| [SpriteClassicFileRow](../structs/SpriteClassicFileRow.md) | 8 | Where one classic sprite file is and how long it is. |
| [SpriteDirectionTablesRow](../structs/SpriteDirectionTablesRow.md) | 1 | One row of SpriteDirectionTables. |
| [SpriteHdEntryRow](../structs/SpriteHdEntryRow.md) | 4 | One HD sheet entry number. |
| [SpriteKindFlagRow](../structs/SpriteKindFlagRow.md) | 1 | One row of SpriteEffectKindFlags. |
| [SpriteLayerByteRow](../structs/SpriteLayerByteRow.md) | 1 | One row of SpriteLayerByteRows. |
| [SpriteLookAttributeRow](../structs/SpriteLookAttributeRow.md) | 4 | One look attribute row. |
| [SpriteMotionByKindRow](../structs/SpriteMotionByKindRow.md) | 1 | One row of SpriteMotionByKind. |
| [TextureIdRow](../structs/TextureIdRow.md) | 4 | One row of SpriteShapeHdTexture. |
| [TextureWindowWordRow](../structs/TextureWindowWordRow.md) | 2 | One row of GfxTextureWindowParams. |
| [UnitSpritePosePackRow](../structs/UnitSpritePosePackRow.md) | 2 | One row of the UnitSpritePosePack table. |

## Globals (14)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_DefaultSamplerWord](../globals/g_DefaultSamplerWord.md) | `0x141D8BC7C` | `uint32` | Default sampler word every render context is reset to (masked with 0x7FFFFFFF). |
| [g_DialogueFaceSlot0](../globals/g_DialogueFaceSlot0.md) | `0x142FF9EDC` | `int32[3]` | Dialogue face slot values 0..2 (0x142FF9EDC, EE0, EE4): unmapped portrait codes; Unit_GetSpriteSetId writes slot 0 with the save-record branch's code; read by the event and dialogue face windows. |
| [g_FaceDisplayMode](../globals/g_FaceDisplayMode.md) | `0x142FF9ED8` | `int32` | Face display mode word: when (mode & ~2) is 0 the face readers map a portrait code through SpriteId_ToShape, else they use the raw code; written 0 then 2 by sub_140210AF0 (battle setup), 0 by Video_RefreshState and su... |
| [g_FaceG2dEntryByFace](../globals/g_FaceG2dEntryByFace.md) | `0x140714EA0` | `int32[206]` | g2d (pack) entry number per face number 0..205 for the HD layer (row 0 -1, rows 155..158 -1); four readers, each bounding the face with 0xCD. |
| [g_GraphicsLevel](../globals/g_GraphicsLevel.md) | `0x142C81554` | `float` | Graphics level; Unit_GetSpriteSetId's save-record branch and the battle palette upload test it against 2.0 (I: 2.0 and up = enhanced graphics). |
| [g_HdFaceSlotValues](../globals/g_HdFaceSlotValues.md) | `0x142E7FCAC` | `int32[]` | HD-layer face slot values (stride 4 dwords per slot); Unit_GetSpriteSetId writes [0]; HdLayer_BindSheetTexture and sub_14041DAA4 read [4 * slot]. |
| [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md) | `0x1437A59E0` | `int32[10]` | Battle face value per look pool record 0..9: sub_14026E838 stores the scene unit's sprite byte; cleared to -1 by sub_140210AF0, saved and restored by sub_140304BEC; ten readers use it as a face number behind the 0xCD ... |
| [g_PortraitCodeA](../globals/g_PortraitCodeA.md) | `0x140680070` | `uint16[211]` | Copy A of the portrait code words (one of six identical copies), read by PartyUnit_BuildJobRecord. |
| [g_PortraitCodeD](../globals/g_PortraitCodeD.md) | `0x140681A90` | `uint16[211]` | Copy D of the portrait code words, read by EventMessage_Scripted (the speaker's portrait). |
| [g_PortraitCodeE](../globals/g_PortraitCodeE.md) | `0x1406829F0` | `uint16[211]` | Copy E of the portrait code words, read by sub_140300768 and sub_140300D74. |
| [g_PortraitCodeF](../globals/g_PortraitCodeF.md) | `0x140683A70` | `uint16[211]` | Copy F of the portrait code words (one of six identical copies), read by sub_14032AB3C. |
| [g_RenderDevice](../globals/g_RenderDevice.md) | `0x140C696A8` | `RenderDevice *` | The render device: name-to-slot tables for constant buffers (+5056), textures (+5064) and samplers (+5072), the render-context array (+4984, stride 6032, count +5088) and the command-memory pool counters (+5144..+5152). |
| [g_Renderer](../globals/g_Renderer.md) | `0x143CDA098` | `Renderer *` | The renderer object: output size (+6568 / +6572), the render-target table (+20832, 40 B per target), the per-type target and slot tables (+23736, +24224) and the UI manager (+37936). |
| [g_SceneIdWord](../globals/g_SceneIdWord.md) | `0x141848BB0` | `uint16` | Scene id word; Unit_GetSpriteSetId and SceneUnit_EntryById take the selector branch (scene unit entries) when it is 21, 43, 44 or 51. |

## Registries (3)

| Name | Summary |
|---|---|
| [LayerPassKeys](../registries/LayerPassKeys.md) | The pass constants OR-ed into the 64-bit sort key of the layer commands. |
| [SamplerSlots](../registries/SamplerSlots.md) | The sampler names of the render device (31 live) and their slot ids. |
| [SpriteNumberTables](../registries/SpriteNumberTables.md) | Every table the executable indexes by sprite number, with the row count, the bound the code applies. |

## Shaders (9)

| Name | Stage | Technique file | Summary |
|---|---|---|---|
| [AlphaCopy_PS](../shaders/AlphaCopy_PS.md) | pixel | uirender.tec | Copies a layer's alpha into the effect alpha target: writes (0, 0, 0, source alpha). |
| [FullscreenTriangle_VS](../shaders/FullscreenTriangle_VS.md) | vertex | uirender.tec | Vertex shader of the alpha copy: an oversized triangle built from the vertex index, so no vertex buffer is bound. |
| [LayerBlendNormal_PS](../shaders/LayerBlendNormal_PS.md) | pixel | uirender.tec | The layer blit pixel shader for blend type 0 (normal), offset variant 0: composites one layer's premultiplied pixels over the frame target by a read-modify-write of an unsigned-normalised UAV. It is the first of the 3... |
| [LayerBlendNormalOffsets_PS](../shaders/LayerBlendNormalOffsets_PS.md) | pixel | uirender.tec | Blend type 0 with the offset variant (digit 1 = 1): the same over composite as LayerBlendNormal_PS with extra samples at the layer's three offset vectors (selected when any of them is non-zero). |
| [LayerQuadOffset_VS](../shaders/LayerQuadOffset_VS.md) | vertex | uirender.tec | Vertex shader of the drop-shadow pass: moves the layer quad by the shadow offset and keeps its texture coordinates. |
| [LayerShadow_PS](../shaders/LayerShadow_PS.md) | pixel | uirender.tec | Drop-shadow pass of a UI layer: darkens the target in place under the layer's blurred alpha, before the layer itself is drawn. |
| [MaskComposite_PS](../shaders/MaskComposite_PS.md) | pixel | uirender.tec | Mask pass of a masked layer (the screen title): the layer's gradient times the mask buffer. |
| [UIImage_PS](../shaders/UIImage_PS.md) | pixel | uirender.tec | The plain UI image pixel shader (UI technique program 0): every textured UI image (discs, the selection ring, the cursor glove, plates, floor tiles, line parts). |
| [UIImage_VS](../shaders/UIImage_VS.md) | vertex | uirender.tec | Vertex shader of the UI image program: position (x, y, z, w) times the projection in constant rows 0..3; colour and texture coordinate passed through (no snapping). |

## Shader programs (4)

| Name | Selector | Program index | Summary |
|---|---|---|---|
| [LayerAlphaCopy](../programs/LayerAlphaCopy.md) | UI manager selector #10 | 0 | First step of a layer's drop shadow: copies the layer alpha into RT3_EffectAlpha inside the layer's atlas rectangle. |
| [LayerBlit](../programs/LayerBlit.md) | UI manager selector #9 | 0 | The layer blit: draws one layer's quad (rect - atlas offset) with the layer blend type as selector digit 0 and the offset-vector flag as digit 1. |
| [LayerShadow](../programs/LayerShadow.md) | UI manager selector #10 | 1 | The drop-shadow draw: the layer quad moved by the offset, darkening the target under the blurred alpha. |
| [UIImage](../programs/UIImage.md) | UI technique (UIRender_ApplyDrawState) | 0 | Draws every textured UI image: program 0 of the UI technique (shader objects 1 and 10). |

## Render targets (8)

| Name | Index | Size | Format | Summary |
|---|---|---|---|---|
| [RT26_LayerContent](../render-targets/RT26_LayerContent.md) | RT 26 | output size | `R8G8B8A8_UNORM` | Layer content target: at the selection ring's glow pass it held the ring layer's own (sharp) pixels in its atlas place; the glow shader reads it as its second texture. |
| [RT27_GlowBlurred](../render-targets/RT27_GlowBlurred.md) | RT 27 | output size | `R8G8B8A8_UNORM` | Full-resolution blurred layer read by the glow pass (its first texture); for a half-size blur it is the bilinear upscale of RT32_HalfBlur. |
| [RT28_BlurScratch](../render-targets/RT28_BlurScratch.md) | RT 28 | output size | `R8G8B8A8_UNORM` | Scratch target of the UI blur's horizontal pass (UIBlur_Run gets 28 as its scratch index from the drop-shadow pass). |
| [RT30_MaskBuffer](../render-targets/RT30_MaskBuffer.md) | RT 30 | output size | `R8_UNORM` | Mask buffer of masked layers: the mask pass reads its red channel. |
| [RT32_HalfBlur](../render-targets/RT32_HalfBlur.md) | RT 32 | half output size (640 x 360 at 720p) | `R8G8B8A8_UNORM` | Half-size blur target: first the 2 x 2 box downsample of the layer, finally the vertically blurred result. |
| [RT37_HalfBlurTemp](../render-targets/RT37_HalfBlurTemp.md) | RT 37 | half output size (640 x 360 at 720p) | `R8G8B8A8_UNORM` | Half-size blur scratch: holds the horizontal pass of the half-size blur. |
| [RT3_EffectAlpha](../render-targets/RT3_EffectAlpha.md) | RT 3 | output size (1280 x 720 at 720p) | `R8G8B8A8_UNORM` | Effect alpha atlas: each layer with a drop shadow copies its alpha here (inside its atlas rectangle), the UI blur blurs it in place, and the shadow pass samples it. |
| [UITarget_Frame](../render-targets/UITarget_Frame.md) | per-type slot 2 (Renderer +0x5CB8 + 800 x type) | output size (1280 x 720 at 720p) | `UNORM (8 bits per channel by the captures)` | The UI frame target: the render target every layer blit composites onto (GUILayer_BlitFinal, GUILayer_BlurShadowPass and the glow pass take it from the same per-type table entry, slot 2 of the 800-byte row of the laye... |

## File formats (2)

| Name | Extension | Summary |
|---|---|---|
| [SpriteSheetEntries](../formats/SpriteSheetEntries.md) | `(g2d entries)` | The sprite data of a unit look: two HD sheet entries, the classic sprite file and its palette rows. |
| [tec](../formats/tec.md) | `.tec` | Shader technique file (for example uirender.tec): the DXBC shader containers of a technique, its programs, sampler presets and the binding tables that tie each shader's registers to engine names. |

## Flows (6)

| Name | Summary |
|---|---|
| [BattleResumeRestoresTheLooks](../flows/BattleResumeRestoresTheLooks.md) | How a battle resumed from a payload gets its looks back: the setup clears the pool's sprite bytes, the payload fills the snapshot region, and Battle_RestoreSceneVars copies the units, the load queue and the 15 pool re... |
| [FrameUiSubmission](../flows/FrameUiSubmission.md) | How one frame's UI reaches the GPU, and why the order matters: commands are packed on the CPU in one order and executed by sort key in another, and every pass inherits the context state it does not set. |
| [LayerDropShadow](../flows/LayerDropShadow.md) | The drop shadow of a UI layer, end to end (decoded and reproduced from mid-frame GPU captures). |
| [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md) | The glow of a UI layer with a blur radius from 3.2 to 6.4 (the Job Tree selection ring: radius 4.0), stage by stage, each stage reproduced from a mid-frame GPU capture (2026-10-30). |
| [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md) | How a party unit's face reaches a menu with enhanced graphics: the save record's marker and job give a look index, the index a portrait code, the code a byte and a colour, the byte a face number through the face table... |
| [UiLayerComposite](../flows/UiLayerComposite.md) | One frame of UI, layer by layer, in the order the game does it: how a widget becomes layers, which target a layer's draws go to, when that target is cleared, what runs on it, and how it is blended onto the frame. |

## Observed behaviours (47)

| Name | Scope | Summary |
|---|---|---|
| [BattleFaceIsThePoolSpriteByte](../behaviors/BattleFaceIsThePoolSpriteByte.md) | engine (battle faces) | A battle unit's face is not a portrait code: the look pool's sprite byte is stored as the pool's face value and ten readers use it as the face number behind the 0xCD cap; a separate code exists only for one special unit. |
| [BattleMotionNumbers](../behaviors/BattleMotionNumbers.md) | engine (battle unit animation choice) | A battle action names its animation by a motion number from two tables (one per ability, one per weapon type); the unit stores motion + 1, and the motion number is the pair index of the classic animation file (front v... |
| [BattlePaletteSourceByLookRange](../behaviors/BattlePaletteSourceByLookRange.md) | engine (battle palette row) | Where a battle unit's palette row comes from depends on its sprite number: the generic looks (96..133) and 159..162 take the unit's byte +4, every other look its CharShape row's colour override or the queue palette. |
| [BlendFactorUsesStoredSourceAlpha](../behaviors/BlendFactorUsesStoredSourceAlpha.md) | GPU (the test machine's GPU and driver), UI draws into an 8-bit target | The destination factor of a UI draw's blend (1 - source alpha) uses the source alpha as the 8-bit target stores it: result = round(source) + round(destination * (1 - round8(source alpha))), with round8 = the target's ... |
| [BlendTermsRoundedSeparately](../behaviors/BlendTermsRoundedSeparately.md) | GPU (the test machine's GPU and driver), UI draws into a layer target | A UI draw's blend into its 8-bit target behaves as if both terms were rounded to 8 bits before they are added: result = round(source) + round(destination * (1 - source alpha)), not round(source + destination * (1 - so... |
| [CharShapeKeyByteSites](../behaviors/CharShapeKeyByteSites.md) | engine (CharShape key) | CharShape_ApplyClut takes its key as a byte: the callee's zero-extending byte load of the key at 0x14026C7C0, the menu caller's byte move of the look at 0x14026E806 and the battle copy loop's byte mask at 0x14026E8D0. |
| [CharShapeRowMissingFaultsTheFormation](../behaviors/CharShapeRowMissingFaultsTheFormation.md) | engine (battle formation) | The battle formation code reads a CharShape row (NXD 174) keyed by the scene unit's sprite byte and, on one path, reads the row's byte +0x2C with no row: a sprite number without a CharShape row faults. |
| [ClassicSpriteFilesByNumber](../behaviors/ClassicSpriteFilesByNumber.md) | the sprite pack, classic palettes and portraits of stock shapes | Classic sprite files are numbered entries of fftpack.bin, and the `offset` column of the classic kind tables is that file number; the game has no portrait for shapes 56 and 57. |
| [CursorDrawnThroughLayerTarget](../behaviors/CursorDrawnThroughLayerTarget.md) | the finger cursor's glove (UI layer) | The glove reaches the screen in two 8-bit stores: it is drawn into a cleared layer target (premultiplied, rounded) and that layer is then blended onto the frame (dst = layer + dst * (1 - layer alpha), rounded again). |
| [EffectPassesInheritDefaultSampler](../behaviors/EffectPassesInheritDefaultSampler.md) | engine | Layer effect passes read their textures through g_Sampler without setting it; because they are packed before the UI draws that set it, they always get the default word (point filter, wrap). |
| [EnhancedDrawsHdSheetsWithTheClassicFilePalette](../behaviors/EnhancedDrawsHdSheetsWithTheClassicFilePalette.md) | engine (unit sprites) | In the enhanced build a unit's HD sprite sheet is drawn with the palette taken from the classic sprite file named in the classic file table, so the colours follow that file, not the sheet. |
| [FaceLookupInlineCopiesDisagreeAboveCode159](../behaviors/FaceLookupInlineCopiesDisagreeAboveCode159.md) | engine (portrait face numbers) | The face-number lookup exists as SpriteId_ToShape and ten inline copies; for codes above 0x9F five of the copies answer differently from the function, so one table row cannot stand for all of them. |
| [FaceNumberCapsClipRawCodesToo](../behaviors/FaceNumberCapsClipRawCodesToo.md) | engine (portrait face numbers) | Sixteen readers cap the face number at 0xCD (205): the twelve caps below and the four readers of the HD face table g_FaceG2dEntryByFace. |
| [GenericUnitSpriteNumberFromJob](../behaviors/GenericUnitSpriteNumberFromJob.md) | engine (unit sprite selection) | A generic unit has no stored sprite number: the game derives it from the job and the sex, with the same sum in at least ten places, and every other job id falls back to a default. |
| [HdSheetFromSlotColoursFromRecord](../behaviors/HdSheetFromSlotColoursFromRecord.md) | engine (Enhanced battle sprite) | In Enhanced a pool's HD sheet comes from its sheet slot (the g2d entry) while its colours come from the pool record's palette. |
| [JobCardPictureOpacityAndPlacement](../behaviors/JobCardPictureOpacityAndPlacement.md) | engine (job card pictures) | A job card (the painting behind the Status panel) is a 400 x 652 picture that is never fully opaque and fades out toward its lower left; its figure touches the top edge with the head left of the middle. |
| [JobChangeTransitionShapeFromTheListEntryByte](../behaviors/JobChangeTransitionShapeFromTheListEntryByte.md) | engine (Change Job transition sprite) | While a job change plays its light pillar, the Status header figure is drawn in a shape JobScreen_UpdateState asks Unit_ResolvePreviewShape for, passing the Change Job list entry's job as one byte; for a generic unit ... |
| [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md) | every layer of a UI frame that is packed (composited, kind 0 or 1, none of the flags +78 / +486 / +488); the Job Tree frame was checked end to end | Where a UI layer's pixels are placed in the layer atlas each frame: the layers are put in a fixed order (their order key), and a shelf packer places each layer's integer rectangle plus a margin of 2 px (32 px when a b... |
| [LayerBlitOverFrameTarget](../behaviors/LayerBlitOverFrameTarget.md) | every layer of blend type 0 (normal) | Store 2: the layer is blended onto the frame target by a pixel shader that reads the frame pixel through a UAV and writes it back: frame = layer + frame x (1 - layer alpha) in premultiplied form, per channel, from the... |
| [LayerCompositeOrder](../behaviors/LayerCompositeOrder.md) | the order of layers and of draws on the frame | Layers are composited in the order the game's draw traversal opened them, but only layers whose rectangles overlap are ordered against each other: each layer gets an order number that is one more than the creation ind... |
| [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md) | every layer's own draws | Store 1: a layer's UI draws go into the layer content target (RT 26, RGBA8 UNORM, 1280 x 720) inside the layer's atlas rectangle, which starts cleared to (0, 0, 0, 0), with the fixed-function blend ONE / INV_SRC_ALPHA... |
| [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md) | engine (battle look pool size) | The look pool's 15 records are not a constant that a same-length change can raise: the record block is followed at once by the scene-unit slots, each pool index owns fixed GPU upload positions or buffers, the HD sheet... |
| [LookSitesUseTheSaveRecordNotTheSlot](../behaviors/LookSitesUseTheSaveRecordNotTheSlot.md) | engine (portraits and faces) | The six portrait readers compute the look from the unit's marker, job byte and sex each time through six copies of one 211-word table; none of them reads the battle slot, and they are separate from the battle sprite p... |
| [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md) | engine (battle sprite loading) | The battle loader already assigns small per-battle slots to looks: a 16-entry queue, 15 look pool records shared by equal sprite numbers, 16 scene-unit records and 10 HD sheet entries. |
| [LookSumSeesTheBaseJob](../behaviors/LookSumSeesTheBaseJob.md) | engine (portrait look index) | Five functions compute a save unit's portrait look index from its job byte (2 * job - 52, + 1 for marker 0x81), each against its own copy of the portrait code words. |
| [MidBattleJoinLoadsLooks](../behaviors/MidBattleJoinLoadsLooks.md) | engine (battle join) | A unit that joins mid-battle is queued by Battle_AddJoinedUnit and loaded by running the look loader once per frame until it returns 0; the loader's file reads are synchronous. |
| [NamedCharactersKeepTheirOwnLookWhateverTheirJob](../behaviors/NamedCharactersKeepTheirOwnLookWhateverTheirJob.md) | engine (unit look by character byte) | A named character (character byte +0 of the save, party or battle record below 0x80, e.g. |
| [PoolRecordKeepsItsSpriteAcrossTheReset](../behaviors/PoolRecordKeepsItsSpriteAcrossTheReset.md) | engine (battle sprite loading) | A look pool record keeps the sprite it holds (byte +1) after LookPool_ResetForBattleLoad, and the load pass skips the classic file of a queued sprite that any record's +1 already names; only the battle setup clears +1... |
| [PortraitCodeIsAByteOnTheSaveRecordPath](../behaviors/PortraitCodeIsAByteOnTheSaveRecordPath.md) | engine (party faces) | On the save-record path a portrait code can only carry 256 distinct faces: the code reader refuses a code with bit 8 or 9 and the cell function returns the low byte. |
| [RasterizerSnapsTo1_256Px](../behaviors/RasterizerSnapsTo1_256Px.md) | GPU (the test machine's GPU and driver) | Vertex positions are snapped to 1/256 of a pixel (rounded to nearest) before rasterization, so a UI quad at a third of a pixel (the 2/3 screen scale) is drawn from slightly moved corners and samples its texture at sli... |
| [ResumeLoadsTheLookStateTwice](../behaviors/ResumeLoadsTheLookStateTwice.md) | engine (battle resume) | A battle resumed from a payload copies the payload twice around the scene-variable restore, builds no scene unit but restores the scene-unit records whole, and rebuilds existing scene units from the restored slot and ... |
| [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md) | engine (battle unit shape) | A scene unit's shape (sprite byte +0xA) is the sprite word of its load queue entry; a battle unit's shape byte +0x18F is written only by the unit builders and comes back in the battle snapshot, while the save keeps no... |
| [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md) | engine (unit sheets) | The 15 colours of a unit sheet (16 with the transparent one) are a property of two CPU routines that expand 4-bit pixels through 16 converted colours; both hand the GPU 32-bit textures, and the battle one already has ... |
| [SpriteLookupFailuresPastTheTables](../behaviors/SpriteLookupFailuresPastTheTables.md) | engine (sprite readers) | What went wrong in game when a sprite number or job id above the stock range reached a reader: three failures. |
| [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md) | engine (unit sprite number) | Which stores of a unit's sprite number are bytes and which are wider: the battle path keeps the number in bytes (limit 255) while the menu path carries it as a 32-bit value. |
| [SpriteSheetPortraitAndPartFiles](../behaviors/SpriteSheetPortraitAndPartFiles.md) | engine (sprite sheet, classic file and portrait files) | A unit sprite is two HD sheet entries plus a classic file whose first 0x200 bytes are its palettes; a portrait is a texture plus a part file that the game asks for by name. |
| [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md) | engine (sprite number tables) | The game reaches every table indexed by a look number only through a fixed set of instructions and bounds. |
| [SpriteTablesEndAtSprite169](../behaviors/SpriteTablesEndAtSprite169.md) | engine (sprite number tables) | The tables indexed by sprite number all have 170 rows (sprites 0 to 169); the unit queue and the face readers compare against fixed bounds, so a sprite number above 169 needs every table and every bound to grow. |
| [TexelWeights8Bit](../behaviors/TexelWeights8Bit.md) | GPU (the test machine's GPU and driver) | Bilinear filtering weights are the sub-texel fraction rounded to 1/256 (8 bits), not exact: the filtered colour of a texel pair at fraction f uses round(f * 256) / 256. |
| [TextFillPassDrawnAsOneShape](../behaviors/TextFillPassDrawnAsOneShape.md) | UI text (SDF font runs: the screen title, the job name tag, the level boards) | A text run's fill pass reaches its target as one shape: the fill glyphs are drawn without blending under a depth test (LESS_EQUAL, depth = 1 - the distance at the pixel centre), so where neighbouring glyph quads overl... |
| [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md) | engine (battle unit colours) | A battle unit's 16 colours are its palette row put through one tint rule (status tints, ambient light), then moved by the palette manager's timed fades; the result is uploaded to the emulated video memory, where the H... |
| [UnitFaceFromSpriteNumber](../behaviors/UnitFaceFromSpriteNumber.md) | engine (small unit portraits) | The small unit face is chosen from the sprite number through three portrait-code tables, then a face number, and the face number is capped at 0xCD; the status card's large job picture follows a different path through ... |
| [UnitFaceIndexReadsTheTableAfterTheHdTable](../behaviors/UnitFaceIndexReadsTheTableAfterTheHdTable.md) | engine (party faces) | Unit_GetFaceIndex reads the face index of a monster job from the table right after the HD sheet entry table, through a virtual base that falls inside the HD table, so an address-range census counts it as an HD reader ... |
| [UnitFigureRenderSlotNumbers](../behaviors/UnitFigureRenderSlotNumbers.md) | engine (menu unit figures) | Every unit figure a menu draws is registered under a render slot number 0..255; the Change Job list, the Job Tree and the Status header each use fixed numbers, so two figures registered under one number draw as one. |
| [UnitMovementAnimationTables](../behaviors/UnitMovementAnimationTables.md) | engine (unit sprite animation) | Eight data tables, one per sprite class, hold the unit's movement animations only (standing, walking, floating, turning, jumping, a few single-frame poses): a row per step, keyed by animation id and step number; attac... |
| [UnormStoreRoundsHalfDown](../behaviors/UnormStoreRoundsHalfDown.md) | GPU (the test machine's GPU and driver) | When a shader stores a float into an 8-bit UNORM target, an exact half rounds down: 16.5 stores 16, 9.5 stores 9. |
| [VertexColourBytesTruncated](../behaviors/VertexColourBytesTruncated.md) | engine (UI node colours) | A UI node's vertex colour reaches the shader as bytes: each channel is the product of the node colour and its opacity, truncated to an integer. |

## Tables (48)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [BlendModeAlpha](../tables/BlendModeAlpha.md) | Executable |  | 4 rows of 1 bytes | Alpha for each of the four semi-transparency modes (half, add, subtract, quarter). |
| [BoneLinkPairs](../tables/BoneLinkPairs.md) | Executable |  | 33 rows of 16 bytes | The 33 bone name pairs that define the chains of a model skeleton (spine, neck, head, arms, hands, fingers, legs, toes, jaw, face, nose flap, forearm and shin extension bones, waist, tail segments). |
| [DissolveOffsets](../tables/DissolveOffsets.md) | Executable (initialised data) |  | 32 rows of 64 bytes | Pixel-order table of a dissolve (reveal) effect: 32 steps, each with 32 offsets. |
| [EffectPoseBlendKeys](../tables/EffectPoseBlendKeys.md) | Executable |  | 10 blocks of 16 bytes | Ten blocks of 16-bit fixed point (4096 = 1.0) ramp values copied by a sprite effect update. |
| [FaceG2dEntryByFace](../tables/FaceG2dEntryByFace.md) | Executable (constant) |  | 206 entries of 4 bytes | g2d (pack) entry number per face number 0..205 for the HD layer (row 0 -1, rows 155..158 -1); four readers, each bounding the face with 0xCD. |
| [GfxBitExpandTables](../tables/GfxBitExpandTables.md) | Executable |  | 16 + 32 + 64 rows of 1 byte | Lookup tables that expand 4, 5 and 6 bit colour channels to 8 bits in the texture format converters. |
| [GfxBlueNoiseTexturePaths](../tables/GfxBlueNoiseTexturePaths.md) | Executable |  | 16 rows of 8 bytes | File paths of the sixteen 64 by 64 blue noise textures the renderer loads at set-up. |
| [GfxColourCubeIndexImage](../tables/GfxColourCubeIndexImage.md) | Executable |  | 1024 bytes (size inferred) | 8-bit index image drawn with the colour cube palette (size word 32 stored by the set-up). |
| [GfxColourCubePalette](../tables/GfxColourCubePalette.md) | Executable |  | 256 rows of 4 bytes | 256-colour palette whose entries step by 8 in red, green and blue; the palette of the index image at 0x14078E2B0. |
| [GfxTextureWindowParams](../tables/GfxTextureWindowParams.md) | Executable |  | 4 words (head of a 2048-byte object) | Texture window parameter words (mask x / y, offset x / y) of a draw mode command. |
| [ItemScreenPalette](../tables/ItemScreenPalette.md) | Executable |  | 256 rows of 2 bytes | 256 colours (15-bit) uploaded to the video page row used by the legacy item and map title textures. |
| [LookPoolFaceValue](../tables/LookPoolFaceValue.md) | Executable (filled at run time) |  | 10 entries of 4 bytes | Battle face value per look pool record 0..9: sub_14026E838 stores the scene unit's sprite byte; cleared to -1 by sub_140210AF0, saved and restored by sub_140304BEC; ten readers use it as a face number behind the 0xCD ... |
| [MapDrawIndexLists](../tables/MapDrawIndexLists.md) | Executable |  | 50 rows of 24 bytes | Per battle map, two lists of map draw-record indices that the two map draw passes treat specially. |
| [NxdDataDepthBias](../tables/NxdDataDepthBias.md) | NXD file | 315 | 12 rows of 12 bytes | Twelve depth-bias values for effect textures. |
| [NxdDataPostEffect](../tables/NxdDataPostEffect.md) | NXD file | 228 | 2 rows of 16 bytes | Two post effect definitions with an effect file path. |
| [NxdDataPostEffectDepthLUT](../tables/NxdDataPostEffectDepthLUT.md) | NXD file | 284 | 30 rows of 40 bytes | Depth lookup parameters (30). |
| [NxdDataPostEffectDOF](../tables/NxdDataPostEffectDOF.md) | NXD file | 227 | 34 rows of 28 bytes | Depth-of-field parameters (34). |
| [NxdDataPostEffectGlare](../tables/NxdDataPostEffectGlare.md) | NXD file | 256 | 19 rows of 24 bytes | Glare parameters (19). |
| [NxdDataPostEffectLUT](../tables/NxdDataPostEffectLUT.md) | NXD file | 285 | 31 rows of 20 bytes | Colour lookup parameters (31). |
| [NxdDataRefinedBgAnim](../tables/NxdDataRefinedBgAnim.md) | NXD file | 49 | 280 rows of 12 bytes | Remastered background animations keyed by map and slot. |
| [NxdDataRefinedBgMeshNode](../tables/NxdDataRefinedBgMeshNode.md) | NXD file | 153 | 1429 rows of 28 bytes | Remastered background mesh nodes keyed by map, group and node. |
| [NxdDataRefinedBgMeshNodeInvisType](../tables/NxdDataRefinedBgMeshNodeInvisType.md) | NXD file | 312 | 1 rows of 12 bytes | Mesh node invisibility type (one row). |
| [NxdDataRefinedBgMeshPolygon](../tables/NxdDataRefinedBgMeshPolygon.md) | NXD file | 232 | 4037 rows of 24 bytes | Remastered background polygons keyed by map and index (4037), linked to conditions. |
| [NxdDataRefinedBgMeshPolygonCond](../tables/NxdDataRefinedBgMeshPolygonCond.md) | NXD file | 326 | 78 rows of 20 bytes | Polygon condition rows (78). |
| [NxdDataRefinedBgSystemTexture](../tables/NxdDataRefinedBgSystemTexture.md) | NXD file | 141 | 870 rows of 24 bytes | System textures of remastered backgrounds, triple keyed. |
| [NxdDataRefinedBgTexture](../tables/NxdDataRefinedBgTexture.md) | NXD file | 71 | 1338 rows of 40 bytes | Textures of remastered backgrounds, triple keyed (1338 rows). |
| [NxdDataRefinedBgUITexture](../tables/NxdDataRefinedBgUITexture.md) | NXD file | 223 | 20 rows of 20 bytes | UI textures of remastered backgrounds, with frame id arrays. |
| [NxdDataRefinedBgUITextureFrames](../tables/NxdDataRefinedBgUITextureFrames.md) | NXD file | 222 | 17 rows of 12 bytes | Frame texture file paths of background UI textures. |
| [NxdDataRefinedPermanentVFX](../tables/NxdDataRefinedPermanentVFX.md) | NXD file | 321 | 21 rows of 12 bytes | Permanent effect definitions (21). |
| [NxdDataRefinedVFXCameraControl](../tables/NxdDataRefinedVFXCameraControl.md) | NXD file | 317 | 1 rows of 20 bytes | Effect camera control parameters (one row). |
| [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md) | NXD file | 202 | 487 rows of 32 bytes | Effect textures (487) linked to depth bias and camera control. |
| [PaletteFormats](../tables/PaletteFormats.md) | Executable |  | 2 rows of 16 bytes | Two palette format descriptors (16- and 256-colour palettes). |
| [PartyFaceIndex](../tables/PartyFaceIndex.md) | Executable |  | 74 rows of 1 byte | Maps a unit marker or job to a face record index. |
| [PartyFaceRecords](../tables/PartyFaceRecords.md) | Executable |  | 90 rows of 12 bytes | Portrait rectangle and variant of each party face. |
| [PortraitCodes](../tables/PortraitCodes.md) | Executable |  | 211 rows of 2 bytes in each of five byte-identical copies (0x1406807C0, 0x140680070, 0x140681A90, 0x1406829F0, 0x140683A70) | Portrait code word of each generic look. |
| [SceneSlotPermutations](../tables/SceneSlotPermutations.md) | Executable |  | 24 rows of 16 bytes | The 24 permutations of the four slots 0..3, walked by a sprite effect update to pick a slot order. |
| [SceneSpriteToFace](../tables/SceneSpriteToFace.md) | Executable |  | 160 rows of 4 bytes | Face number of each scene sprite id, read by the sprite-id-to-shape function and five inline copies of it. |
| [ShopScreenPalette](../tables/ShopScreenPalette.md) | Executable |  | 16 rows of 2 bytes (first block) | 16 colours (15-bit) copied into the video page by the shop screen set-up. |
| [SpriteClassicFilesByShape](../tables/SpriteClassicFilesByShape.md) | Executable |  | 170 rows of 8 bytes | Classic sprite file locator per shape, used for the palette load of the HD sheet. |
| [SpriteClassicFilesByShapeB](../tables/SpriteClassicFilesByShapeB.md) | Executable |  | 170 rows of 8 bytes | Second copy of the classic sprite file locator table, read when the language code is 0; byte-identical to SpriteClassicFilesByShape. |
| [SpriteDirectionTables](../tables/SpriteDirectionTables.md) | Executable |  | 184 bytes in six sub-tables | Small per-facing tables read by the sprite record code: mirror flag words, frame flag masks, walk phase steps and palette base words. |
| [SpriteEffectKindFlags](../tables/SpriteEffectKindFlags.md) | Executable |  | 32 rows of 1 byte | One flag byte per sprite record kind read by the effect placement code. |
| [SpriteHdEntryByShape](../tables/SpriteHdEntryByShape.md) | Executable |  | 170 rows of 4 bytes | First HD sheet entry of every look in the g2d pack. |
| [SpriteLayerByteRows](../tables/SpriteLayerByteRows.md) | Executable |  | 3 rows of 24 bytes (80 to the next symbol) | Three rows of per-kind bytes stored into the sprite object (+18 / +19). |
| [SpriteLookAttributes](../tables/SpriteLookAttributes.md) | Executable |  | 170 rows of 4 bytes | Per look: which frame file and animation sequence file kind it uses, the pose remap flag and a scale byte. |
| [SpriteMotionByKind](../tables/SpriteMotionByKind.md) | Executable |  | 2 rows of 16 bytes | Motion number per sprite kind class, in two variants chosen by a flag test. |
| [SpriteShapeHdTexture](../tables/SpriteShapeHdTexture.md) | Executable |  | 82 rows of 4 bytes (84 to the next symbol) | HD texture id per sprite shape (effect and scene sprites), -1 for none. |
| [UnitSpritePosePack](../tables/UnitSpritePosePack.md) | Executable (initialised data) |  | 107 offsets | Offset index and pose records for drawing a unit sprite as a rotated quad: 107 offsets, records of 28 bytes. |
