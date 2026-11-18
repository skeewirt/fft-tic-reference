# RuntimeJobListEntry

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of the Change Job list as built by the game.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="entry"></a>`0x0` | entry | `uint16` | V | Job id in the low 13 bits; 0x2000 locked for the party; 0x4000 released by another member (mode 3) or the unit own job (mode 2); 0xFFFF ends the list. |

## Referenced by

- Described by tables: [RuntimeJobList](../tables/RuntimeJobList.md)

## Open questions

None recorded.
