# BattleStatusPanelVariants

- **Kind:** registry
- **Area:** [Battle](../areas/battle.md)
- **Resolved by:** [Battle_UnitStatusFillAlt](../functions/Battle_UnitStatusFillAlt.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The four variants of the alternate battle unit status panel built by `Battle_UnitStatusFillAlt`. Each variant is a fixed tuple: the scene task that starts it, the four-word position block it passes, the ten-field number table it draws and the shared stat block that supplies the values. Modes 0 and 1 use the actor-side stat block and modes 2 and 3 the target-side block. Modes 0 and 3 are started alone; one battle presentation program starts modes 1 and 2 together.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="mode 0"></a>0 | `mode 0` | `pos 0x1408081E0 \| numbers 0x140808200 \| stat 0x1407832A0` | V | Started by `BattleTask_Slot13Entry`, which battle presentation programs 2, 3 and 6 run as their last task (slot 13, tag 17 in programs 2 and 3, tag 37 in program 6). First position word 0x008C. I: the A (first) actor-side panel. |
| <a id="mode 1"></a>1 | `mode 1` | `pos 0x1408081E8 \| numbers 0x140808480 (tbl_UiStatusNumbersActorB) \| stat 0x1407832A0` | V | Started by `BattleTask_ActorForecastPanel` after the secondary-action preview has run and the predicted HP/MP have been copied into the UI manager; program 5 runs it in slot 12 with tag 19 beside mode 2. First position word 0x0089. I: the B (second) actor-side panel, the actor half of the forecast pair. |
| <a id="mode 2"></a>2 | `mode 2` | `pos 0x1408081F0 \| numbers 0x140808580 (tbl_UiStatusNumbersTargetB) \| stat 0x140783320` | V | Started by `BattleTask_TargetForecastPanel` after it swaps the two preview unit slots and refreshes twice; program 5 runs it in slot 13 with tag 18. First position word 0x0157. I: the B (second) target-side panel, the target half of the forecast pair. |
| <a id="mode 3"></a>3 | `mode 3` | `pos 0x1408081F8 \| numbers 0x140808340 \| stat 0x140783320` | V | Started by `sub_140229D84`, a 78-byte wrapper that only refreshes the scene and seeds its own panel counter; program 4 runs it alone in slot 12 with tag 58. First position word 0x0151. I: the A (first) target-side panel. |

## Behavior

- V: the four position blocks are adjacent four-word blocks at 0x1408081E0, 0x1408081E8, 0x1408081F0 and 0x1408081F8. Only the first word differs (0x008C, 0x0089, 0x0157, 0x0151); word 1 is 0x00AA and words 2 and 3 are 0x0023 and 0x0034 in all four. Word 0/1 is the panel origin and word 2/3 extends the right and bottom edges of the frame.
- V: the number tables are four 0x140-byte tables of ten 32-byte records with the inline names hp, hpmax, mp, mpmax, wt, wtmax, at, atmax, level and exp. The actor pair (0x140808200 and 0x140808480) points its value fields into the stat block at 0x1407832A0; the target pair (0x140808340 and 0x140808580) points into 0x140783320. Modes 0 and 1 draw identical numbers, as do modes 2 and 3.
- V: the two stat blocks are scratch copies of a preview unit, refilled by `sub_140226E44` from the actor and target preview slots before each variant runs. Their word at +0x0A is read as a battle-unit-table slot (above 20 selects fallback constants), not a panel kind. Their +0x18 word is the unit byte +0x41 (or 100 when unit byte +0x1B8 is set), named wt in the number table; the panel body rewrites the +0x02 team code each frame and caps +0x18 at 100.
- V: the first word of each position block is the panel's left edge: 0x008C and 0x0089 for the two actor panels, 0x0157 and 0x0151 for the two target panels. The four-word blocks are handed whole to the frame helper, so words 2/3 are used as width and height extensions, not as text ids.
- I: mode 0 is the standing turn-status panel, mode 3 a lone target panel shown with the banner, and modes 1 and 2 the paired forecast panels (rests on the battle presentation programs that start them: 0 and 3 alone, 1 with 2). The A/B labels come from that pairing; the visible titles are not established.
- ?: a named record for the four position blocks and the two stat blocks; which program selects each variant; why modes 0 and 1 carry byte-identical number tables; the meaning of the 3 and 6 pixel difference between the two words inside each pair.

## Notes

Covers the four call sites, the four position blocks, the four number tables (all ten records each), the two stat blocks and the per-language cell tables, with `sub_140226E44` and `sub_140226CA0` for the stat-block fill. The four position blocks and the two stat blocks have no named global record; the page and this table name them by address. Addresses are build-specific.

## Open questions

? a record for the four position blocks and the two stat blocks; ? the visible titles of the four panels; ? what selects each battle presentation program; ? why the A and B tables of one role are duplicates.
