# ResumeEntry

- **Kind:** file format
- **Extension:** `.sav`
- **Area:** [Save data](../areas/save-data.md)
- **Read by:** [SaveSlot_LoadToLive](../functions/SaveSlot_LoadToLive.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of `autoenhanced.png`: a 16-byte entry header, a 340-byte payload header, then a body that is either the 40,164-byte save work copy (kind 0, the world and main form) or a 668,112-byte battle snapshot followed by a fixed 1 MB texture page (kind 1). Completes BattleResumeImage, which describes the payload bodies; this page gives the two headers and the texture section. Offsets below are from the start of the entry.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="entry_header"></a>+0x00 | entry_header | `{uint32 size; uint32 crc32; uint32 version; uint32 reserved}` | V | 16, CRC-32 of the payload, 17, 0; the CRC is compared when the entry is attached to its object. |
| <a id="magic"></a>+0x10 | magic | `char[4]` | V | `FFTI`; a payload with another tag is rejected by the import. |
| <a id="version"></a>+0x14 | version | `uint32` | V | 122 (0x7A); any other value is rejected. |
| <a id="structured_size"></a>+0x18 | structured_size | `uint32` | V | 40,508 for kind 0 or 786,776 for kind 1: the size of the structured payload, not the entry length (a kind-1 entry is longer by its texture section). |
| <a id="kind"></a>+0x1C | kind | `uint32` | V | 0 = save work copy (world and main entries), 1 = battle (attack and fturn, and the battle main entry). |
| <a id="self_check"></a>+0x20 | self_check | `uint32` | V | 70 (0x46) times the structured size; the import recomputes the product from the tag's first byte and the size field and rejects a mismatch. |
| <a id="leader_name"></a>+0x24 | leader_name | `char[16]` | V | Blank in every decoded entry; the import copies 17 bytes (with the next byte) into the auto slot's name field. |
| <a id="summary_tag"></a>+0x34 | summary_tag | `uint8` | V | 0xFE, the empty-name marker the manual slot summary also carries. |
| <a id="summary_job"></a>+0x35 | summary_job | `uint8` | V | The first party unit's job byte. |
| <a id="summary_level"></a>+0x36 | summary_level | `uint8` | V | The first party unit's level. |
| <a id="place_bytes"></a>+0x37 | place_bytes | `uint8[2]` | V | Two scene variables read after a scene update; they become the slot summary's two place bytes. |
| <a id="place_id"></a>+0x39 | place_id | `uint8` | V | Scene variable 0x31, the map/place byte. |
| <a id="party_index"></a>+0x3A | party_index | `uint8` | V | The leader's party slot (1 when the party object is absent). |
| <a id="cleared"></a>+0x3B | cleared | `uint8` | V | Game-cleared flag, copied into the summary. |
| <a id="global_byte"></a>+0x3C | global_byte | `uint8` | V | A global byte copied into the header but not read back by the import. |
| <a id="config_byte"></a>+0x3D | config_byte | `uint8` | V | A config byte (the difficulty), copied into the summary. |
| <a id="battle_marker"></a>+0x3E | battle_marker | `uint8` | V | Set when kind is 1; the materialiser branches on it. |
| <a id="new_game_plus"></a>+0x3F | new_game_plus | `uint8` | V | New-game+ flag, copied into the summary. |
| <a id="reserved_at_40"></a>+0x40 | reserved_at_40 | `uint32` | V | Zero. |
| <a id="play_time"></a>+0x44 | play_time | `uint32` | V | Hours x 3600 + minutes x 60 + seconds, from the three clock bytes at 0x141856700. |
| <a id="timestamp"></a>+0x48 | timestamp | `uint64` | V | Time of the capture; the import puts it at slot +68. |
| <a id="progress"></a>+0x50 | progress | `uint32` | V | Main progress value, copied into the summary. |
| <a id="previews"></a>+0x54 | previews | `preview_record[6]` | V | Six 32-byte preview records for kind 0 only (the leader, then units 50..53); the resume list draws its sprites from them. |
| <a id="reserved_at_114"></a>+0x114 | reserved_at_114 | `uint32` | V | Zero. |
| <a id="battle_control"></a>+0x118 | battle_control | `uint32[3]` | V | Three battle control words; the materialiser copies them back to the globals they came from (0x142E7FC78 and two more). |
| <a id="battle_words"></a>+0x124 | battle_words | `uint32[16]` | V | Sixteen more battle control words (0x142E7FEA0). |
| <a id="body"></a>+0x164 | body | `work copy or battle snapshot` | V | Kind 0: the 40,164-byte work copy, then 4 zero bytes. Kind 1: the 668,112-byte snapshot, then 118,324 zero bytes. |
| <a id="yox_magic"></a>+0xC0168 | yox_magic | `char[4]` | V | `YOX` and a zero byte, at the end of the structured size; kind 1 only. |
| <a id="yox_codec"></a>+0xC016C | yox_codec | `uint32` | V | 2 = deflate, 0 = stored (the writer falls back when compression fails). |
| <a id="yox_raw_size"></a>+0xC0170 | yox_raw_size | `uint64` | V | 1,048,576: the inflated page has a fixed size. |
| <a id="yox_data"></a>+0xC0178 | yox_data | `deflate or stored bytes` | V | Inflates into the fixed 1 MB page, a 1024 x 512 16-bpp image; it carries no object id. |

## Behavior

- V: two saved backups hold 16 entries: `resume_en00..02_{main,world,attack,fturn}`, `resume_enbtl_{main,world,attack}` and `resume_enwm_main`; the battle set has no fturn entry.
- V: kind 0 is a manual-slot work copy byte for byte, only shifted (body at entry +356, which is slot +0); main and world entries differ in name and summary, not in form.
- V: kind 1 is a sparse same-build memory snapshot (41.5 to 54.7 KB of its 668,112 bytes are nonzero) followed by 118,324 zero bytes, so the structured size stays the constant 786,776.
- V: the texture page follows the structured size and is not counted in it; the attack and fturn captures carry different pages, so it must be stored byte exact.
- V: the queue function stamps the CRC and queues with version 17, and the import verifies the self-check product before it copies the summary into the auto slot.
- I: the 340-byte header is a union of a resume summary and battle control words, because a kind-0 entry fills only the summary half and the kind-1 entries add the battle block.

## Notes

BattleResumeImage gives the payload forms, BattleSnapshot the blocks of the kind-1 body, and UnitSaveRecord the fields of the work copy. Entry lengths follow from the forms: 40,524 for kind 0 and 1,119,315 in the observed kind-1 copy.

## Open questions

? the meaning of the 16 battle control words beyond the globals they are copied to; ? what the game does when a requested resume entry is absent.
