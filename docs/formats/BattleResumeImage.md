# BattleResumeImage

- **Kind:** file format
- **Extension:** `.sav`
- **Area:** [Save data](../areas/save-data.md)
- **Read by:** [SaveSlot_LoadToLive](../functions/SaveSlot_LoadToLive.md), [SaveSlot_WriteFromLive](../functions/SaveSlot_WriteFromLive.md), [SaveSlots_LoadFromFile](../functions/SaveSlots_LoadFromFile.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The payload of a resume entry of `autoenhanced.png`. Two forms: the world and main entries carry the 40,164-byte save work copy (the manual-slot layout) at +356 behind a 340-byte header; the attack and fturn entries, and the battle main entry, carry a 668,112-byte battle snapshot followed by a fixed 1 MB texture page. The two headers and the texture section are in ResumeEntry; the snapshot's blocks are in BattleSnapshot.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="file_header"></a>+0 | file_header | `16 bytes` | V | same shape as the manual-save header: u32 16 at +0, a changing u32 at +4, u32 17 at +8, u32 0 at +12 |
| <a id="tag"></a>+16 | tag | `char[4]` | V | `FFTI` |
| <a id="header_word"></a>+20 | header_word | `u32` | V | 122 (0x7A) in every entry decoded |
| <a id="payload_size"></a>+24 | payload_size | `u32` | V | 40508 for a world entry; equals entry length - 16 |
| <a id="reserved"></a>+340 | reserved | `16 bytes` | V | all 0xFF in the world entries |
| <a id="work_copy"></a>+356 | work_copy | `40164 bytes` | V | a packed save work copy with the manual-slot layout; 882 bytes differ from manual slot 0 of the same save set |
| <a id="trailer"></a>+40520 | trailer | `4 bytes` | V | zero |

## Behavior

- V: the owner's `autoenhanced.png` decodes to 16 entries: `resume_en00..02_{world,attack,fturn,main}.sav`, `resume_enbtl_{world,attack,main}.sav` and `resume_enwm_main.sav`.
- V: decoded lengths: world entries 40524 bytes; `resume_en00_attack.sav` 1101050; `resume_en00_fturn.sav` 1078129; `resume_en00_main.sav` 1077019; `resume_en01_main.sav` 1074514; `resume_en02_main.sav` 1076987; `resume_enbtl_main.sav` 1078129.
- V: every world entry has `SC` at +356; the 40164 bytes there compare with manual slot 0 with only 882 differing bytes.
- I: those differing bytes are the summary, date and situation fields a later pack would change.
- V: the later save-time copy of the same layout is what `SaveSlot_LoadToLive` loads when the slot's situation byte is 1.
- I: the 356-byte prefix is a resume descriptor (scene, entry kind and the time token); its fields are not decoded.
- I: the main/attack/fturn images hold the battle state proper (a 66-byte learned block was matched inside a main entry); their internal layout is not decoded.
- ?: whether the main/attack/fturn image carries a copy of the random state, the frame counters or the camera record.

## Notes

The world entry does carry the slot work copy; it starts at +356, not at a different layout. The container itself is a PNG `ffTo` chunk, `UMIF`, XOR scramble and preset-dictionary deflate.

## Open questions

? what the game does when a requested resume entry is absent; ? which scene event marks each of the resume points 00..02; ? the meaning of the 16 battle control words.
