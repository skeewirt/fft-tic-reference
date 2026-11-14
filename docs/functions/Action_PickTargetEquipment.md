# Action_PickTargetEquipment

- **Address:** `0x1403065C4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `? (writes a slot descriptor through a pointer in r8)`
- **Callers:** `Formula_37_RendEquipment`, `Formula_38_StealEquipment`, `Formula_46_DarkSwordCrush`
- **Callees:** `Item_GetRecord`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses which equipment slot a steal or break action aims at, from the target unit's hand and body slots, and reports the
chosen slot and item to the action builder.

## Behavior

- V: It starts from a stored target record and an action output pointer; the first thing it writes is a slot-type byte of
  0xFE, meaning no slot chosen.
- V: It inspects five hand words at +0x1A, +0x1C, +0x1E, +0x22 and +0x26 and two byte-sized hand slots at +0x20 and
  +0x24.
- V: A word equal to 255 counts as an empty slot for the three +0x1A..+0x1E words; the two +0x22/+0x26 words are compared
  against a bound of 261 instead.
- V: The ability case is a chain of subtractions on the current ability id, which is read from a word global, so the case
  ids are not immediates in this body; each case tests one of the equipment words at +26 through +38 against 255 and
  0x105.
- V: The hand slots compare the levels of the two weapons, read with byte loads, so only the low byte of an id is used in
  that comparison.
- V: The bound register also derives 255 (the bound minus 6) and is rebuilt from it (255 plus 6).
- V: A unit whose status byte hides the equipment (the reaction/steal flags it reads early) short-circuits before any slot
  is chosen.
- V: The two byte hand slots are read as 8-bit item ids and also treat 255 as empty, so an item id above 255 cannot be
  expressed in that part of the record.
- V: The chosen slot type is encoded as a bit: 0x20, 8, 2, 0x40, 0x80 for the word slots and 0x10 / 4 for the two byte
  slots; the chosen id is stored as a word at +4 of the output.
- I: The bit values line up with the five visible equipment slots (right hand, left hand, head, body, accessory) plus the
  two extra target slots, but the exact slot naming is not stated anywhere in the code read.
- I: The bound of 261 and the 255 empty value are the same conventions used by the inventory and the party record, which
  supports reading this as the steal/break target selector.
- V (2026-11-10; corrects the case-id bullet above): the case ids are compare immediates on the word at 0x1407B0778 (the ability being resolved): 110..114, 138..141, 160..163 and 361..365; each picks one equipment word (slot types 0x80, 0x40, 0x20, 8 or 2, 4 and 16 for the two byte slots); any other id, or a monster unit (byte +6 mask 0x20), clears the slot byte and returns -1 with no item. The choice is keyed by the ability id: see FormulaHandlersChooseTheirEffectByAbilityId.
- V (decompiled again): it stores the slot mask at +0x1B (R+27: 0xFE first, 0 when nothing is picked) and the item id at R+4; it returns 0 when a piece is picked and -1 otherwise. The slot by ability id: 110, 138, 161, 361 head (mask 0x80, unit word +0x1A); 111, 139, 160, 362 body (0x40, +0x1C); 114, 163, 365 accessory (0x20, +0x1E); 113, 141, 162, 364 the weapon with the higher record byte +2 of the two hand bytes (0x10 right, +0x20; 0x04 left, +0x24, only when its value is higher); 112, 140, 363 the right shield (0x08, +0x22) else the left (0x02, +0x26).
- V: a word of 255 or 0x105 and above counts as empty; a unit with +6 bit 0x20 set returns -1 at once.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

- I: Read from the head and the slot decision ladder; the two byte slots are the only place on the item path where an id is
  read from a byte.

## Open questions

- ?: What writes the byte slots at +0x20 and +0x24, and can they ever hold a value above 255?
- ?: Which abilities the case values stand for (I: steal / break equipment); the case ids are deltas in the subtraction
  chain, not immediates in this body.
