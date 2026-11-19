# BonusEntitlementGroupMatch

- **Kind:** observed behaviour
- **Scope:** engine (bonus entitlements)
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [BonusEntitlements_Setup](../functions/BonusEntitlements_Setup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The bonus entitlement setup matches the entitlement row's group number against the group number of every DLCPathList row; it does not look the path list up by key.

## Behavior

- V: SystemBonusEntitlement dlc_path_group (+0xC) is compared with DLCPathList +8 for every DLCPathList row; the matching rows' paths (+4) are collected.
- M: both stock rows that name a group name group 1, which is also the key of the only DLCPathList group row, so a key reading and a group reading agree on the stock data.

## Notes

DLCPathList +8 is therefore a group number.

## Open questions

None recorded.
