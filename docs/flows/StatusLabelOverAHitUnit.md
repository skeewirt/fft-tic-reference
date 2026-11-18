# StatusLabelOverAHitUnit

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a status an action added or removed is shown over the hit unit (the styled name with its icon): the unit's label task queues one BattleSignal id per status from the result block's two 40-bit sets, then pops and draws them one at a time.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [ResultLabel_QueueFromUnit](../functions/ResultLabel_QueueFromUnit.md) | V | With the result flag 0x08 (block +39) and no KO added (block +29 bit 0x20), every set bit of the added set (block +29..+33) and the removed set (block +34..+38) queues tbl_StatusBattleSignal[id] (\| 0x80 when removed) at task +476; the count is task +469, at most 0x1B; a table byte of 0 queues nothing. |
| <a id="2"></a>2 | [ResultLabel_ShowNext](../functions/ResultLabel_ShowNext.md) | V | After the number labels, each call takes the entry at task +476[count - 1], decrements the count and draws it as label kind 96 (added) or 112 (removed). |
| <a id="3"></a>3 | [BattleLabel_ShowStatusSignal](../functions/BattleLabel_ShowStatusSignal.md) | V | Fills the label node with the BattleSignal row's title and the icon of the UIStatusEffect row whose field +24 names that BattleSignal key (keys 1..1005 scanned). |

## Open questions

? when exactly the callers of ResultLabel_QueueFromUnit run relative to the hit animation.
