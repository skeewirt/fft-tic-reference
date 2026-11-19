# NxdDataEventIdRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.event_id table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 485, 62 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="link"></a>`0x10` | link | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 146 distinct values. |
| <a id="sead_state_parameter"></a>`0x18` | sead_state_parameter | `int32` | M | Measured over every stock row: Every value is a key of nxd.SeadStateParameter. Observed in the stock rows: 0 to 11, 12 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="skippable"></a>`0x20` | skippable | `uint8` | V | Read in the code: Non-zero arms the event for skipping when it is loaded, so the pause overlay offers Skip. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="skip_no_reset"></a>`0x21` | skip_no_reset | `uint8` | V | Read in the code: Non-zero: taking a skip of this event does not run the reset of the event's sound slots; zero: the skip clears slot records 1 and 2 and the event sound entry list. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="keep_auto_advance"></a>`0x22` | keep_auto_advance | `uint8` | V | Read in the code: Non-zero: dialogue auto-advance that was on at the end of the previous event stays on in this event. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="keep_fast_forward"></a>`0x23` | keep_fast_forward | `uint8` | V | Read in the code: Non-zero: a fast-forward running at the end of the previous event continues in this event without a new press. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="skip_once"></a>`0x24` | skip_once | `uint8` | V | Read in the code: Non-zero: the event may be skipped only once (skip-once starts at 1 and becomes 2 after the first skip). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="ends_action"></a>`0x25` | ends_action | `uint8` | V | Read in the code: Non-zero: when this event runs as the battle message raised after a unit acted (BattleMsg_Dispatch kind 8 returns 2) and the unit has moved, the unit's action is marked done. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown26"></a>`0x26` | unknown26 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown27"></a>`0x27` | unknown27 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="no_pause"></a>`0x29` | no_pause | `uint8` | V | Read in the code: Non-zero blocks the event pause overlay (and so skipping) for this event. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="reset_unit_motion"></a>`0x2A` | reset_unit_motion | `uint8` | V | Read in the code: Non-zero: at the start of the event every battle unit not in Crystal, KO, Undead, Jumping, Stone, Chest or Critical is put into motion 2; zero leaves the units' motions alone. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown2b"></a>`0x2B` | unknown2b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataEventId](../tables/NxdDataEventId.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 9 of 19 columns not decoded.
