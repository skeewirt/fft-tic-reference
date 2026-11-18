# UIDialogRowsOfSettings

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UIDialog rows (nxd 34, `UITable_GetRow(34, row)`) the settings screens and neighbours use, and the UI texts they quote.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="restore tab defaults"></a>61 | `restore tab defaults` | `Yes / No` | V | The restore-defaults question for one settings tab. |
| <a id="apply display"></a>62 | `apply display` | `Apply / Restore Previous` | V | The display-change confirmation with a restore-previous option. |
| <a id="discard changes"></a>63 | `discard changes` |  | V | Asked when Back is pressed with changes pending (text not read). |
| <a id="return to title"></a>70 | `return to title` | `Yes / No` | V | The Return to Title warning. |
| <a id="exit game"></a>71 | `exit game` | `Yes / No` | V | The Exit Game warning. |
| <a id="key binding prompt"></a>232 | `key binding prompt` |  | V | The prompt for a key to press (ConfigItem row type 5). |
| <a id="message only"></a>31, 32, 33, 38, 39 | `message only` | ``<string=lstr0>` alone` | V | 31: Dispatch / Cancel (the errand dialogs). |

## Behavior

- V: the dialog buttons and titles are rows of the general UI text table.

## Open questions

None recorded.
