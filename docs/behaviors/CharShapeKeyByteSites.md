# CharShapeKeyByteSites

- **Kind:** observed behaviour
- **Scope:** engine (CharShape key)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [CharShape_ApplyClut](../functions/CharShape_ApplyClut.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [sub_14026E838](../functions/sub_14026E838.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

CharShape_ApplyClut takes its key as a byte: the callee's zero-extending byte load of the key at 0x14026C7C0, the menu caller's byte move of the look at 0x14026E806 and the battle copy loop's byte mask at 0x14026E8D0.

## Behavior

- V: the callee's zero-extending byte load of the key is at 0x14026C7C0; the menu caller's byte move of the look is at 0x14026E806; the battle copy loop's byte mask is at 0x14026E8D0.
- M (unicorn, pristine exe, every sprite byte 0..255): stock battle cx = 0x100 | S.

## Open questions

None recorded.
