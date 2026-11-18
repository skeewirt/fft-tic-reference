# ResultLabel_QueueFromUnit

- **Address:** `0x14026801C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char ResultLabel_QueueFromUnit(__int64 task)`
- **Callers:** sub_1401FAEE8, Battle_TurnStep, sub_140202E0C, sub_14020435C, sub_1402059AC, sub_14020BFD4, sub_14020CC50, sub_14026B310, sub_14031BA38, sub_14031C674
- **Callees:** ResultLabel_ShowNext

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a unit's label task from the unit's action-result block: which number and text labels to show, and the queue of status labels (BattleSignal ids) for the statuses the action added or removed.

## Behavior

- V: the unit record is the task pointer at +328; the result block is the unit at +446 (block +0 is read as the unit byte +446).
- V: only when block +0 is non-zero it sets bits of the task word +472 from the result flag byte (block +39, unit +485): 0x80 -> 1, 0x40 -> 2, 0x20 -> 4 (not when block +29 has bit 0x20), 0x10 -> 8, and more bits from the words at unit +460 / +464 and the byte +488.
- V: when the flag byte has bit 0x08 it sets the queue count (task +469) to 0 and, unless block +29 has bit 0x20, walks the five bytes of the added set (block +29..+33) and the removed set (block +34..+38) bit by bit (status id = 8 * byte + bit, bit 0x80 first): a bit of the first set queues byte_140672CC0[id], a bit of the second set queues byte_140672CC0[id] | 0x80 (the second is skipped when unit +475 bit 0x40 or unit +476 bit 0x01 is set and block +34 has bit 0x20). An id whose table byte is 0 is not queued.
- V: the queue is task +476 (bytes); the walk stops adding at 0x1B entries.
- V: the code after the walk (the join at 0x140268256, reached from all three paths) sets the task byte +344 from unit +477, +482 and the task byte +965; when the task byte +832 is 0 it clears the word +838 and calls ResultLabel_ShowNext.
- V: when block +0 is zero it sets task +472 bit 22, 23 or 24 (with bit instructions) from the byte at unit +448 instead (other label kinds).
- V (tested 2026-11-17): only statuses of the 40-bit sets reach this queue; an entry written into the queue after the walk (task +476, count +469) with a BattleSignal id beyond the stock rows is shown like the stock entries (the styled name with its icon).

## State touched

- Calls: [ResultLabel_ShowNext](ResultLabel_ShowNext.md)

## Referenced by

- Appears in flows: [StatusLabelOverAHitUnit](../flows/StatusLabelOverAHitUnit.md)
- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md)

## Notes

Name is ours. The task is a per-unit object of the battle screen (21 slots; ResultLabel_ShowNext takes the slot from the unit byte +1).

## Open questions

? the meaning of each task +472 bit beyond the labels they select in ResultLabel_ShowNext.
