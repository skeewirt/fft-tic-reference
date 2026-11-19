# UIAddonRows

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [UIAddon_LoadByRow](../functions/UIAddon_LoadByRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Rows of the screen table (`uiaddon.nxd`, nxd id 24) that the title screens use: each row's `path` names the layout file a screen loads.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="title first config"></a>242 | `title first config` | `ui/ffto/title/ffto_title_first_config.uib` | V | First-start configuration screen. |
| <a id="title mode select"></a>243 | `title mode select` | `ui/ffto/title/ffto_title_mode_select.uib` | V | Enhanced / Classic mode select. |
| <a id="title menu"></a>244 | `title menu` | `ui/ffto/title/ffto_title_enhanced.uib` | V | The Enhanced title menu (struct UIAddonFFTOTitle). |
| <a id="title play mode"></a>245 | `title play mode` | `ui/ffto/title/ffto_title_playmode.uib` | V | Play mode choice after New Game. |
| <a id="title cushion"></a>247 | `title cushion` | `ui/ffto/title/ffto_title_cushion.uib` | V | Title cushion screen. |
| <a id="system save / load"></a>252 | `system save / load` | `ffto_system_saveload.uib` | V | Save and load list. |
| <a id="config enhanced"></a>253 | `config enhanced` | `ffto_config_enhanced_ver02.uib` | V | Enhanced configuration screen. |
| <a id="saving"></a>256 | `saving` | `ffto_saving.uib` | V | Saving indicator; the title agent's third add-on. |
| <a id="system save / load dialog"></a>257 | `system save / load dialog` | `ffto_system_saveload_dialog.uib` | V | Dialog of the save and load list. |

## Behavior

- V: read in the stock `uiaddon.nxd` (nxd id 24); only the paths of the rows listed were read.

## Notes

Paths of rows 252 to 257 are given without their folder as read; rows other than these were not read.

## Open questions

None recorded.
