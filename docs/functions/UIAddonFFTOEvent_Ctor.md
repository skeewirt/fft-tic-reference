# UIAddonFFTOEvent_Ctor

- **Address:** `0x140135A00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 sub_140135A00(UIAgentFFTOEvent *agent, ...)`
- **Callers:** UIAgentFFTOEvent construction path (vtable/registration)
- **Callees:** Mem_Alloc, `sub_1401372F0`, `sub_1401D16C4`, `sub_1401D1A00`, `sub_1401D1970`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the four addons owned by the event UI agent, including the pause overlay.

## Behavior

- V: allocates 2280 bytes and initializes the event main addon (registered as addon type 25).
- V: allocates 48 bytes, sets vtable `vftable_ffto::Game::UI::UIAddonFFTOPause_140710FE8`, registers it as type **37** (`a1[9]`).
- V: allocates 80 bytes for `UIAddonFFTOEventCaption` (vtable `0x140711118`, type 38).
- V: allocates 96 bytes for `UIAddonFFTOChapter` (vtable `0x140711080`, type 27, initial dword +84 = 1068121457 and byte +88 = 0).
- V: all four are attached with `sub_1401D16C4(agent, addon)` and typed with `sub_1401D1A00(addon, type)`.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md)

## Notes

The pause addon is only a 48-byte base object; its behaviour is in the `ffto_pause.uib` widget states. A UI addon setup `sub_140134EC8` (the setup half of the pair whose constructor `sub_140134E50` allocates a 1032-byte type-257 addon) pushes pause id 9 through the PauseManager when its fifth argument is non-zero; the NXD 282 row 9 then supplies the overlay duration and states (I: the 3.5 s hold measured by the owner is that row's duration). Which screen calls that pair is `?`.

## Open questions

? the NXD 282 row 9 contents (duration, control bytes, UI value); ? which state the ring fill plays.
