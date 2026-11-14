# AutoSaveWrite

- **Kind:** flow
- **Area:** [Save data](../areas/save-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where a resume entry comes from and when it is written: the per-frame flush turns dirty group buffers into named entries, stamps each with a CRC, and one write kick sends the whole container. The world-map save and a manual battle save reuse the same entry and the same kick.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 |  | V | Every frame the update calls the flush; it looks at four group buffers (main, world, attack, fturn) and does nothing when none is dirty. |
| <a id="2"></a>2 |  | V | World group dirty: queue `resume_enwm_main.sav`. |
| <a id="3"></a>3 |  | V | fturn group dirty: queue the battle set at point 1 through the same part fan-out; in both saved copies the set is main, world and attack, with no fturn entry. |
| <a id="4"></a>4 |  | V | main group dirty: queue all four parts at resume point ring[+0x30] + 2, then advance the ring modulo 3 (points 00..02). |
| <a id="5"></a>5 |  | V | Each name is formatted from the part table (main, world, attack, fturn) and the point; a per-group map deduplicates repeated names before anything is queued. |
| <a id="6"></a>6 |  | V | The queue function stamps the CRC over the payload and queues the entry with version 17, then marks the group clean. |
| <a id="7"></a>7 |  | V | One write kick for area `AUTOENHANCED` follows the flush when anything was queued; the container writer rebuilds the PNG from the queue. |
| <a id="8"></a>8 | [SaveSlot_WriteFromLive](../functions/SaveSlot_WriteFromLive.md) | V | A manual save made in battle queues its own `resume_enmaNN_world.sav` (NN = slot number) through the same entry function and the same write kick. |
| <a id="9"></a>9 |  | V | The world-map save calls the flush from a UI callback and kicks the same write; the `enwm_main` entry itself is queued by the per-frame flush's world branch, which runs a few frames earlier or later. |

## Behavior

- V: main is written last because the parts are queued in index order 1, 2, 3, 0.
- V: the bodies are built before the flush (the battle handler and the pack code fill the group buffers); the flush only names, deduplicates and queues bytes.
- V: world and main entries are kind 0, attack and fturn are kind 1, and the manual `enmaNN` entry is always kind 0 (it is the world buffer).
- V: when no group is dirty nothing is queued, so the write kick is not issued every frame.

## Notes

The capture writes the two bodies elsewhere: the battle handler for kind 1 and the slot pack code for kind 0, which is why the flush can treat every group the same way.

## Open questions

? which scene event marks each of the three rotating resume points 00..02.
