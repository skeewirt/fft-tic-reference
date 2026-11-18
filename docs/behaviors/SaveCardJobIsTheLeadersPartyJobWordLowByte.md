# SaveCardJobIsTheLeadersPartyJobWordLowByte

- **Kind:** observed behaviour
- **Scope:** a manual save's slot card
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [SaveWork_PackFromParty](../functions/SaveWork_PackFromParty.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveSlot_BuildClassicTitle](../functions/SaveSlot_BuildClassicTitle.md), [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The slot card's job byte (slot image +274) is the low byte of the leader's 16-bit party job word: SaveWork_PackFromParty picks the first party unit whose marker (+114) is 1..3 and passes its word +36 to SaveWork_PackFromLive, which stores its low byte (0x140218F9D). Only the Classic title reads it back; the Enhanced save list does not show a job.

## Behavior

- V: SaveWork_PackFromParty: leader = first g_PartyUnits[i] with (byte +114) - 1 <= 2; clears the hero name (+257, 16 bytes), +273 = 0xFE, then SaveWork_PackFromLive(slot, word +36, word +0, index).
- V: SaveWork_PackFromLive stores its job argument's low byte at +274 and the next argument's at +275 (0x140218F9D / 0x140218FA3).
- V (seen live 2026-11-17): with a leader whose party job word read 0x1F4 (500), a manual save held 244 at +274.
- V: the reads of +274: SaveSlot_BuildClassicTitle (movzx at 0x14021C17D); SaveLoadList_FillItem (the Enhanced list) fills level, location, next event, date, play time, clear marks and sprite records, no job.

## Open questions

None recorded.
