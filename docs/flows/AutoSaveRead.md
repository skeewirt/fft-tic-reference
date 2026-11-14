# AutoSaveRead

- **Kind:** flow
- **Area:** [Save data](../areas/save-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a resume entry reaches the game: the reader queues one request per entry name, a single read kick mounts the container, and the delivery function hands each entry to its object, where the header is validated and the body copied to the checkpoint or the battle buffer.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 |  | V | The reader asks for the main part of a point, then for the parts that point carries: all four for a rotating point 00..02, and the battle set's own parts for point 1. |
| <a id="2"></a>2 |  | V | Each part becomes a queued request: the object, the entry name and a flag go into a 328-byte record on the request vector. |
| <a id="3"></a>3 |  | V | One read kick for area `AUTOENHANCED` follows the requests; it mounts the container and reads every entry the queue names. |
| <a id="4"></a>4 |  | V | Each entry is handed to the delivery function: the 16-byte header goes into the object, the object's handler copies the payload, and the object's post-delivery step runs. |
| <a id="5"></a>5 |  | V | The object checks the stored CRC against the payload before it accepts the entry; a mismatch rejects it. |
| <a id="6"></a>6 |  | V | The import validates the payload header (tag, version 122, kind below 2, self-check product) and copies the summary bytes into the auto slot. |
| <a id="7"></a>7 |  | V | The materialiser copies the body: 40,164 bytes to the checkpoint for kind 0, or 668,112 bytes to the battle buffer with the control words and the inflated texture page for kind 1. |
| <a id="8"></a>8 | [SaveSlot_LoadToLive](../functions/SaveSlot_LoadToLive.md) | V | A battle-saved manual slot requests its own `resume_enmaNN_world.sav` through the same queue and kick, then unpacks the checkpoint. |

## Behavior

- V: requests are told apart by name (the `resume_` prefix), so a replacement that answers the read kick can serve exactly the resume entries and pass every other name to the game.
- V: the kick is synchronous, so the entries are already in their objects when it returns.
- V: the reader is reached from the title's Continue, from the load menu and from the battle-resume setup, so all three take the same path.
- V: the delivered payload is the same shape the writer produced, so the reader needs no schema for the battle body.

## Notes

The header import and the materialiser run per part, so a battle resume pays for the 668,112-byte copy before the first turn and not when the file is mounted.

## Open questions

? the order in which the parts are materialised when several are requested at once.
