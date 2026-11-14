# GUIComponent_LoadProps

- **Address:** `0x1403F4EC8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIComponent_LoadProps(__int64 a1, int *file, __int64 a3, GUIComponent *comp)`
- **Callers:** GUIComponent_LoadDef
- **Callees:** GUINode_SetSize, UIName_Assign, UIName_SetKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads a component's property block from the UIB file into the runtime component: the enable byte and values of every effect group (colour transform, offsets, single float, drop shadow, glow, opacity, clip, mask).

## Behavior

- V: the property block v5 = the component record in the file plus the dword stored at record+12 (file + file[3]). Every 'props' offset below is a byte offset into that block; every 'comp' offset is a runtime offset in the component.
- V: enable bytes: comp+60 <- props byte 20, +88 <- 40, +96 <- 68, +120 <- 76, +172 <- 100, +186 <- 176, +192 <- 196, +216 <- 120, +244 <- 144.
- V: colour transform group (enable comp+60): comp+28 / +32 / +36 <- props dwords 7 / 8 / 9 divided by 100.0, comp+40 <- 1.0f, comp+44 / +48 / +52 <- props bytes 21 / 22 / 23 divided by 255.0, comp+56 <- 0.
- V: offsets group (enable comp+88): comp+64..+84 <- props dwords 11..16 (six floats copied raw). Single-float group (enable comp+96): comp+92 <- props dword 18.
- V: drop-shadow group (enable comp+120 <- props byte 76): comp+100 <- props float 20 (offset 80, blur radius), comp+104 <- props dword 21 (offset 84, strength), comp+108 <- props dword 22 (offset 88, offset x), comp+112 <- props dword 23 (offset 92, offset y), comp+116 <- colour: word at props 96 and byte at props 98 in the low three bytes, the top (alpha) byte forced to 0xFF.
- V: glow group (enable comp+172 <- props byte 100): comp+156 <- props dword 27 (offset 108), comp+160 <- props dword 28 (offset 112), comp+164 <- colour: word at props 116 and byte at props 118, alpha byte forced to 0xFF (only bytes 116..118 are read), comp+168 <- mode from props dword 26 (offset 104): 0 -> 0, 1 -> 1, 2 -> 2, any other value leaves comp+168 unchanged.
- V: comp+186 (enable <- props byte 176) group: comp+184 <- props byte 180, comp+185 <- props byte 184, comp+176 <- props float 47 (offset 188) * 0.01, comp+180 <- props dword 48 (offset 192). Opacity-like group: comp+192 (enable <- props byte 196), comp+188 <- props dword 50 (offset 200).
- V (file data, ffto_job_tree.uib, UnitSelect component props at file 0x844): byte 100 = 1 is the only effect enable set; dword 27 = 6.0, dword 28 = 0.8, colour bytes = (255, 239, 179).
- I: the drop-shadow group is the one the later stages forward as the +177 layer group (ComponentEffects_Collect: comp+120 -> context +136; GUILayer_BuildRecord: -> record+153 = layer+177); the glow group is forwarded as +178 (context +156 -> record+154 = layer+178). The field meanings (radius, strength, offset, colour) are read from the consumers, not from names in the file.

## State touched

- Calls: [GUINode_SetSize](GUINode_SetSize.md), [UIName_Assign](UIName_Assign.md), [UIName_SetKey](UIName_SetKey.md)

## Referenced by

- Called by: [GUIComponent_LoadDef](GUIComponent_LoadDef.md)

## Notes

Both colours (shadow comp+116, glow comp+164) are read as three bytes with the alpha byte forced to 0xFF. Copy sibling: sub_1403DF454 (proposed name GUIComponentProps_Copy) copies the same fields from one component to another.

## Open questions

? which shipped UIB components set the shadow enable (props byte 76) and with which values; only the Job Tree UnitSelect glow was read from file data. ? the clip margins comp+196..+211 are copied from a local filled earlier in the function and were not traced. ? what modes 1 and 2 of comp+168 do (the glow consumer takes mode 3 for the Job Tree).
