# SoundBankSab

- **Kind:** file format
- **Area:** [Event system](../areas/event-system.md)
- **Read by:** [SoundCue_Play](../functions/SoundCue_Play.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

sound/common/sound.sab (0006.pac, 78 MB, stored uncompressed): a SEAD sound bank ('sabf' version 2) whose 690 sounds are the ids SoundCue_Play accepts (0..0x2B1); the audio is CRI HCA, not encrypted.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="magic"></a>+0 | magic | `char[4]` | V | 'sabf', then u8 version 2, u16 header size 0x10, u32 file size; +0x10 the name 'sound'. |
| <a id="chunks"></a>+0x20 | chunks | `16 bytes each` | V | 'snd ' at 0x60, 'seq ' at 0x206A0, 'trk ' at 0x2F5F0, 'mtrl' at 0x4BC50 (tag, u16 version, u16 size, u32 offset). |
| <a id="sound_count"></a>snd + 4 | sound_count | `u16` | V | 690, followed by a table of offsets: the sound id is the index (exactly 0..0x2B1, the bound SoundCue_Play checks). |
| <a id="material_count"></a>mtrl + 4 | material_count | `u16` | V | 810 materials (the audio streams), offsets from mtrl + 16. |
| <a id="codec"></a>material + 5 | codec | `u8` | V | 7 for 781 materials (an HCA stream follows its extra data: 'HCA\0', 'fmt', 'comp', 'loop', 'ciph' 0 = not encrypted), 0 for 29 (empty). +4 channels, +8 sample rate (44100 / 48000), +0x0C / +0x10 loop start / end, +0x18 stream size. |

## Behavior

- I: the remapped sound id selects the snd entry; how an entry reaches its materials (seq, trk) was not read.

## Open questions

None recorded.
