# Save_BootClear

- **Address:** `0x1402D3FA0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void Save_BootClear(void)`
- **Callers:** sub_1402D4A2C
- **Callees:** memset, sub_140245A88, sub_140245C84, sub_14037ABBC, sub_140245D44, sub_14039D828, EventThread_Yield, CardSlot_IsValid, sub_14021849C, SceneTask_Start, sub_1402F7F4C, sub_1402D3918, Status_BuildFlagMasks, sub_14033FB84, sub_14031EF70, sub_140273D78, sub_1402B2004, sub_14025F7C0, sub_1402B1CD0, sub_140283E24, sub_1402B2124, sub_140283F64, sub_1401D6F9C, sub_1400EC678, sub_1400ECC5C, sub_14013EA54, sub_14013EE4C, sub_14037ADB8, sub_140257354, EventVar_Write, sub_1402F41D0, GameData_ReadSectors, sub_14033D6B0, sub_140246078, sub_140210AF0, sub_1402B20C0, SceneVar_Write, sub_1402BA744, sub_14024599C, sub_1402D38EC, sub_1402BAB04, sub_1400E43B4, sub_1401DDEC4, sub_1401E2D64, sub_1401E3744, sub_14039DCE8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The boot-time save clear: it fills the save cache and the auto slot with the empty pattern, resets the save manager and the auto-slot header, and starts the reload state machine.

## Behavior

- V: the slot cache at 0x142C8B970 is filled with 0xFF over 0x1EA488 bytes, and the 0x9CE4-byte auto-slot image at 0x142E75DF8 with 0xFF as well (the fill byte is edx = -1).
- V: the dword at 0x142E7FADC is cleared at entry, and a computed word is written to 0x1408FBC5C later in the body.
- V: CardSlot_IsValid is used to reject an absent card before the clear, and the save-manager state is reset through sub_140245A88.
- V: EventVar_Write and SceneVar_Write clear the story and scene variables the save path owns.
- V: Status_BuildFlagMasks and the item-state builders are called so the live state matches a new game.
- V: the clear-and-reload state machine is started with sub_140245C84 and the auto-slot header is imported with sub_14021849C.
- V: the single caller is the boot sequence, so this runs before any slot is read.
- I: the 0x1EA488 cache size is the flat image of the 50 manual slots, which is why the whole image is cleared at once.
- ?: whether a card-present boot with an absent file takes the same clear path; the condition was not decoded.

## State touched

- Calls: [sub_140245C84](sub_140245C84.md), [EventThread_Yield](EventThread_Yield.md), [CardSlot_IsValid](CardSlot_IsValid.md), [sub_14021849C](sub_14021849C.md), [SceneTask_Start](SceneTask_Start.md), [sub_14033FB84](sub_14033FB84.md), [sub_14031EF70](sub_14031EF70.md), [sub_140257354](sub_140257354.md), [EventVar_Write](EventVar_Write.md), [GameData_ReadSectors](GameData_ReadSectors.md), [sub_140210AF0](sub_140210AF0.md), [SceneVar_Write](SceneVar_Write.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Notes

Whole function read (2697 bytes).

## Open questions

None recorded.
