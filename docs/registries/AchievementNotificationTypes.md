# AchievementNotificationTypes

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [AchievementOtherNovel_Match](../functions/AchievementOtherNovel_Match.md), [AchievementOtherJournal_Match](../functions/AchievementOtherJournal_Match.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The type number of each achievement notification class: the virtual function at +8 of the notification's vtable returns it, and the achievement classes compare it in their match functions.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="unlockednotification"></a>1 | `UnlockedNotification` |  | V | Type 1. |
| <a id="gameprogresssnotification"></a>2 | `GameProgresssNotification` |  | V | Type 2 (the class name has three s in the game). |
| <a id="jobchangenotification"></a>3 | `JobChangeNotification` |  | V | Type 3. |
| <a id="abilitylearningbymenunotification"></a>4 | `AbilityLearningByMenuNotification` |  | V | Type 4. |
| <a id="abilitylearningbybattlenotification"></a>5 | `AbilityLearningByBattleNotification` |  | V | Type 5. |
| <a id="abilitylearningbysuccessionnotification"></a>6 | `AbilityLearningBySuccessionNotification` |  | V | Type 6. |
| <a id="jobmasternotification"></a>7 | `JobMasterNotification` |  | V | Type 7. |
| <a id="battleactionreactionnotification"></a>8 | `BattleActionReactionNotification` |  | V | Type 8. |
| <a id="battleactionendnotification"></a>9 | `BattleActionEndNotification` |  | V | Type 9. |
| <a id="battleactionteleportnotification"></a>10 | `BattleActionTeleportNotification` |  | V | Type 10. |
| <a id="battleactionpoachnotification"></a>11 | `BattleActionPoachNotification` |  | V | Type 11; sent by Poach_GiveResult. |
| <a id="battleactionmovenotification"></a>12 | `BattleActionMoveNotification` |  | V | Type 12. |
| <a id="changeturnnotification"></a>13 | `ChangeTurnNotification` |  | V | Type 13. |
| <a id="levelupnotification"></a>14 | `LevelUpNotification` |  | V | Type 14. |
| <a id="profitstartnotification"></a>15 | `ProfitStartNotification` |  | V | Type 15. |
| <a id="profitendnotification"></a>16 | `ProfitEndNotification` |  | V | Type 16. |
| <a id="employnotification"></a>17 | `EmployNotification` |  | V | Type 17. |
| <a id="joinnotification"></a>18 | `JoinNotification` |  | V | Type 18. |
| <a id="poachprocessnotification"></a>19 | `PoachProcessNotification` |  | V | Type 19. |
| <a id="poachsellnotification"></a>20 | `PoachSellNotification` |  | V | Type 20. |
| <a id="mapitemdiscoverynotification"></a>21 | `MapItemDiscoveryNotification` |  | V | Type 21. |
| <a id="chocoboridenotification"></a>22 | `ChocoboRideNotification` |  | V | Type 22. |
| <a id="egghatchnotification"></a>23 | `EggHatchNotification` |  | V | Type 23. |
| <a id="novelreadthroughnotification"></a>24 | `NovelReadThroughNotification` |  | V | Type 24; carries the book id at +8; sent by NovelReader_SendReadThrough and matched by AchievementOtherNovel_Match against Achievement book. |
| <a id="journalnotification"></a>25 | `JournalNotification` |  | V | Type 25; carries the Journal event_id (+0x18) at +8; matched by AchievementOtherJournal_Match against Achievement event_id. |
| <a id="glossarynotification"></a>26 | `GlossaryNotification` |  | V | Type 26. |
| <a id="checkjobmasternotification"></a>27 | `CheckJobMasterNotification` |  | V | Type 27. |
| <a id="checklevelnotification"></a>28 | `CheckLevelNotification` |  | V | Type 28. |

## Behavior

- V: each type function returns its constant.

## Notes

Which achievement class matches which type was read only for the novel and journal classes.

## Open questions

? the match rules of the other classes.
