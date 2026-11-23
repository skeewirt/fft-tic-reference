# UIAgentBase

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The common front of every UI agent (64 bytes), built by sub_1401D14F4 (0x1401D14F4): the vtable, the UI module's allocator and the vector of attached add-ons. Each derived constructor calls it first, replaces the vtable and adds its own fields from +0x40.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="vtable"></a>`0x0` | vtable | `void *` | V | Base vtable 0x140713238; every derived constructor overwrites it with its own. |  |  |
| <a id="allocator"></a>`0x8` | allocator | `void *` | V | The UI module's allocator (`qword_143CDAA80`+0x20), or 0 when the module is absent. The base destructor frees the add-on vector through it. |  |  |
| <a id="addons_begin"></a>`0x10` | addons_begin | `UIAddon **` | V | First attached add-on; `UIAgent_IsActive` compares it with +0x18. | [UIAgent_DetachAddon](../functions/UIAgent_DetachAddon.md), [UIAgent_IsActive](../functions/UIAgent_IsActive.md) |  |
| <a id="addons_end"></a>`0x18` | addons_end | `UIAddon **` | V | One past the last attached add-on; `UIAgent_AttachAddon` grows it by 8 and `UIAgent_DetachAddon` shrinks it by 8. | [UIAgent_AttachAddon](../functions/UIAgent_AttachAddon.md), [UIAgent_DetachAddon](../functions/UIAgent_DetachAddon.md), [UIAgent_IsActive](../functions/UIAgent_IsActive.md) | [UIAgent_AttachAddon](../functions/UIAgent_AttachAddon.md), [UIAgent_DetachAddon](../functions/UIAgent_DetachAddon.md) |
| <a id="addons_capacity"></a>`0x20` | addons_capacity | `UIAddon **` | V | End of the vector's storage; the add-on push helper compares it with the end and reallocates when they meet. | [UIAgent_AttachAddon](../functions/UIAgent_AttachAddon.md) |  |
| <a id="unknown28"></a>`0x28` | unknown28 | `uint64_t` | ? | Zeroed by the base constructor; its use was not established in this pass. |  |  |
| <a id="unknown30"></a>`0x30` | unknown30 | `uint64_t` | ? | Zeroed by the base constructor; its use was not established in this pass. |  |  |
| <a id="unknown38"></a>`0x38` | unknown38 | `uint64_t` | ? | Zeroed by the base constructor; its use was not established in this pass. |  |  |

## Behavior

- V: `sub_1401D14F4` writes the vtable, copies the allocator from the UI module and zeroes +0x10..+0x20 (the add-on vector) plus +0x28..+0x3F (three qwords); it stops at +0x40, so every derived agent's own fields begin at +0x40.
- V: `UIAgent_AttachAddon` sets add-on +0x10 = agent and appends the add-on to this vector; `UIAgent_DetachAddon` removes the entry and decrements +0x18.
- V: `UIAgent_IsActive` (vtable slot 2) is exactly begin != end. Base slots 3-5 are further add-on predicates: any add-on's byte +0x28 is set, all add-ons' byte +0x29 are set (after slot 2 passes), and any add-on's +0x18 pointer leads to a byte +0x4A that is set.
- V: the base destructor `sub_1401D156C` frees the vector storage through the allocator at +8 and clears +0x10, +0x18 and +0x20.
- V: the state machine is not part of the base. Generic agents such as Fade, Cursor and SoundVisualizer have no such block; UIAgentFFTOSystem builds a 32-byte one at +0x48 (owner +0, handler +8, selector +0x10, state +0x18) and UIAgentFFTOSaveLoad builds two, at +0x48 and +0x68. `UIAgent_SetState` operates on such a block.
- I: the qwords at +0x28, +0x30 and +0x38 are unused by this build's agents (rests on the constructors and base virtuals read: nothing writes them after the base constructor).

## Notes

Constructor 0x1401D14F4 (67 bytes); destructor body 0x1401D156C; base vtable 0x140713238; slot 1 (per-frame update) is pure in the base and every derived agent supplies it. In the System agent, +72 is the state block's owner pointer and the state id is +96 (+0x60). `UIAgentCursor` and `UIAgentFFTOTitle` keep their own state fields. The add-ons are a vector at +0x10 (begin), +0x18 (end) and +0x20 (capacity); agent +8 is its allocator, not a list.

## Open questions

What +0x28, +0x30 and +0x38 are for, and which agents beyond UIAgentFFTOSystem and UIAgentFFTOSaveLoad embed a state block.
