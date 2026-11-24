# OptimalFittingBuysTheCandidatesMarkedWithBit15

- **Kind:** observed behaviour
- **Scope:** engine (Outfitter Fitting, the Optimal Fitting button)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [PartyHandWord](../structs/PartyHandWord.md), [sub_140287D9C](../functions/sub_140287D9C.md), [sub_1402D6914](../functions/sub_1402D6914.md), [sub_1402D5CC4](../functions/sub_1402D5CC4.md), [sub_1402D6464](../functions/sub_1402D6464.md), [sub_1402D6FB8](../functions/sub_1402D6FB8.md), [Item_GetRecord](../functions/Item_GetRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Optimal Fitting takes five candidate words from sub_140287D9C, which sets bit 15 on every candidate that is neither the unit's current item nor its stored original; the button's loop buys a marked candidate (price added to the session total, the hand word stored with bit 15) and puts an unmarked one on as already owned, with no price.

## Behavior

- V: sub_140287D9C writes its five picks to the candidate words (g_EquipCandidates, 0x141876C64, which is g_EquipSet + 0x24). Its last loop compares each pick with the unit's hand word (unit + 0x54 + 2 * slot) and with the unit's entry of the override array; a pick equal to either is left as it is, any other gets bit 15 (an OR with 0xFFFF8000 at 0x140288549) before it is stored.
- V: the Optimal Fitting message (case 0x46 of sub_1402D6914) walks slots 0..3: it loads the candidate with a sign-extending load and tests it with 0xFFFF8000 (0x1402D6A74). A zero or marked candidate: sub_1402D6464 clears the slot (refunding a pending pick), the candidate's price (Item_GetRecord of candidate AND 0x3FF, mask at 0x1402D6B1E; price at record + 8) is added to the session total (dword_143D1AC68), and the candidate word, mark included, becomes the hand word, which is the pending-purchase form of a hand word. An unmarked candidate: when the hand word is pending its price is subtracted (hand word AND 0x3FF, mask register loaded at 0x1402D6A50 and again at 0x1402D6A95 / 0x1402D6B36) and the override entry cleared; the candidate is stored plainly.
- V: any marked candidate sets the screen state byte (byte_140D407BE) to 10, the state in which the confirm button is offered; with none the function posts message 510 or 511 instead.
- V: the same loop, with the same test (0x1402D5EEB) and masks (0x1402D5ECD, 0x1402D5F3D), is in sub_1402D5CC4, the Fitting screen's opener.
- V (seen live 2026-11-24): with the candidates' bit 15 missing at the test, Optimal Fitting put the picks on with a total cost of 0: the stat preview rose (HP 43 to 72 on one unit), the After column and the total did not change and the confirm button stayed dark. With the mark present the same press listed the two picks in the After column, showed their sum (700 + 1,200 = 1,900) and lit the confirm button; confirming took 1,900 gil and equipped both; backing out left equipment and gil as they were.

## Notes

The mark is the picker's own: it is set only on the candidate words. On a hand word bit 15 means picked or bought in this visit (PartyHandWord).

## Open questions

? the accessory (slot 4): the loop walks four slots and the accessory candidate is copied apart (word_141876C6C); not read.
