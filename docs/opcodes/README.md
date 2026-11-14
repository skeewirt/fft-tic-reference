# Event opcodes

The event script language: one flat data record per opcode (format: docs/guides/opcodes-format.md). Index page only; the records are the documentation.

242 records. Format of a record: [kinds/opcode.json](../../kinds/opcode.json). Data: [data/opcodes.jsonl](../../data/opcodes.jsonl).

| Op | Name | Operand bytes | Conf | Effect |
|---|---|---|---|---|
| `0x00` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x01` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x02` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x03` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x04` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x05` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x06` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x07` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x08` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x09` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x0A` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x0B` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x0C` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x0D` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x0E` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x0F` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x10` | DisplayMessage | 14 / 17 | V | Starts the dialogue-window task to show a message. |
| `0x11` |  | 5 | V | For each unit the id names, applies the mode to bit 0 of the flag byte at +143 (and zeroes the word at +24 for mode 1), passes the action code to a helper routine, and waits for frames when the code is 83, 84 or 85. |
| `0x12` | LookUpSpeakerUnit | 2 | V | Passes its 16-bit operand to the shared speaker and unit lookup routine and ignores the result. |
| `0x13` | ResetCamera | 2 | V | Stores its operand in a global, waits two frames, then resets the camera state (the angles, position and matrices that opcode 0x1B interpolates) to its defaults. |
| `0x14` |  | 2 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x15` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x16` | WaitForSkipOrButton | 0 | V | Waits frame by frame until the current task's kind value becomes 3, or the skip flag is set, or one of three button groups is active; it skips the wait for one particular event when two state flags are clear. |
| `0x17` | NoOp17 | 5 | V | Does nothing; the interpreter goes straight to the next instruction. |
| `0x18` |  | 6 | V | Stores its operands in globals (a 16-bit value, a unit looked up from the byte at +3, and three bytes), sets event variable 31 to 0, then waits two frames. |
| `0x19` | StartStateMove | 16 | V | On its first run (while a global flag is zero) it saves seven state-block values and four globals, then starts a task that moves those seven values toward the operand targets over the step count, shaped by the curve g... |
| `0x1A` | ChangeScreenColor | 5 | V | Starts a task that applies a screen colour change and waits for the duration the last operand selects. |
| `0x1B` | MoveCamera | 14 | V | Starts a task that moves the camera from its current state to the target values over the given number of frames. |
| `0x1C` | SetWaitScale | 1 | V | Stores its operand in an interpreter local that opcode 0xF1 later reads. |
| `0x1D` | StartParallelBlockA | 0 | V | Starts a task that runs the instructions that follow, and continues the main script at the next 0x1E instruction, skipping the instructions between. |
| `0x1E` | EndParallelBlockA | 0 | V | Does nothing when executed; it is the end marker of the block that opcode 0x1D starts. |
| `0x1F` |  | 5 | V | EventScript_Run first stores a quantized copy of the current angle in a global, then the handler rewrites the next 0x19 instruction: three position words at its operand bytes 0 to 5, built from the two units' node wor... |
| `0x20` |  | 6 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x21` |  | 2 | V | Sets a 32-bit global to the operand, unless that global holds 166 and the operand is not -1; if a second global's high dword is non-zero it sets the first global to 0 instead, again unless it holds 166. |
| `0x22` |  | 3 | V | Stores its three operand bytes into globals (one 16-bit value and the two words of a 32-bit value), then waits one frame. |
| `0x23` | NoOp23 | 3 | V | Does nothing: the interpreter skips over it (it shares an empty case with 0x24). |
| `0x24` | NoOp24 | 0 | V | Does nothing: the interpreter skips over it (it shares an empty case with 0x23). |
| `0x25` |  | 4 | V | Stores its two 16-bit operands into two 16-bit globals. |
| `0x26` |  | 2 | V | For each of the task slots 1 to 16 that is in use, has task kind 2 and whose first parameter equals the operand, changes its task kind to 1. |
| `0x27` | WaitUntilFlagCleared | 0 | V | Sets a global word to 1 and waits frame by frame until that word reads zero, then continues. |
| `0x28` |  | 8 | V | Immediately, SceneCallback_Dispatch mode 1 runs EventBlock_ApplyOperands: when the unit resolves it calls a block helper with the scale, the three unit bytes at +136 to +138, the vector and the constant 1; when the he... |
| `0x29` |  | 2 | V | Calls a helper routine with its 16-bit operand and the value 1, then continues. |
| `0x2A` | StartParallelBlockB | 0 | V | Starts a scene task with the operand block as its data, then continues at the next 0x2B instruction, skipping the instructions between. |
| `0x2B` | EndParallelBlockB | 0 | V | Does nothing when executed; it is the end marker of the block that opcode 0x2A starts. |
| `0x2C` |  | 7 | V | The placement routine of opcode 0x53, run with the flag set to 0: it writes a 7-byte placement record for the second unit, plus one for the first unit that gets the opposite heading. |
| `0x2D` |  | 6 | V | Passes the location of its operand bytes to a helper routine and continues. |
| `0x2E` |  | 8 | V | Loads two scratch values (a 16-bit value and a byte each) from its operands and passes them with a signed count to a helper; when the flag byte is 0 it also copies the scratch values to two globals. |
| `0x2F` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x30` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x31` |  | 5 | V | Passes its five signed operand bytes to a helper routine (operand 5 as the second argument, operands 2 to 4 as the last three). |
| `0x32` |  | 7 | V | Passes the location of its operand bytes to a helper routine and continues. |
| `0x33` |  | 5 | V | Passes its five operand bytes to a helper routine (operand 5 as the second argument) and continues. |
| `0x34` |  | 2 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x35` |  | 4 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x36` |  | 2 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x37` |  | 2 | V | For each of the 6 records of the event-unit table (584 bytes each) whose id field equals the operand, flips a one-bit flag. |
| `0x38` |  | 2 | V | Reads two triples of 16-bit values from the bytes of the instruction that follows it, divides their distance by its operand, and writes the result as a frame count into that following instruction (operand bytes 15 and... |
| `0x39` | WaitUntilNoUnitActive | 0 | V | Waits frame by frame until no unit has its activity flag set. |
| `0x3A` | WaitUntilLoadDone | 0 | V | Waits frame by frame until a pending-load flag clears. |
| `0x3B` | StartUnitMove | 12 | V | Starts a task, tagged type 11, that moves the three position values of the named object from their current values to the three targets over the given number of frame steps, shaped by the curve mode and weight, and con... |
| `0x3C` |  | 2 | V | Stores its operand in a global, waits two frames, then waits until a pending flag clears. |
| `0x3D` | RemoveUnit | 2 | V | Looks up the unit named by its operand; if found, it waits while the unit's activity byte (record offset 168) is nonzero, then unlinks the unit's record from the unit list and, when the unit occupies a preview slot, m... |
| `0x3E` |  | 9 | V | Starts a task that moves three values in a straight line from the start triple to the end triple, two frames per step, passing them with the first operand to a helper at every step; continues without waiting. |
| `0x3F` |  | 4 | V | Sets the low four bits of a byte in an 8-byte-stride per-tile table; the entry is picked from the three signed operand bytes and a width byte. |
| `0x40` |  | 5 | V | Picks an entry of the per-tile table from three signed index bytes, stores operand 4 in one of its byte fields, copies the low bit of operand 3 into a flag bit, and sets the low six bits of its first byte to 0x15 unle... |
| `0x41` | StartCounterTask | 4 | V | Starts a task that never returns by itself: it adds operand 1 to a shared 16-bit counter every operand-2 frames and adds operand 3 once every operand-4 frames; the instruction continues without waiting. |
| `0x42` | StopKind13Task | 0 | V | Waits one frame, then, if a running task of kind 13 other than this one exists, clears its entry pointer and a status word for it; when no such task exists and a global dword is zero, it calls the same helper with no ... |
| `0x43` |  | 1 | V | After a four-frame wait it runs the set-up branch chosen by the mode byte; modes 1 and 6 are skipped while scene variable 508 is nonzero, mode 6 hands its mode on to the mode 15 branch and mode 14 hands on the last sl... |
| `0x44` |  | 2 | V | Resolves the operand to a slot and, if found, runs ScenePreview_ClaimForUnit on it; only while variable 39 equals 396 it also calls a helper on the unit's preview entry and invokes a callback (mode 1) for the slot. |
| `0x45` |  | 3 | V | Finds the preview entry for the id; when it is usable and the unit has no slot, shows it with ScenePreview_ShowEntry using operand 3 and sets the pending flag; when the unit has a slot, runs ScenePreview_ClaimForUnit ... |
| `0x46` |  | 2 | V | Resolves the operand to a slot and, if found, runs SceneUnit_SetFlag156 on it; in event 325 at one script position it does the same for slots 0 to 19, and while a global counter equals 2 it appends an entry to a list. |
| `0x47` | StartEffectInFreeSlot | 8 | V | Takes the first free slot out of 21, records it in the word table at operand 3, starts an effect there with the other operands and sets a pending flag; when all 21 slots are busy the instruction is retried. |
| `0x48` | WaitForEffectPending | 0 | V | Waits one frame at a time until the pending flag set by opcodes 0x45 and 0x47 is clear. |
| `0x49` | StartParallelBlockC | 0 | V | Starts a task that runs the instructions that follow, and continues the main script at the next 0x4A instruction, skipping the instructions between. |
| `0x4A` | EndParallelBlockC | 0 | V | Does nothing when executed; it is the end marker of the block that opcode 0x49 starts. |
| `0x4B` | WaitForNoTaskTag14 | 0 | V | Waits one frame at a time until no task other than the running one has tag 14. |
| `0x4C` |  | 2 | V | Stores the operand in a 16-bit global, waits two frames, then calls a helper that resets a set of globals. |
| `0x4D` |  | 1 | V | Stores the operand in a 16-bit global and waits two frames, except in one specific event where it does not wait. |
| `0x4E` |  | 3 | V | Resolves the operand to a task slot and, if one is found, writes operand 3 into one byte field of that slot's record. |
| `0x4F` |  | 1 | V | Stores the operand in a 16-bit global, waits two frames, then waits until another 16-bit global is zero. |
| `0x50` | ReadBlockToImage | 1 | V | Reads 8192 bytes of game data from sector four times the operand, waits until the read completes, copies one of eight 32-byte presets (or a default value for operands of 8 or more) into a global, copies eight 8-by-48 ... |
| `0x51` | SetKeyedTaskValues | 5 / 7 | V | Finds the live task whose tag is 51 and whose key matches operand 1 among three table entries and, if found, stores the two values in two per-task fields and sets that task's tag to 1; it then waits four frames unless... |
| `0x52` |  | 2 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x53` |  | 7 | V | For each key of a fixed 21-key order that passes the group test against the second reference, writes a 7-byte placement record for the second unit, with a heading computed from the two units' position words so that it... |
| `0x54` |  | 2 | V | Stores its two operand bytes as the two halves of a 32-bit global and sets a companion flag word to 1. |
| `0x55` |  | 2 | V | Stores its two operand bytes as the two halves of a second 32-bit global and sets that global's companion flag word to 1. |
| `0x56` |  | 0 | V | Sets a request flag to 1 and waits one frame at a time until something else clears it. |
| `0x57` |  | 0 | V | Sets a second request flag to 1 and waits one frame at a time until something else clears it. |
| `0x58` | LoadEventSprite | 3 | V | Starts the task that loads an event character's sprite data for one of two display sides. |
| `0x59` |  | 1 | V | Stores its operand in a 32-bit global. |
| `0x5A` |  | 1 | V | Stores its operand in a 32-bit global. |
| `0x5B` |  | 1 | V | Stores its operand in a 32-bit global. |
| `0x5C` |  | 3 | V | Stores operand 3 together with the slot number resolved from the s16 operand (shifted up one byte) in a 32-bit global. |
| `0x5D` |  | 1 | V | Stores its operand in a 32-bit global. |
| `0x5E` |  | 1 | V | Stores its operand in a 16-bit global. |
| `0x5F` |  | 6 | V | Finds the preview-unit entry for the key and writes operands 3 to 6 into its bytes 79 to 81; when the entry has an active slot it also starts an effect there. |
| `0x60` |  | 2 | V | Stores the two operand bytes in a 32-bit global (second one shifted up 16 bits), waits one frame, then sets a flag word to 1 if another global equals 2. |
| `0x61` | NoOp61 | 3 | V | Does nothing; its three operand bytes are skipped without being read. |
| `0x62` |  | 6 | V | Same writes as opcode 0x5F, but the preview-unit entry is picked by index (operand 1) and no effect is started; operand 2 is not read. |
| `0x63` |  | 1 | V | Stores its operand in the 32-bit global that sets the curve mode and weight for the task started by opcode 0x19 (bits 0 and 1 and bits 2 and 3 select curve modes, bits 4 to 7 the weight). |
| `0x64` | WaitEffectSlotIdle | 2 | V | Waits one frame at a time until the effect slot named by the operand is idle, or until all 21 slots are idle when the operand is -1. |
| `0x65` | WaitAllEffectSlotsIdle | 0 | V | Waits one frame at a time until all 21 slots of the effect table are idle (the same wait as opcode 0x64 with -1). |
| `0x66` | CopyBlock512 | 0 | V | Copies a 512-byte block from one global buffer to another. |
| `0x67` |  | 2 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x68` |  | 3 | V | Sets byte 341 of the object belonging to the resolved slot to 2 when operand 3 is 1, otherwise to 0; does nothing when the reference does not resolve. |
| `0x69` |  | 8 | V | For each key of a fixed 21-key order that passes the group test, it writes a 7-byte placement record for the unit then in the reference, with the heading from the cell position (operands 3 and 4) and that unit's posit... |
| `0x6A` | StartChannelStep | 5 | V | Starts a task, tagged type 53, that for the given number of frames refreshes the channel of the keyed object each frame (channel 12 when the key is the current one, and the bound channel from 13 to 19 when one matches... |
| `0x6B` | StartChannelBindStep | 5 | V | Starts a task, tagged type 53, that releases the keyed object, then binds the key to a channel (operand 4 nonzero) or makes it the current key (zero), calls a refresh helper, and then runs the same frame loop as opcod... |
| `0x6C` | ClearObjectFlag04 | 2 | V | Clears bit 0x04 of the byte at offset 143 in the record of each object selected by the operand. |
| `0x6D` | SetObjectFlag04 | 2 | V | Sets bit 0x04 of the byte at offset 143 in the record of each object selected by the operand. |
| `0x6E` | StartObjectMove | 12 | V | Starts a task, tagged type 11 so opcode 0x6F can wait for it, that moves the three position values of the named object to the three targets in a number of frame steps given by the distance divided by operand 11, shape... |
| `0x6F` | WaitForMoveTasks | 2 | V | Waits one frame at a time until no running task is tagged type 11 for the resolved object (the tasks started by opcode 0x6E). |
| `0x70` |  | 4 | V | Resolves operand 1 to a slot and, if found, negates and adds back the three position words of its unit node so they become zero, then runs SceneUnit_ResetFields on that same unit with operands 3 and 4 (a preview byte ... |
| `0x71` | MoveUnitEntryToFront | 2 | V | Resolves the unit id in operand 1 to a slot and, if found, moves that unit's entry to the front of the object list; it continues without waiting. |
| `0x72` |  | 0 | V | Waits one frame, then sets a 16-bit global flag to 1. |
| `0x73` | WriteAdjustedWords | 14 | V | Adds a fixed adjustment from a table to each of its seven 16-bit operand words (the first three adjustments are divided by 1024, and the value 10000 is left unchanged), then writes the seven results into the script by... |
| `0x74` | NoOp74 | 6 | V | Does nothing; its operand bytes are skipped (shares its body with opcode 0x75). |
| `0x75` | NoOp75 | 6 | V | Does nothing; its operand bytes are skipped (shares its body with opcode 0x74). |
| `0x76` |  | 6 | V | Starts a task that tags itself as type 54 and calls two helpers, and continues without waiting; the task does not read the operand bytes. |
| `0x77` |  | 0 | V | Copies one 32-bit global into another when the source is nonzero, then sets the state of the task tagged 55 (if one exists) to 54. |
| `0x78` |  | 2 | V | Starts a task with operand 1 as its mode and operand 2 as its argument (task slot 2 is used instead when slot 4 was chosen and the mode is 7); continues without waiting. |
| `0x79` |  | 4 | V | When the id resolves to an index, stores operand 3 in one 16-bit table at that index and clears the same index in a second 16-bit table. |
| `0x7A` |  | 2 | V | While variable 508 reads 0, finds the first live unit-save entry whose first byte equals the operand, adds one (capped at 99) to a counter for each valid id in its seven item bytes, and marks the entry empty. |
| `0x7B` | WaitForInputMask | 2 | V | Waits one frame at a time until the global input word overlaps the operand mask (widened as described), or until a 16-bit global or a flag pair ends the wait, and sets a global flag to 1 when the operand equals the bi... |
| `0x7C` | ResetObjectChannels | 0 | V | Clears the current key and sets the entries of channels 10, 12 and 13 to 19 of one global object to the released state (freeing an attached resource where present), then resets the channel binding table; it continues ... |
| `0x7D` | ShowPanelRow | 1 | V | Starts a task tagged 61 that waits for shared sequencer slot 12, sets a panel flag, then acts on the table row numbered by the operand (kind 0 runs the title panel, kind 1 runs a queued wait, other kinds do nothing), ... |
| `0x7E` | WaitUntilVarAtLeast | 4 | V | Waits one frame at a time until the variable named by operand 1 reads at least operand 3, or until a stop flag ends the wait; variable 87 has its own special handling. |
| `0x7F` |  | 4 | V | Resolves the id to a slot; if found, stores a value built from the two operand bytes (operand 4 plus 100 times operand 3 plus one) in a per-slot table and refreshes the slot's object through helpers. |
| `0x80` |  | 3 | V | For each slot matched by the id, runs a helper on the slot's object and then waits the number of frames in operand 3. |
| `0x81` | SetObjectFlag02 | 3 | V | For each slot matched by the id, sets or clears bit 0x02 of a flag byte in the slot's object according to operand 3. |
| `0x82` |  | 0 | V | While variable 508 reads 0, sets a 16-bit global to 2, runs a helper, waits one frame and runs three more helpers; otherwise does nothing. |
| `0x83` | AddToClampedField | 5 | V | For each matched entry, adds the signed amount to the selected field and clamps the result to that field's allowed range. |
| `0x84` |  | 1 | V | When the operand is non-zero, starts music track number operand plus 44 on channel 9 of the sound object: it looks up the track plus 1 as a hash key; on a hit it hands the cached entry to a replay helper, and on a mis... |
| `0x85` | StoreVarBitsToTable | 1 | V | While variable 508 reads 0 and the operand is nonzero, copies bits 0 to 4 of variable 47 and bits 0 to 3 of variable 46 into the nine-bit slot for group n of a global bit table. |
| `0x86` |  | 3 | V | Resolves the id to an object and, if found, stores operand 3 in a word at offset 336 of it together with a derived class byte at offset 338. |
| `0x87` |  | 4 | V | If both references resolve, it installs SceneUnit_MeasureRange as the global callback and calls SceneCallback_Dispatch mode 3 with the second unit's preview index, the address of a fixed tile point and the first unit'... |
| `0x88` | RestoreSavedTableBytes | 0 | V | Restores the first byte of each of 32 twenty-byte records in a global table from a 32-byte backup array. |
| `0x89` | SaveAndClearTableBytes | 0 | V | Copies the first byte of each of 32 twenty-byte records in a global table into a 32-byte backup array, then zeroes those table bytes. |
| `0x8A` | WaitForDataLoad | 0 | V | Repeats a frame wait followed by a mode 1 callback dispatch, which calls MultiStr_Includes, and stops when MultiStr_Includes returns zero; MultiStr_Includes returns EventDataLoad_Poll's busy result. |
| `0x8B` |  | 0 | V | Sets a global flag to 1 and starts a task that waits frame by frame until another global becomes zero and then ends; continues without waiting. |
| `0x8C` |  | 6 | V | Resolves operand 1 and, unless the result is negative as a 16-bit value, updates bit 0x01 of the found object's byte +143, writes the 7-byte row for slots 0 to 20 with operand 3 as byte 0 and zero in bytes 4 and 6, an... |
| `0x8D` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x8E` |  | 0 | V | Waits two frames, then waits one frame at a time while a scene task tagged 61 exists and its result field is still zero. |
| `0x8F` |  | 1 | V | Stores its operand in a 32-bit global. |
| `0x90` |  | 3 | V | Waits one frame at a time until the two globals equal operands 1 and 2 and a button test passes (one button pressed, four others not), or until a stop flag is set; operand 3 is not read. |
| `0x91` |  | 3 | V | Waits for shared sequencer slot 13, loads the map-title texture chosen by scene variable 51, then starts a task that runs three sweeps of the 0-to-255 value over frames (up, hold at 255, sweep again with the second la... |
| `0x92` |  | 5 | V | Starts a task that resolves the unit id and, when it resolves, applies a mode-dependent update to the unit's preview row and status bits, runs the unit-end callback EventUnitStatus_RefreshNode (modes 1 to 4 and up and... |
| `0x93` | SetVar84 | 2 | V | While variable 508 reads 0, writes the operand into variable 84. |
| `0x94` |  | 2 | V | Resolves operand 1 and, unless the result is 2000, runs a callback and a helper call, then waits 10 frames, calls SceneUnit_ResetAndQueue4 with +31, waits 50 frames, calls it with -31, waits 60 frames, and clears two ... |
| `0x95` | NoOp95 | 0 | V | Does nothing. |
| `0x96` |  | 0 | V | Sets a global wait flag, waits one frame at a time until something else clears it, then waits 60 more frames. |
| `0x97` |  | 2 | V | Resolves the id to an object and, if found, runs SceneUnit_RunPlacement on its record with the arguments 0 and 1; continues without waiting. |
| `0x98` |  | 2 | V | Resolves the operand to a slot and, if found, installs a global callback and invokes it once (mode 1) for that slot. |
| `0x99` |  | 2 | V | For each of the 21 slots whose unit id equals the operand and whose unit record has flag bits 0x30 set and state not -2, calls a helper on the slot. |
| `0x9A` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x9B` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x9C` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x9D` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x9E` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0x9F` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xA0` | CompareVarsLessOrEqual | 0 | V | Sets variable 0 to 1 if variable 0 is less than or equal to variable 1 (signed 32-bit comparison), otherwise to 0. |
| `0xA1` | CompareVarsGreaterOrEqual | 0 | V | Sets variable 0 to 1 if variable 0 is greater than or equal to variable 1 (signed 32-bit comparison), otherwise to 0. |
| `0xA2` | CompareVarsEqual | 0 | V | Sets variable 0 to 1 if variable 0 equals variable 1, otherwise to 0. |
| `0xA3` | CompareVarsNotEqual | 0 | V | Sets variable 0 to 1 if variable 0 differs from variable 1, otherwise to 0. |
| `0xA4` | CompareVarsLess | 0 | V | Sets variable 0 to 1 if variable 0 is less than variable 1 (signed 32-bit comparison), otherwise to 0. |
| `0xA5` | CompareVarsGreater | 0 | V | Sets variable 0 to 1 if variable 0 is greater than variable 1 (signed 32-bit comparison), otherwise to 0. |
| `0xA6` |  | 4 | V | Looks up the id in table 280; if that row is valid it uses the row's dword at +8 as a key into table 279; if that row is valid as well, it creates a 56-byte sound resource that carries the id at +32, calls a helper ro... |
| `0xA7` | SetEntryStateById | 4 | V | Sets the state byte to 4 for every entry in the global object's entry list whose id equals the operand, passing each matching entry's resource pointer to a helper first when one is held. |
| `0xA8` |  | 6 | V | If the unit exists, stores the low byte of the operand in the unit's byte +343, then calls SceneUnit_BuildPalette, which builds 16 packed 15-bit palette words from the table 302 row for that byte and passes them with ... |
| `0xA9` |  | 6 | V | If the unit exists, stores the low byte of the operand in the unit's byte +345, clears bit 0x40 of the unit's byte +300, and sets that bit to bit 0 of byte +8 of the table 305 row for that key when the row exists. |
| `0xAA` |  | 1 | V | Sets a one-byte flag of a global object to 1 when the operand is nonzero, otherwise to 0. |
| `0xAB` |  | 4 | V | Only when the enhanced-edition flag is 1, starts a task and stores the operand in its record; otherwise does nothing. |
| `0xAC` | RunSubquestPanel | 4 | V | Creates a sub-quest UI panel object holding the operand, waits until input key 0x15, 0x1A or 0x1B is active, then releases the panel, waits for its hide state to end, and resets the interface flags it set on entry. |
| `0xAD` | CharaRenderLoadTargetA | 8 | V | Loads the table-284 record for the first operand into the target fields of the first renderer sub-block, copies that block's first 32 bytes over the following 32 bytes, clears one dword, and stores the second operand ... |
| `0xAE` | CharaRenderLoadTargetB | 8 | V | Loads the table-285 record for the first operand into the target fields of the second renderer sub-block, copies that block's first 12 bytes over the following 12 bytes, clears one dword, and stores the second operand... |
| `0xAF` | EventStateSetKey | 4 | V | Stores the operand as the current key of the event-state object and, when the key changes, sets a flag on that object to 1 if any table-33 entry for the key has the value 91 in one of two fields, otherwise 0. |
| `0xB0` | VarAdd | 4 | V | Adds a literal to a variable. |
| `0xB1` | VarAddVar | 4 | V | Adds another variable to a variable. |
| `0xB2` | VarSub | 4 | V | Subtracts a literal from a variable. |
| `0xB3` | VarSubVar | 4 | V | Subtracts another variable from a variable. |
| `0xB4` | VarMul | 4 | V | Multiplies a variable by a literal. |
| `0xB5` | VarMulVar | 4 | V | Multiplies a variable by another variable. |
| `0xB6` | VarDiv | 4 | V | Divides a variable by a literal; division by zero ends the task. |
| `0xB7` | VarDivVar | 4 | V | Divides a variable by another variable; division by zero ends the task. |
| `0xB8` | VarMod | 4 | V | Sets a variable to its remainder modulo a literal. |
| `0xB9` | VarModVar | 4 | V | Sets a variable to its remainder modulo another variable. |
| `0xBA` | VarAnd | 4 | V | Bitwise AND of a variable with a literal. |
| `0xBB` | VarAndVar | 4 | V | Bitwise AND of a variable with another variable. |
| `0xBC` | VarOr | 4 | V | Bitwise OR of a variable with a literal. |
| `0xBD` | VarOrVar | 4 | V | Bitwise OR of a variable with another variable. |
| `0xBE` | VarZero | 2 | V | Sets a variable to zero; for variable 87 it also clears a field of a global record. |
| `0xBF` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xC0` | NoOp16Bytes | 16 | V | Does nothing; its operand bytes are skipped. |
| `0xC1` |  | 0 | V | When the dword at a global is zero, sets the high dword of a global to 2, processes flagged preview-unit slots, waits for frames while a UI routine reports busy when any record was flagged, and does not clear that hig... |
| `0xC2` |  | 4 | V | Only when the enhanced-edition flag is 1, starts a task and stores the operand in its record; otherwise does nothing. |
| `0xC3` |  | 2 | V | Passes the 16-bit operand to EventPreviewUnit_StageSlot, which resolves it to a preview slot and, when it resolves, copies the 512-byte slot into a staging buffer and sets a staged flag; in event 281 a reference of 25... |
| `0xC4` |  | 12 | V | Copies the 4-byte field at offset 4 of the table-226 record named by the third operand into a UI node, clears another node field, looks up the table-224 entry named by the first two operands for that node, and plays t... |
| `0xC5` | CharaRenderLoadRecordTimed | 8 | V | When the first operand is nonzero, loads the table-227 record for it into the renderer block and stores the second operand as a float time value in that block. |
| `0xC6` | CharaRenderSetSlotTimed | 8 | V | Stores the resolver's result as a 16-bit slot value in the renderer block, sets a changed flag when it differs from the previous slot, sets a flag byte to 1, stores the second operand as a float time value, and copies... |
| `0xC7` |  | 16 | V | Writes its four operand values into the character renderer's state block (three floats and a duration in seconds) and sets a fixed flag dword there. |
| `0xC8` |  | 8 | V | Sets the first 8 bytes of the indexed record to 1 and stores operand 2 in the dword after them. |
| `0xC9` | SetUiByte185 | 1 | V | Stores the operand in the byte at offset 185 of a global UI object. |
| `0xCA` | SetUiFlagOnLanguageMatch | 1 | V | When the enhanced-edition flag is 1 and the mask matches the current language, sets byte 184 of a UI object to 1. |
| `0xCB` |  | 8 | V | When operand 1 is nonzero, loads that id's table 256 entry into a sub-object of the unit sprite renderer with EventCharaSprite_SetTable256Entry, and sets the change time to operand 2 divided by 60 seconds (0.5 seconds... |
| `0xCC` |  | 12 | V | When operand 2 is zero, sets the first dword of the indexed 20-byte record to 1; otherwise sets bit 0 of the indexed 36-byte entry and calls a helper that fills the record. |
| `0xCD` |  | 8 | V | Rewrites the indexed record: copies a dword into it from a companion table, sets its state to 1 or 2 and clears its two 16-byte blocks and a trailing dword. |
| `0xCE` | SetUiFlag45 | 1 | V | Sets the byte at offset 45 of a global object to 1 when the operand is nonzero, otherwise to 0. |
| `0xCF` | ReleasePendingPair | 0 | V | Passes each nonzero value of a global pending pair to a routine that removes that id from its tables, then zeroes both values and a further pending dword. |
| `0xD0` | JumpForwardIfVar0Zero | 1 | V | Conditional jump: when variable 0 is zero, scans forward from the next instruction for the first 0xD2 or 0xD4 instruction whose key byte equals the operand and continues after it; otherwise does nothing. |
| `0xD1` | JumpForwardToMarker | 1 | V | Jump forward: continues after the first later 0xD2 instruction with the same key; if none is found before an end instruction (0xDB), the script ends. |
| `0xD2` | JumpTargetForward | 1 | V | Does nothing when executed; it is the target marker for the forward jumps of opcodes 0xD0 and 0xD1. |
| `0xD3` | JumpBackToMarker | 1 | V | Jump backward: continues after the nearest earlier 0xD5 instruction with the same key; if none is found the script ends. |
| `0xD4` | JumpTargetForwardAlt | 1 | V | Does nothing when executed; it is an alternative target marker for the forward jump of opcode 0xD0. |
| `0xD5` | JumpTargetBackward | 1 | V | Does nothing when executed; it is the target marker for the backward jump of opcode 0xD3. |
| `0xD6` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xD7` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xD8` | NoOpD8 | 1 | V | Does nothing; the operand byte is skipped. |
| `0xD9` | JumpBackStopMarker | 1 | V | Does nothing when executed; the backward jump of opcode 0xD3 stops at it whatever the key. |
| `0xDA` | NoOpDA | 0 | V | Does nothing. |
| `0xDB` | End | 0 | V | The end-of-script opcode: it waits for the pending-work word, for the scene tasks tagged 8 and for a loader dword to clear, does the end-of-script clean-up, and then either ends the running task (when one of the end c... |
| `0xDC` |  | 0 | V | Sets a 16-bit global to 13. |
| `0xDD` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xDE` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xDF` |  | 0 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xE0` | NoOpE0 | 2 | V | Does nothing; its operand bytes are skipped. |
| `0xE1` |  | 1 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xE2` |  | 1 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xE3` |  | 0 | V | Same body as opcode 0xDB: it waits for the pending-work word, for the scene tasks tagged 8 and for a loader dword to clear, does the end-of-script clean-up, and then either ends the running task (when one of the end c... |
| `0xE4` |  | 1 | V | No handler: the interpreter steps over the instruction by its length and then ends the script run. |
| `0xE5` | WaitForTaskKey | 2 | V | While the mode dword is zero, waits one frame at a time until one of the 16 task slots is running with a key equal to the operand; when the mode dword is 1 it continues without waiting. |
| `0xE6` |  | variable | V | No handler: the interpreter steps over the instruction by its variable length and then ends the script run. |
| `0xE7` |  | 4 | V | Looks up the 4-byte id in table 87 and, when the panel at offset 80 of the global UI object exists, sets its text lines from table 86 (type code 115, one line) or table 85 (type code 113, one or two lines) and plays t... |
| `0xE8` | SetUiByte174OnLanguage | 1 | V | Only when the enhanced-edition flag is 1 and a check of the operand against the current language succeeds, sets the byte at offset 174 of a global UI object to 1. |
| `0xE9` | SetSettingDword | 8 | V | Stores operand 2 in the dword slot given by operand 1 of a global settings object, then notifies registered observers. |
| `0xEA` | SetSettingBool | 5 | V | Stores a boolean (operand 2 equals 1) in the byte slot given by operand 1 of the same settings object, then notifies registered observers. |
| `0xEB` | SetKeyedTaskValuesWide | 6 / 10 | V | Looks for one of three table entries whose key equals operand 1 and whose task slot is active with tag 51; if found, stores the two values in that slot and sets its state to 1. |
| `0xEC` |  | 0 | V | Unless the low dword of a global state word equals 1, starts a UI task that plays a language-keyed UI state and waits for it to finish, and sets the low dword of another global to 1. |
| `0xED` |  | 6 | V | Stores the negated 16-bit operand in a field of a global object and calls a helper with the 4-byte operand, which waits several frames. |
| `0xEE` | SetUiDataPointer | 4 | V | Looks up the id in a table and stores a pointer to the found data at offset 176 of a global UI object. |
| `0xEF` |  | 0 | V | Sets the byte at offset 33 of a global object to 0. |
| `0xF0` | WaitOneFrame | 0 | V | Waits one frame. |
| `0xF1` | WaitFrames | 2 | V | Waits for the given number of frames, multiplied by the scale set by opcode 0x1C when that scale is above 1; with a scale of 1 or less only frames in which a flag condition holds are counted. |
