# AudioBusAndEffectNames

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x14077C420`
- **Rows:** 36 text pointers then 5 function pointers
- **Keyed by:** bus number 0..7 for the first eight; effect id 0..18 (I)
- **Read by:** [AudioBus_FindByName](../functions/AudioBus_FindByName.md), [AudioBus_FindMasterOut](../functions/AudioBus_FindMasterOut.md)
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Names of the audio mixer: eight bus names, the master output name, a second bus list, one shared string, nineteen effect names (reverb, echo, biquad, band pass, compressor, delay, pitch shifter, equalisers, chorus, flanger, distortion, amplitude analyser, surrounder, I3DL2 reverb, multi tap delay, limiter, matrix, bus buffer pool) and five function pointers. Verdict: text.

## Behavior

- V: the bus name search walks the first eight names (bound 8) when the library object is not ready; a name equal to the master name returns bus 0
- V: the master output lookup tries the master name and then BUS0, and returns 0xFFFF when neither is found
- V: each effect name is also returned by a one-line function of the audio library

## Notes

Our names. Tags: V layout, V reader, I use.

## Open questions

- ?: what the second bus list and the shared string are for
