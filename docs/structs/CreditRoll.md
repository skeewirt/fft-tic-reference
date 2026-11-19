# CreditRoll

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The credit roll object stepped by CreditRoll_Step: the script position, the line templates and the y position.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by |
|---|---|---|---|---|---|
| <a id="next_row"></a>`0x48` | next_row | `int32` | V | Next script row (+72). | [CreditRoll_Step](../functions/CreditRoll_Step.md) |
| <a id="use_title_script"></a>`0x5C` | use_title_script | `uint8` | V | 1 = the script table is UITitleCredit (308), else UIEndCredit (307) (+92). |  |
| <a id="finished"></a>`0x5D` | finished | `uint8` | V | Set at the end of the script (+93). | [CreditRoll_Step](../functions/CreditRoll_Step.md) |
| <a id="template_a"></a>`0x120` | template_a | `pointer` | V | Line template node (+288) of line type 1 ('text'). |  |
| <a id="template_b"></a>`0x138` | template_b | `pointer` | V | Line template (+312) of line type 7 (nodes 'text01' and 'text02'). |  |
| <a id="template_c"></a>`0x168` | template_c | `pointer` | V | Line template (+360) of line type 10 ('text', caption 1). |  |
| <a id="y_position"></a>`0x224` | y_position | `int32` | V | Roll y position (+548); every builder adds the line spacing; the stepper stops at 1080. | [CreditRoll_Step](../functions/CreditRoll_Step.md) |

## Behavior

- V: further templates exist for the other line types.

## Notes

Name is ours. Offsets in decimal in the code: +72, +92, +93, +288, +312, +360, +548.

## Open questions

? the other fields.
