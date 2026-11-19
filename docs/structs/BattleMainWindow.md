# BattleMainWindow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle main window object (UIAddonFFTOBattleMain4): only the fields read so far.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="icon_random_node"></a>`0xF8` | icon_random_node | `pointer` | V | The node 'IconRandom': plays 'Show' after the damage number when the random-icon flag is set. |
| <a id="state_key_hide"></a>`0xE0B8` | state_key_hide | `pointer` | V | State-name key 'Hide' (+57528); 'HideAT' is at +57544. |
| <a id="state_key_show"></a>`0xE388` | state_key_show | `pointer` | V | State-name key 'Show' (+58248); 'ShowAT' is at +58264. |
| <a id="action_word"></a>`0xE59C` | action_word | `uint16` | V | The action word shown: kind bits 0xF800 (0x7000 ability, 0xB000 weapon attack). |
| <a id="hand_items"></a>`0x102CC` | hand_items | `uint16[2]` | V | The two item ids of the weapon attack shown. |
| <a id="random_icon"></a>`0x102D0` | random_icon | `uint8` | V | Random-icon flag: an ability action copies the Ability random_icon column; a weapon attack sets it when either hand item has the Item random_icon column. |

## Behavior

- V: BUi_BattleMain4_RegisterStateKeys sets the state-name keys; the damage-number refresh function reads the others.

## Notes

Partial: fields named from the functions BUi_BattleMain4_RegisterStateKeys and sub_140109134.

## Open questions

? the rest of the object.
