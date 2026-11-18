# GeneralOptionsOpenAndClose

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the settings screen opens from the mode select or the in-game menu and closes again, through the System agent.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [UIAgentFFTOSystem_OpenConfig](../functions/UIAgentFFTOSystem_OpenConfig.md) | V | Allocates the add-on (3416 bytes), runs its constructor, attaches it, +1456 = the add-on, add-on +52 = mode, agent state 3. |
| <a id="2"></a>2 | [UIAgentFFTOSystem_StateOpenConfig](../functions/UIAgentFFTOSystem_StateOpenConfig.md) | V | UI state 14 fade; when it is done state 0; on leave the layout of `uiaddon.nxd` row 253 is loaded into +1456. |
| <a id="3"></a>3 | [UIAddonFFTOConfig_BindNodes](../functions/UIAddonFFTOConfig_BindNodes.md) | V | Tabs by mode, nodes bound, guide bar shown; ConfigMenu_SetTabTitles and ConfigMenu_ShowTab fill header and rows. |
| <a id="4"></a>4 | [UIAddonFFTOConfig_OnInput](../functions/UIAddonFFTOConfig_OnInput.md) | V | Back asks UIDialog 63 when changes are pending, then calls the agent's vtable +48 with (agent, addon, 0, 0, 0). |
| <a id="5"></a>5 | [UIAgentFFTOSystem_OnAddonEvent](../functions/UIAgentFFTOSystem_OnAddonEvent.md) | V | Event 0 from the General Options add-on selects state 4. |
| <a id="6"></a>6 | [UIAgentFFTOSystem_StateCloseConfig](../functions/UIAgentFFTOSystem_StateCloseConfig.md) | V | Fades to UI state 14 and hides +1456; when done shows the system menu again if +1448 exists, else frees the add-ons. |
| <a id="7"></a>7 | [UIAgent_DetachAddon](../functions/UIAgent_DetachAddon.md) | V | Removes the add-on, hides it and calls its slot 5 (UIAddonFFTOConfig_OnClose: settings save requested). |

## Open questions

None recorded.
