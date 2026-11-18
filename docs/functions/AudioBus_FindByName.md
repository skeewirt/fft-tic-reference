# AudioBus_FindByName

- **Address:** `0x14044DFD4`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `unsigned short AudioBus_FindByName(const char *name)`
- **Callers:** AudioBus_FindMasterOut and the audio set-up code
- **Callees:** the library bus name search

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the mixer bus number for a bus name, or 0xFFFF when there is none.

## Behavior

- V: when the audio library object exists, has its bus table and a version above 0x1090000, asks the library's own name search.
- V: otherwise compares the name with the first eight entries of exe.audio.bus_and_effect_names (BUS0..BUS7) and returns the matching index; a name equal to the master output name returns 0.
- V: no match returns 0xFFFF.

## Referenced by

- Called by: [AudioBus_FindMasterOut](AudioBus_FindMasterOut.md)
- Reads tables: [AudioBusAndEffectNames](../tables/AudioBusAndEffectNames.md)

## Notes

Name is ours.

## Open questions

None recorded.
