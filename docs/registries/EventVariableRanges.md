# EventVariableRanges

- **Kind:** registry
- **Area:** [Event system](../areas/event-system.md)
- **Resolved by:** [EventVar_Read](../functions/EventVar_Read.md), [EventVar_Write](../functions/EventVar_Write.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The runs of event variable ids that mirror a game table: the id is a base plus the row key of that table, and the value is a flag or a small state. One member per range, with its rule and at most three examples; the rows themselves are the game's tables, not repeated here. The member id is the first id of the range.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="battle_local_block"></a>112 | `battle_local_block` | `32 ids (112..143)` | I | Battle-local block. The scenario setup writes 0 to every id in it before each battle, and the write lock leaves the whole block writable. Scripts of battle events use single ids of it as flags (see the entries 125..134 above). The block is dwords for 112..127 and bits for 128..143. Tag I: the reset and the lock exemption are decoded; the purpose of each id is only inferred from the scripts that set it. |
| <a id="reopen_flags"></a>420 | `reopen_flags` | `24 ids (420..443)` | ? | A block of 24 flags counted by the legacy menu's re-open helper (kind 29) while variable 146 is set. No writer was found for 420..426 and 441..443; 427..440 of the same block are the special replay unlocks below. Tag ?: the count is decoded, the meaning of the flags that nothing writes is not. |
| <a id="special_replay_unlocks"></a>427 | `special_replay_unlocks` | `14 ids (427..440)` | V | Special replay unlock n = id - 427 (n 0..13): the event viewer's special entry n, whose label is message 64 + n of text bank 29 and whose replayed event comes from word 64 + n of the replay event table. The viewer's hidden-entry test keeps most of these entries from ever being listed. Examples: 427 replays event 588; 428 replays event 586; 430 replays nothing (word 0xFFFF). Overlaps the re-open block above. |
| <a id="plain_replay_unlocks"></a>444 | `plain_replay_unlocks` | `64 ids (444..507)` | V | Plain replay unlock k = id - 444 (k 0..63): when set, the event viewer lists plain entry k (label message k of text bank 29), which replays the event in word k of the replay event table. Usually a later script of the story sets it, not always the very next one. Examples: 444 replays event 7 (set by event 12); 456 replays event 68; 507 replays event 299. |
| <a id="location_open_flags"></a>512 | `location_open_flags` | `43 ids (512..554)` | V | World-map location n = id - 512, where n is the key of the Town table (0..42): non-zero means the location is revealed (drawn, listed in the location menus, selectable). The world-event rows reveal a location (action 34) only while its flag is 0. Id 555 would be key 43, an empty row; keys 44..46 take a special path that uses situation flags instead of this range. Examples: 512 is Royal City of Lesalia (key 0); 513 is key 1; 554 is key 42. |
| <a id="route_open_flags"></a>556 | `route_open_flags` | `51 ids (556..606)` | V | World-map route n = id - 556, where n is the row of the Route table: non-zero means the route between its two town columns is open. The world-event rows open a route (action 32) only while its flag is 0, and the route search and road markers use only open routes; the map refreshes every route's drawing from these flags when it opens. Examples: 556 is route row 0 between Eagrose Castle and Ziekden Fortress; 557 is row 1; 606 is row 50. |
| <a id="location_visited_flags"></a>615 | `location_visited_flags` | `43 ids (615..657)` | I | Location n = id - 615 (same key as 512 + n): visited, or its arrival event done. The location list shows the row in its visited state when set, the destination balloons are skipped, and for towns 0..15 the town services need it together with the open flag. Tag I: the readers are decoded, the setter is inferred from the arrival event script that writes it. Example: 615 is Royal City of Lesalia (set by event 224). |
| <a id="destination_choice_flags"></a>658 | `destination_choice_flags` | `63 ids (658..720)` | I | Destination-choice flags: the choice list of the world map reads 658 + a byte of a 68-byte table indexed by candidate id minus one (values 0..62); a set flag removes the candidate from the list. Candidate ids whose byte is 0 all land on 658. Tag I: the reader is decoded; which of the 62 other ids are used was not settled (the world-event table references only the Fort Besselat pair). Examples: 658 is the shared base; 659..720 are the other flags. |
| <a id="rumour_unlock_flags"></a>721 | `rumour_unlock_flags` | `64 ids (721..784; 23 rows used, 721..743)` | V | Rumour r = id - 721, where r is the key of the Gossip table: non-zero means the rumour is unlocked for the taverns whose town bit is set in the rumour town mask table. Applying a rumour at the tavern can also write story flags (for example 166 and 170 above). Ids 744..784 have no Gossip row; 759 is documented as its own entry above. Examples: 721 is rumour 0 (The Corpse Brigade); 740 is rumour 19; 743 is rumour 22. |
| <a id="treasure_found_flags"></a>801 | `treasure_found_flags` | `47 ids (801..847)` | V | The treasure list: the id is read as a variable from the variable column (offset +12) of a Collection row of kind 0 (treasures) or of a Book row (ids 818..821 and 832); non-zero means found or obtained. 801..831 is the errand treasure pool 1 (31 ids). 833 and 834 are skipped by the list builder, and 835..847 have no Collection or Book row. Examples: 801 is Collection row 16 (Four-Deity Plate); 818 is Book row 0 (Mesa's Musings); 832 is a Book id. |
| <a id="unexplored_land_flags"></a>848 | `unexplored_land_flags` | `16 ids (848..863)` | V | Unexplored lands found: the id is the variable column (+12) of a Collection row of kind 1; non-zero means the land was found. The 16 ids are the errand treasure pool 2, and the list builder and the completion counter read them. Examples: 848 is Collection row 0 (Chaos Shrine); 849 and 863 are the next and last ids. |
| <a id="errand_state_nibbles"></a>864 | `errand_state_nibbles` | `96 ids (864..959)` | V | Errand e = id - 864, where e is the key of the Profit table (96 rows). Each id is a nibble holding state bits: 0x02 dispatched (set at the start, cleared by the result and the recall), 0x04 succeeded (also the prerequisite test of other errands and the report list), 0x08 attempted (set at the start). 0x01 was not seen used. Examples: 864 is errand 0 (The Fate of Our Company); 865 is errand 1; 959 is errand 95. |
| <a id="person_entries"></a>960 | `person_entries` | `64 ids (960..1023)` | V | Person p = id - 960 (position in the personae list, 64 positions; 18, 21, 52 and 53 are never listed). Value 0 = not listed; 1..11 = the biography stage shown (text bank 30, message 16 x p + value); 12..15 = how the unit left the party: 12 dismissed, 13 deserted in battle, 14 left over a change of ideals, 15 died in battle. A store is accepted only while the current value is below 12, so a departure value freezes the entry (checked whatever the write lock says). The 12..15 meaning is V for the nine persons whose lore variants test it (974, 975, 982, 984, 988, 989, 994, 1005, 1006) and I for the other positions; the 1..11 stages are I except where a script shows them. The unit marker table UnitMarkerPersonVariables names 15 of these ids, and writes 12 on a confirmed dismissal. Examples: 974 is Agrias (position 14); 975 is Orlandeau; 982 is Beowulf. |

## Behavior

- V: each range is read by code as base + row key; the ids of one range are never mixed with another's keys.
- V: ids 960 and above accept a store only while their current value is below 12 (see EventVariableWriteLock).
- I: the visited flags (615..657) and the destination-choice flags (658..720) are tagged from the shape of their readers; the other ranges are proven by a table row that points at the id.

## Referenced by

- Observed behaviours: [EventVariableWriteLock](../behaviors/EventVariableWriteLock.md)

## Notes

Our names. Where a game name labels a row it is an example, never a list.

## Open questions

- ?: which destination-choice ids besides the Fort Besselat pair are ever used
