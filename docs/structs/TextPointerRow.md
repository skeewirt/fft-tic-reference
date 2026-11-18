# TextPointerRow

- **Kind:** structure
- **Area:** [Resource](../areas/resource.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of a table of text pointers (audio loader errors, mixer names, XML status names, value type names).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="text"></a>`0x0` | text | `pointer` | V | pointer to a zero-terminated name |

## Referenced by

- Described by tables: [AudioBusAndEffectNames](../tables/AudioBusAndEffectNames.md), [AudioCueLoadErrorNames](../tables/AudioCueLoadErrorNames.md), [AudioTableValueTypeNames](../tables/AudioTableValueTypeNames.md), [AudioTableValueTypeNamesAlt](../tables/AudioTableValueTypeNamesAlt.md), [GfxBlueNoiseTexturePaths](../tables/GfxBlueNoiseTexturePaths.md), [UiEquipScreenNodeNames](../tables/UiEquipScreenNodeNames.md), [UiEventCommandNames](../tables/UiEventCommandNames.md), [UiEventWindowFontAndNameNodeRun](../tables/UiEventWindowFontAndNameNodeRun.md), [UiGuideTipPageNamesRun](../tables/UiGuideTipPageNamesRun.md), [UiLauncherControllerGuideLabelsRun](../tables/UiLauncherControllerGuideLabelsRun.md), [UiLauncherModeNamesRun](../tables/UiLauncherModeNamesRun.md), [UiPartyMemberPartNodeNamesRun](../tables/UiPartyMemberPartNodeNamesRun.md), [UiRadioButtonNodeNamesRun](../tables/UiRadioButtonNodeNamesRun.md), [UiStartupScreenNodeNamesRun](../tables/UiStartupScreenNodeNamesRun.md), [UiStoryButtonNodeNamesRun](../tables/UiStoryButtonNodeNamesRun.md), [UiTabButtonNodeNamesRun](../tables/UiTabButtonNodeNamesRun.md), [XmlStatusNames](../tables/XmlStatusNames.md)

## Open questions

None recorded.
