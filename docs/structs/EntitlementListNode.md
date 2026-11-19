# EntitlementListNode

- **Kind:** structure
- **Area:** [Application and startup](../areas/app-startup.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One node of the application's entitlement list (g_Application +1488), built by BonusEntitlements_Setup.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="code"></a>`0x10` | code | `char[16]` | V | The entitlement code (SystemBonusEntitlement entitlement), a bounded copy. | [BonusEntitlements_Setup](../functions/BonusEntitlements_Setup.md) |  |
| <a id="owned"></a>`0x21` | owned | `uint8` | V | 1 when the platform check found the entitlement owned (+33); BonusEntitlement_IsOwned returns it. |  | [BonusEntitlement_IsOwned](../functions/BonusEntitlement_IsOwned.md) |
| <a id="unknown_34"></a>`0x22` | unknown_34 | `uint8` | ? | Copy of SystemBonusEntitlement +0x10 (+34); no reader found. | [BonusEntitlements_Setup](../functions/BonusEntitlements_Setup.md) |  |

## Behavior

- V: a code that is already listed gets no second node.

## Notes

Name is ours.

## Open questions

? the reader of +34.
