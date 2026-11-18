# AudioBus_FindMasterOut

- **Address:** `0x14044E07C`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `unsigned short AudioBus_FindMasterOut(void)`
- **Callers:** audio set-up code
- **Callees:** AudioBus_FindByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the bus number of the master output.

## Behavior

- V: looks up the bus named MasterOut with AudioBus_FindByName; when that fails, looks up BUS0.
- V: returns 0xFFFF when neither exists.

## State touched

- Calls: [AudioBus_FindByName](AudioBus_FindByName.md)

## Referenced by

- Reads tables: [AudioBusAndEffectNames](../tables/AudioBusAndEffectNames.md)

## Notes

Name is ours.

## Open questions

None recorded.
