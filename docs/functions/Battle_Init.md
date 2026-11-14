# Battle_Init

- **Address:** `0x14020EF10`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 sub_14020EF10(void)`
- **Callers:** `sub_140210AF0` (battle scene update/start)
- **Callees:** `sub_1401E9B1C`, `sub_1401E9E10`, `sub_1401F92A8`, `sub_1401EE21C`, `sub_1401EE518`, `sub_1401EBB48`, `sub_1401EB468`, `sub_140101370`, `sub_1402089FC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates and resets the battle singletons when a battle starts: BattleControl, post-battle calculator, a 3008-byte battle object, the map-view camera manager, markers and the command menu.

## Behavior

- V: if `qword_143CD9EF0` (BattleControl) is null, allocates 693712 (0xA95D0) bytes, zeroes it, calls `sub_1401E9B1C` and `sub_1401E9E10`, and stores the pointer at 0x143CD9EF0.
- V: if `qword_143CDA750` is null, allocates 3400 bytes, sets vtable `PostBattleCalc_140713F28`, zeroes 106 4-qword records, stores at 0x143CDA750 and calls `sub_1401F92A8`.
- V: if `qword_143CDA740` is null, allocates 3008 bytes and initializes it with `sub_1401EE21C`; sets `+1172=1`, `+1176=1`, byte `+1892 = byte_140C757AA`, `+1928 = dword_140D40548`, word `+1893=257`, `+1932=90`, then `sub_1401EE518`.
- V: if `qword_143CDA758` is null, allocates 304 bytes, sets vtable `MapViewCameraManager_140713F38`, and writes its defaults: `+8=5, +12=1, +16=8, +20=1, +24=20, +28=20, +32=3840, +96/+88/+100/+104=0, +36=0, +40..+80=0, +112=0`, word `+288=1280`, `+292/+296=1`.
- V: resets `word_1408081E2 = word_140808782 = 170`, `dword_142FEC534 = 1`, `word_142FEF6CC = 0`, `dword_140D4058C/90 = 0`; calls `sub_1401EBB48(qword_143CDA080)` (EnhancedMarkingUtility) and zeroes 0x51E0 bytes at `qword_143CDA388+8`.
- V: fills the turn list with 0xFF (36 bytes at 0x140D40490 in 4-byte steps), calls `sub_1402089FC`, sets `byte_140D40906 = 10`, `dword_1407DC2BC = 1`, sets BattleControl `+693388 = -1`, `+693395 = 0`, zeroes 21 52-byte state records at `+691969`, zeroes 0xA0 bytes at `+693504`, calls `sub_1401EB468`.
- V: clears the 16-bit field at offset 689110 of BattleControl, then **resets the command menu** by calling the menu-windows reset (`sub_140101370`) on the battle menu agent, which is the ninth entry (offset 64) of the UI agent manager's agent vector (`qword_143CD9DA8`, vector at +16).
- V: sets `g_CharaRenderMgr + 13502 = 0`, zeroes `xmmword_140D4057C`, `qword_140D40570`, `dword_140D40578/98/A4`.

## State touched

- Calls: [sub_1401F92A8](sub_1401F92A8.md)
- Writes: [g_PostBattleCalc](../globals/g_PostBattleCalc.md)

## Referenced by

- Called by: [sub_140210AF0](sub_140210AF0.md)

## Notes

This is the best single breakpoint for "a battle just started": it runs once per battle, right before the command menu agent is reset. Field meanings of the camera manager defaults are `?`.

## Open questions

? what the 3008-byte object at 0x143CDA740 is; ? the meaning of camera fields +8..+32.
