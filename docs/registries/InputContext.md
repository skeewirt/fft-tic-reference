# InputContext

- **Kind:** registry
- **Area:** [Input](../areas/input.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The input contexts an action row can belong to: the row's mask against the module's context mask.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="default"></a>1 | `default` | `1` | V | The row's context when neither context byte is set; active. |
| <a id="context_2"></a>2 | `context_2` | `2` | V | UIKeyAssign context_2 (+0x2A): never active in the stock mask, so a row with only this flag is never live. |
| <a id="context_4"></a>4 | `context_4` | `4` | V | UIKeyAssign context_4 (+0x2B): active. |
| <a id="context_16"></a>16 | `context_16` | `16` | I | Present in the module mask 0x15 (1 + 4 + 16); no row selects it. |

## Behavior

- V: the module's mask is written once, with 0x15, by InputModule_Init; Input_UpdateActionRow tests row mask AND module mask.

## Open questions

? why context 2 exists.
