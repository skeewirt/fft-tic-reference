# UnitIdentityIds

- **Kind:** registry
- **Area:** [Unit data](../areas/unit-data.md)
- **Resolved by:** [Recruit_GenerateUnit](../functions/Recruit_GenerateUnit.md)
- **Values stored in:** [UnitSaveRecord](../structs/UnitSaveRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit is identified by its marker (save record +0, the character template), not by its job (+2): the job changes, the marker stays. A story character's marker, its character-name row (+560, nxd.CharaName) and its own story job share one number; generic units share two markers (0x80, 0x81) and draw a name row at random.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="ramza"></a>1 | `Ramza` | `marker 1, name row 1, story jobs 1, 2 and 3` | V | Seen in every slot of two saves: marker 1 and name row 1 while the job byte was 1, 76, 80 or 89. nxd.CharaName rows 1, 2 and 3 are all named Ramza; jobs 1 and 2 are named Squire, job 3 Gallant Knight. |
| <a id="delita"></a>4 | `Delita` | `marker 4, name row 4, job 4` | V | A guest unit in the saves (record 50). |
| <a id="argath"></a>7 | `Argath` | `marker 7, name row 7, job 7` | V | A guest unit in the saves (record 51). |
| <a id="story characters 1..73"></a>73 | `story characters 1..73` | `job N and name row N name the same character` | I | Compared over nxd.Job and nxd.CharaName: wherever both rows are filled for N in 1..73 they agree (8 Zalbaag / Ark Knight, 13 Orlandeau / Sword Saint, 60..73 the Lucavi). Jobs 74 and up are the generic jobs; name rows past 73 are other named people with no job of their own. |
| <a id="generic male"></a>128 | `generic male` | `marker 128 (0x80), name row 256..511` | V | Every generic male unit in the saves; name rows seen 416..476 (Recruit_GenerateUnit: base 256 plus a random 0..255). |
| <a id="generic female"></a>129 | `generic female` | `marker 129 (0x81), name row 512..767` | V | Every generic female unit in the saves; name rows seen 517..744 (base 512). |

## Open questions

None recorded.
