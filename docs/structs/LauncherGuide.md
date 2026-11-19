# LauncherGuide

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The launcher's guide pages state (UIAddonFFTOLauncher): the page set and the nodes the page builders use.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="start_state_node"></a>`0x208` | start_state_node | `pointer` | V | Node that plays the 'Start' state (+520). |
| <a id="info_panel"></a>`0x218` | info_panel | `pointer` | V | Info panel (+536), hidden for the controls page. |
| <a id="controls_panel"></a>`0x220` | controls_panel | `pointer` | V | Controls panel (+544). |
| <a id="start_button_node"></a>`0x230` | start_button_node | `pointer` | V | Node focused on the start page (+560). |
| <a id="guide_set"></a>`0x25C` | guide_set | `int32` | V | Guide set key (+604): 1 Enhanced, 11 Classic. |
| <a id="start_page_enabled"></a>`0x266` | start_page_enabled | `uint8` | V | Set by actions 110 and 112 (+614): a page with start_page set is kept in the page list only then. |
| <a id="picture_image"></a>`0x270` | picture_image | `pointer` | V | Image node of the info page, set with GuiImage_SetIconById (+624). |

## Behavior

- V: Launcher_DrawPage picks the page builder by the LauncherGuide row's controls_page and start_page bytes.

## Notes

Name is ours. Offsets in decimal in the code.

## Open questions

? which launcher entry passes action 110 and which 111.
