# Battle formulas

The battle formula functions, dispatched by formula id.

Functions: 153, Observed behaviours: 1.

## Functions (153)

| Name | Address | Purpose |
|---|---|---|
| [Battle_Rand15](../functions/Battle_Rand15.md) | `0x14030D088` | The battle's random number: a 15-bit value, fixed while a forecast runs. |
| [Formula_01_NormalAttack](../functions/Formula_01_NormalAttack.md) | `0x140307120` | Normal attack: the physical evade gate, then the whole weapon attack (weapon-type value x WP with the physical modifiers, critical and element), and the weapon's status on the 19 percent roll. |
| [Formula_02_WeaponCastsSpell](../functions/Formula_02_WeaponCastsSpell.md) | `0x140307140` | Weapon attack that can cast a spell: the whole weapon attack, and on the 19 percent status roll the weapon's inflict byte becomes the ability resolved next instead of a status. |
| [Formula_03_WeaponPowerSquared](../functions/Formula_03_WeaponPowerSquared.md) | `0x1403071A4` | Weapon power squared: A = WP + weapon bonus, B = WP, through the physical modifiers and the critical roll, with no hit roll of its own. |
| [Formula_04_MagicGun](../functions/Formula_04_MagicGun.md) | `0x1403071DC` | Magic gun: picks one of three spells of the weapon's element by a random roll and deals its damage as (WP + bonus) x the spell's Y through the magic chain. |
| [Formula_05_WeaponAttackNoElement](../functions/Formula_05_WeaponAttackNoElement.md) | `0x1403072F8` | Weapon attack without the element steps: the physical evade roll, the weapon-type A and B, the modifiers and critical, then the 19 percent status roll. |
| [Formula_06_WeaponDrainHP](../functions/Formula_06_WeaponDrainHP.md) | `0x140307388` | Weapon attack that drains HP: the weapon-type damage, and the caster gains what the target loses (reversed on an Undead target). |
| [Formula_07_WeaponHeal](../functions/Formula_07_WeaponHeal.md) | `0x1403073C4` | Weapon that heals: the weapon-type amount through the zodiac and physical modifiers, given to the target as HP (damage on an Undead target); no hit roll. |
| [Formula_08_BlackMagickSummonDamage](../functions/Formula_08_BlackMagickSummonDamage.md) | `0x1403073F4` | Magic damage: MA x Y with elemental, Shell, Zodiac and Faith modifiers. |
| [Formula_09_Gravity](../functions/Formula_09_Gravity.md) | `0x140307474` | Gravity damage: a percentage of the target's maximum HP, gated by a magic hit check. |
| [Formula_100_JumpDamage](../functions/Formula_100_JumpDamage.md) | `0x140309474` | Jump damage: PA x WP, with PA x 3/2 when the weapon is a spear and PA x (PA x Brave / 100) bare-handed, through the caster and target modifiers. |
| [Formula_101_Physical80HPDrain](../functions/Formula_101_Physical80HPDrain.md) | `0x14030D540` | PA x WP physical damage reduced to 80 percent, and the caster gains the damage dealt as HP (reversed on an Undead target). |
| [Formula_102_WotLPhysical80MPDrain](../functions/Formula_102_WotLPhysical80MPDrain.md) | `0x14030D5AC` | WotL physical: PA x WP damage reduced to 80%, with the difference restoring the caster's MP. |
| [Formula_103_WotLHolySwordAlias](../functions/Formula_103_WotLHolySwordAlias.md) | `0x14030D618` | WotL Holy Sword: alias of F45; shares its target and calculation. |
| [Formula_104_WotLDistanceScaledPhysical](../functions/Formula_104_WotLDistanceScaledPhysical.md) | `0x14030D620` | Distance-scaled weapon attack: the weapon-type value and WP, with WP + 3 next to the target, WP + 1 at two tiles and half the weapon-type value from three tiles, then the whole physical chain. |
| [Formula_105_WotLLevelScaledPhysical](../functions/Formula_105_WotLLevelScaledPhysical.md) | `0x14030D6E0` | WotL level-scaled physical: PA comes from MA, and Y scales with max HP and MA. |
| [Formula_106_ReDispatchChainFormula](../functions/Formula_106_ReDispatchChainFormula.md) | `0x14030D720` | Re-dispatch: calls the formula table with a different ID, then applies the post-dispatch step. |
| [Formula_10_FaithBasedStatus](../functions/Formula_10_FaithBasedStatus.md) | `0x1403074EC` | Faith-based status: a magic hit check that applies a status effect and deals no damage. |
| [Formula_11_FaithBasedBuff](../functions/Formula_11_FaithBasedBuff.md) | `0x14030750C` | Faith-based buff: a magic hit check that applies a beneficial status. |
| [Formula_12_MagicalHealing](../functions/Formula_12_MagicalHealing.md) | `0x140307564` | Magical healing: MA x Y healing with Zodiac and Faith scaling, plus the undead reversal check. |
| [Formula_13_RaiseRevive](../functions/Formula_13_RaiseRevive.md) | `0x1403075AC` | Raise/revive: a magic hit check followed by percentage-of-max-HP healing when the target is dead. |
| [Formula_14_DeathInstantKill](../functions/Formula_14_DeathInstantKill.md) | `0x140307640` | Instant death: a magic hit check followed by percentage-of-max-HP damage, with undead and immunity handling. |
| [Formula_15_MPDrainMagical](../functions/Formula_15_MPDrainMagical.md) | `0x140307748` | MP drain: a magic hit check then MP damage based on the target's maximum MP, restoring the caster's MP. |
| [Formula_16_HPDrainMagical](../functions/Formula_16_HPDrainMagical.md) | `0x1403077A0` | HP drain: a magic hit check then HP damage based on the target's maximum HP, restoring the caster's HP. |
| [Formula_18_Quick](../functions/Formula_18_Quick.md) | `0x1403077F4` | Quick: a magic hit check that sets the extra-turn effect. |
| [Formula_20_GolemShield](../functions/Formula_20_GolemShield.md) | `0x14030784C` | Golem shield: a magic hit check that creates a damage-absorbing barrier. |
| [Formula_21_Return](../functions/Formula_21_Return.md) | `0x1403078FC` | Return: a magic hit check that resets the target's CT. |
| [Formula_22_Disempower](../functions/Formula_22_Disempower.md) | `0x140307928` | Disempower: a magic hit check that deals MP damage equal to the target's current MP. |
| [Formula_23_Gravija](../functions/Formula_23_Gravija.md) | `0x140307960` | Gravija: a magic hit check that reduces the target to 1 HP. |
| [Formula_26_StatSap](../functions/Formula_26_StatSap.md) | `0x1403079A8` | Stat lowering by magic: the magic evade gate, then a chance of MA + Y (magic modifiers, zodiac, Faith); on success the stat the ability id selects drops by X. No damage. |
| [Formula_27_Magicksap](../functions/Formula_27_Magicksap.md) | `0x140307A24` | Magicksap: a magic hit check that deals MP damage based on the target's maximum MP. |
| [Formula_28_BardSongs](../functions/Formula_28_BardSongs.md) | `0x140307A70` | Songs: an X percent roll (Formula_BardDancerGate), then an effect chosen by the ability id: MP or HP restore of MA + Y, Speed, PA or MA + 1, a status, or every stat up. |
| [Formula_29_DancerDances](../functions/Formula_29_DancerDances.md) | `0x140307B44` | Dances: an X percent roll, then an effect chosen by the ability id: MP or HP damage of weapon-type value + WP, Speed, PA or MA - 1, a status, or the all-stats change downward. |
| [Formula_30_IaidoHeaven](../functions/Formula_30_IaidoHeaven.md) | `0x140307C10` | Iaido Heaven: PA is replaced by MA and Y is averaged with MA, then the magic chain runs. |
| [Formula_31_IaidoNether](../functions/Formula_31_IaidoNether.md) | `0x140307C28` | Iaido Nether: MA x Y with element, caster/Shell/Sleep/Zodiac and inverse-Faith scaling. |
| [Formula_32_DrawOutDamage](../functions/Formula_32_DrawOutDamage.md) | `0x140307D50` | Draw Out damage: MA x Y through the magic chain, with weather and element checks. |
| [Formula_33_DrawOutDamageStatus](../functions/Formula_33_DrawOutDamageStatus.md) | `0x140307D84` | Draw Out damage plus status: MA x Y magic damage written to the MP-damage field. |
| [Formula_34_DrawOutBuff](../functions/Formula_34_DrawOutBuff.md) | `0x140307DE8` | Draw Out buff: status-only; applies the buff carried by the ability data. |
| [Formula_35_DrawOutHeal](../functions/Formula_35_DrawOutHeal.md) | `0x140307DFC` | Draw Out heal: MA x Y healing with the undead reversal check. |
| [Formula_36_Geomancy](../functions/Formula_36_Geomancy.md) | `0x140307E34` | Geomancy: MA and an averaged Y through the magic chain, with a terrain element. |
| [Formula_37_RendEquipment](../functions/Formula_37_RendEquipment.md) | `0x140307E74` | Break equipment: when Action_PickTargetEquipment finds a piece it resolves a sub-action; otherwise the physical evade gate, then a chance of PA + WP + Y; on success (and past Formula_StealGate) the flag word gets the ... |
| [Formula_38_StealEquipment](../functions/Formula_38_StealEquipment.md) | `0x140307FCC` | Steal equipment: an equipment-slot check then a Speed-based hit; success steals the item. |
| [Formula_39_StealGil](../functions/Formula_39_StealGil.md) | `0x140308098` | Steal Gil: a physical evade check and a Speed-based hit, then a gil transfer. |
| [Formula_40_StealEXP](../functions/Formula_40_StealEXP.md) | `0x1403080F8` | Steal EXP: a physical evade check and a Speed-based hit, then a CT/EXP modifier. |
| [Formula_41_StealHeartCharm](../functions/Formula_41_StealHeartCharm.md) | `0x140308208` | Charm: a chance of MA + X (zodiac only, no Faith); on success, when caster and target are on different sides, the ability's status through Formula_56. |
| [Formula_42_Speechcraft](../functions/Formula_42_Speechcraft.md) | `0x140308284` | Talk: a target with the refusing reaction may refuse on a Brave roll; then a chance of MA + X (zodiac only, no Faith) and an effect chosen by the ability id. |
| [Formula_43_RendStats](../functions/Formula_43_RendStats.md) | `0x1403083F4` | Stat lowering by force: the physical evade gate, then a chance of PA + Y with the physical modifiers; on success the stat the ability id selects drops by X. No damage. |
| [Formula_44_RendMP](../functions/Formula_44_RendMP.md) | `0x140308448` | MP damage by force: the physical evade gate, a chance of PA + Y with the physical modifiers, then MP damage of Y percent of the target's max MP. |
| [Formula_45_HolySword](../functions/Formula_45_HolySword.md) | `0x1403084C4` | Holy Sword: PA x (WP + Y) through the physical chain, then a status. |
| [Formula_46_DarkSwordCrush](../functions/Formula_46_DarkSwordCrush.md) | `0x140308538` | Dark Sword (Crush): PA x WP physical damage that also destroys a piece of equipment. |
| [Formula_47_DuskbladeMPDrain](../functions/Formula_47_DuskbladeMPDrain.md) | `0x140308664` | Duskblade: PA x WP physical damage that restores the caster's MP. |
| [Formula_48_ShadowbladeHPDrain](../functions/Formula_48_ShadowbladeHPDrain.md) | `0x1403086AC` | Shadowblade: PA x WP physical damage that heals the caster for the damage dealt. |
| [Formula_49_MonkPhysicalAveraged](../functions/Formula_49_MonkPhysicalAveraged.md) | `0x1403086F4` | Monk physical (averaged): PA x Y where Y is averaged with PA, then the physical chain. |
| [Formula_50_PummelRandomHits](../functions/Formula_50_PummelRandomHits.md) | `0x140308780` | Pummel: an additive PA + averaged-Y base multiplied by a random number of hits. |
| [Formula_51_Purification](../functions/Formula_51_Purification.md) | `0x140308820` | Purification: an additive PA + X hit check that removes negative statuses. |
| [Formula_52_Chakra](../functions/Formula_52_Chakra.md) | `0x140308874` | Chakra: PA x Y healing split between HP and MP, with no Faith scaling. |
| [Formula_53_Revive](../functions/Formula_53_Revive.md) | `0x1403088D4` | Revive: a PA-based hit check then percentage-of-max-HP healing, with the undead check. |
| [Formula_54_FocusAccumulate](../functions/Formula_54_FocusAccumulate.md) | `0x14030602C` | Focus/Accumulate: a self-only PA increase that always succeeds. |
| [Formula_55_RushBasicPhysical](../functions/Formula_55_RushBasicPhysical.md) | `0x14030895C` | Rush/basic physical: PA x a random number of hits with the standard physical modifiers. |
| [Formula_56_StatusOnlyApplication](../functions/Formula_56_StatusOnlyApplication.md) | `0x14030698C` | Status-only application: the shared status engine used by many formulas; no damage component. |
| [Formula_57_Tailwind](../functions/Formula_57_Tailwind.md) | `0x14030605C` | Tailwind: a self-only Speed increase that always succeeds. |
| [Formula_58_Steel](../functions/Formula_58_Steel.md) | `0x140306044` | Steel: a self-only Brave increase that always succeeds. |
| [Formula_59_Shout](../functions/Formula_59_Shout.md) | `0x140306074` | Shout: a self-only combined Brave/PA/MA/Speed increase. |
| [Formula_60_Chant](../functions/Formula_60_Chant.md) | `0x14030609C` | Chant: the caster pays HP, the target heals twice that amount. |
| [Formula_61_MagicStatusOnly](../functions/Formula_61_MagicStatusOnly.md) | `0x140308A24` | Magic status-only: a magic hit check that applies a status with no damage. |
| [Formula_62_ReduceTo1HP](../functions/Formula_62_ReduceTo1HP.md) | `0x140308A44` | Reduce to 1 HP: sets the target's HP to 1 with no hit check or modifiers. |
| [Formula_63_AimedShotSpeedBased](../functions/Formula_63_AimedShotSpeedBased.md) | `0x140308A70` | Aimed Shot: a Speed-based hit check that inflicts a status. |
| [Formula_64_SealEvil](../functions/Formula_64_SealEvil.md) | `0x140308ABC` | Seal Evil: a Speed-based hit check that only affects undead targets. |
| [Formula_65_CelestialStasis](../functions/Formula_65_CelestialStasis.md) | `0x140308B24` | Celestial Stasis: a magic hit check that fails when caster and target share a zodiac sign. |
| [Formula_66_ConstructPhysical](../functions/Formula_66_ConstructPhysical.md) | `0x140308B7C` | Construct physical: a primary PA x Y hit plus a secondary PA x Y / X hit. |
| [Formula_67_MissingHPDamage](../functions/Formula_67_MissingHPDamage.md) | `0x1403060D8` | Missing HP damage: uses the caster's missing HP, with no hit check. |
| [Formula_68_CurrentMPDamage](../functions/Formula_68_CurrentMPDamage.md) | `0x1403060F8` | Current MP damage: deals damage equal to the target's current MP, with no hit check. |
| [Formula_69_MissingHPAlt](../functions/Formula_69_MissingHPAlt.md) | `0x140306114` | Missing HP (alternate): uses the target's missing HP, with no hit check. |
| [Formula_71_HPDrain](../functions/Formula_71_HPDrain.md) | `0x140308BEC` | % HP drain: percentage-of-max-HP damage that heals the caster, then a status. |
| [Formula_72_ItemRestoreHP](../functions/Formula_72_ItemRestoreHP.md) | `0x140308C30` | HP restore item: heals 10 x the item's amount byte (an Undead target takes it as damage). |
| [Formula_73_ItemRestoreMP](../functions/Formula_73_ItemRestoreMP.md) | `0x140306BD0` | MP restore item: restores 10 x the item's amount byte as MP. No hit roll, no Undead rule. |
| [Formula_74_ItemRestoreAll](../functions/Formula_74_ItemRestoreAll.md) | `0x140308C70` | Full restore item: HP healed = the target's max HP and MP healed = its max MP (an Undead target takes the max HP as damage). |
| [Formula_75_ItemRevive](../functions/Formula_75_ItemRevive.md) | `0x140308C98` | Revive item: on a target being revived, heals a random 1 to the item's amount byte; on an Undead target, damage equal to its current HP. |
| [Formula_76_MagicHealSimplified](../functions/Formula_76_MagicHealSimplified.md) | `0x140308D0C` | Magic heal (simplified): MA x Y healing with caster boost and Zodiac, then the undead check. |
| [Formula_77_PhysicalHPDrain](../functions/Formula_77_PhysicalHPDrain.md) | `0x140308D48` | Physical HP drain: a magic-style hit check then percentage-of-max-HP damage that heals the caster. |
| [Formula_78_MAYPhysicalFullChain](../functions/Formula_78_MAYPhysicalFullChain.md) | `0x140308DBC` | MA x Y physical: the full magic chain applied to a physical-style attack. |
| [Formula_79_PhysicalMissingHP](../functions/Formula_79_PhysicalMissingHP.md) | `0x140308DF4` | Physical plus missing HP: a physical evade check and magic chain, then damage equal to the caster's missing HP. |
| [Formula_80_PhysicalStatus](../functions/Formula_80_PhysicalStatus.md) | `0x140308E50` | Physical plus status: a physical evade check and magic chain, then a status through F56. |
| [Formula_81_MonsterBuffHealMagicHitStatus](../functions/Formula_81_MonsterBuffHealMagicHitStatus.md) | `0x140308E90` | Status with a magic chance: MA + X with the element boost, the caster's magic modifiers and zodiac (no Faith); on success the ability's status through Formula_56. |
| [Formula_82_SelfDestructHPBasedDamage](../functions/Formula_82_SelfDestructHPBasedDamage.md) | `0x140308EE4` | Self-destruct: HP-based damage, with a different value for self versus area targets. |
| [Formula_83_MonsterHPDamageMagicChain](../functions/Formula_83_MonsterHPDamageMagicChain.md) | `0x140308F28` | Monster % HP damage: a magic hit check then percentage-of-target-max-HP damage. |
| [Formula_84_MPRestorationMagicBased](../functions/Formula_84_MPRestorationMagicBased.md) | `0x140308FA0` | MP restoration: MA x Y MP healing with caster boost and Zodiac; always succeeds. |
| [Formula_85_PeckPhysicalHitPADrain](../functions/Formula_85_PeckPhysicalHitPADrain.md) | `0x140308FF8` | Peck: a magic hit that reduces the target's PA. |
| [Formula_86_BeamPhysicalHitMADrain](../functions/Formula_86_BeamPhysicalHitMADrain.md) | `0x14030902C` | Beam: a magic hit that reduces the target's MA. |
| [Formula_87_BequeathBaconSelfSacrifice](../functions/Formula_87_BequeathBaconSelfSacrifice.md) | `0x140309060` | Sacrifice: fills the target's HP and MP words with its own maximums, then, when the target is below level 99, turns the result into a stat change (flag word 0x80) and applies the ability's status to the caster. |
| [Formula_88_MalboroSporesMagicHitRecruitment](../functions/Formula_88_MalboroSporesMagicHitRecruitment.md) | `0x1403090F4` | Malboro Spores: a magic hit check that validates the target and sets the recruit/charm flag. |
| [Formula_89_LevelDrainPhysicalHitLevelSteal](../functions/Formula_89_LevelDrainPhysicalHitLevelSteal.md) | `0x14030918C` | Level Drain: a magic hit that sets the level-drain flag. |
| [Formula_90_DragonSCharmSpeciesGatedStatus](../functions/Formula_90_DragonSCharmSpeciesGatedStatus.md) | `0x1403091D8` | Dragon's Charm: a species-gated status with no hit check. |
| [Formula_91_DragonSGiftSpeciesGatedHPMPGift](../functions/Formula_91_DragonSGiftSpeciesGatedHPMPGift.md) | `0x140309214` | Dragon's Gift: a species-gated self-damage plus target heal. |
| [Formula_92_DragonSMightSpeciesGatedAllStatBoost](../functions/Formula_92_DragonSMightSpeciesGatedAllStatBoost.md) | `0x140309288` | Dragon's Might: a species-gated Brave/PA/MA/Speed boost. |
| [Formula_93_DragonSSpeedSpeciesGatedAllBuff](../functions/Formula_93_DragonSSpeedSpeciesGatedAllBuff.md) | `0x1403092D8` | Dragon's Speed: a species-gated all-buff. |
| [Formula_94_TriElementReDispatchesToF30](../functions/Formula_94_TriElementReDispatchesToF30.md) | `0x140307C10` | Tri-Element: shares the F30 target; the ability supplies the element and parameters. |
| [Formula_95_NanoflareReDispatchesToF30](../functions/Formula_95_NanoflareReDispatchesToF30.md) | `0x140307C10` | Nanoflare: shares the F30 target. |
| [Formula_96_MagicAveraged](../functions/Formula_96_MagicAveraged.md) | `0x140309310` | Averaged magic damage: A = MA, B = (MA + Y) / 2, then the magic damage tail (a thunk to Formula_MagicAvgDamage). |
| [Formula_97_MagicBasedBraveModify](../functions/Formula_97_MagicBasedBraveModify.md) | `0x140309318` | Magic-based Brave modify: a magic hit check that adjusts the target's Brave. |
| [Formula_98_PhysicalBasedBraveModify](../functions/Formula_98_PhysicalBasedBraveModify.md) | `0x14030934C` | Brave change with a magic roll that ignores Faith: the magic evade gate, then a MA + X chance; on a hit the target's Brave changes by Y. |
| [Formula_99_SpeedTimesWeaponPower](../functions/Formula_99_SpeedTimesWeaponPower.md) | `0x140309380` | Thrown weapon: damage = the caster's Speed x the weapon's WP through the physical modifiers; a target with the catch reaction may catch it on a Brave roll. |
| [Formula_AdjustEvadeForTargetStatus](../functions/Formula_AdjustEvadeForTargetStatus.md) | `0x14030573C` | Evade-setup step: clears the four evade bytes or halves the baseline byte according to status bits of the target. |
| [Formula_AdjustHitForTargetFlag](../functions/Formula_AdjustHitForTargetFlag.md) | `0x140305700` | Evade-setup step of the weapon formulas: halves the baseline byte and sets reaction 449 when the target meets two conditions. |
| [Formula_BardDancerGate](../functions/Formula_BardDancerGate.md) | `0x140304D5C` | The Bard and Dancer hit roll: scales the shown percent by X and rolls a miss against X. |
| [Formula_CasterMagMods](../functions/Formula_CasterMagMods.md) | `0x140305CB0` | The caster's magic damage modifiers: two passive bits scale A. |
| [Formula_CasterStatusMods](../functions/Formula_CasterStatusMods.md) | `0x140305D08` | The caster's status modifiers on A: Berserk raises it, Toad flattens it. |
| [Formula_ChanceRoll](../functions/Formula_ChanceRoll.md) | `0x140306408` | Turns R+6 (a chance in percent) into the shown hit percent and the roll that can make the action miss. |
| [Formula_ChanceSum](../functions/Formula_ChanceSum.md) | `0x140305F4C` | Builds a chance in percent in R+6: A plus the zodiac-adjusted B. |
| [Formula_CritRoll](../functions/Formula_CritRoll.md) | `0x140305EB4` | The 4 percent critical hit: marks R+1, adds a random share of A and runs the knockback calculation. |
| [Formula_DamageAB](../functions/Formula_DamageAB.md) | `0x140305F08` | The damage amount: R+6 = A * B capped at 0x7FFF, kind bit 0x80. |
| [Formula_DrainHP](../functions/Formula_DrainHP.md) | `0x1403062F0` | HP drain: the target takes the amount and the caster gets it, or the reverse when the target is Undead. |
| [Formula_DrainMP](../functions/Formula_DrainMP.md) | `0x1403063B8` | MP drain: the amount becomes MP damage on the target and an MP heal on the caster. |
| [Formula_DrawOutGate](../functions/Formula_DrawOutGate.md) | `0x14030655C` | The Draw Out katana break roll: writes the caster-side result with the broken-or-kept flag. |
| [Formula_EarthFloatAndAffinity](../functions/Formula_EarthFloatAndAffinity.md) | `0x1403061C8` | Float nullifies an earth hit, then the element affinity step runs with the ability's element. |
| [Formula_ElemBoostAction](../functions/Formula_ElemBoostAction.md) | `0x140305BE8` | Element boost from the ability's element: A = 5 * A / 4 when the caster's element mask has the ability record's element. |
| [Formula_ElemBoostWeapon](../functions/Formula_ElemBoostWeapon.md) | `0x140305BB8` | Element boost from the weapon's element: A = 5 * A / 4 when the caster's element mask has the weapon's element. |
| [Formula_ElementAffinity](../functions/Formula_ElementAffinity.md) | `0x140305554` | The target's element affinities applied to R+6: absorb, null, half, weak and the Oil double. |
| [Formula_EvadeByteRoll](../functions/Formula_EvadeByteRoll.md) | `0x140305130` | One evade roll of Formula_EvadeRoll: a failed hit stores the miss reason. |
| [Formula_EvadeRoll](../functions/Formula_EvadeRoll.md) | `0x14030588C` | The shared evade step of the physical and magic gates: scales the shown hit percent by the four evade bytes and rolls each of them. |
| [Formula_FaithScale](../functions/Formula_FaithScale.md) | `0x140306258` | Scales R+6 by the caster's and the target's faith: R+6 = R+6 * casterFaith * targetFaith / 10000. |
| [Formula_FinalizeAbsorb](../functions/Formula_FinalizeAbsorb.md) | `0x140306224` | Sets the kind bits of a damage result and turns an absorbed hit into a heal. |
| [Formula_HealSwap](../functions/Formula_HealSwap.md) | `0x140306378` | Turns the computed amount into a heal, or into damage when the target is Undead. |
| [Formula_KnockbackCalc](../functions/Formula_KnockbackCalc.md) | `0x140304DC0` | Works out the tile a hit target is knocked back to and queues it as a request. |
| [Formula_MagicAvgDamage](../functions/Formula_MagicAvgDamage.md) | `0x140306F9C` | Sets A = MA and B = (MA + Y) / 2, then jumps into the magic damage tail. |
| [Formula_MagicDamageTail](../functions/Formula_MagicDamageTail.md) | `0x140306F4C` | The tail of every stock magic damage formula: the magic modifier chain on A, the damage, the scene and affinity steps, and the status tail. |
| [Formula_MagicHitElem](../functions/Formula_MagicHitElem.md) | `0x140307028` | Magic hit chance with the element boost and the faith factor: sets A = MA and B = X, runs the magic modifier chain, then the chance roll. |
| [Formula_MagicHitNoElem](../functions/Formula_MagicHitNoElem.md) | `0x140306FCC` | Magic hit chance without the element boost: A = MA, B = X, then the magic modifier chain, the faith factor and the chance roll. |
| [Formula_MagicHitNoFaith](../functions/Formula_MagicHitNoFaith.md) | `0x140307088` | Magic hit chance without the faith factor: A = MA, B = X, then the element boost, the magic modifier chain and the chance roll. |
| [Formula_PhysAttackFull](../functions/Formula_PhysAttackFull.md) | `0x140306EF0` | The whole stock weapon attack as one unit (formulas 1 and 2): weapon stat, bonus, modifiers, critical, damage, affinity. |
| [Formula_PhysMods](../functions/Formula_PhysMods.md) | `0x140306E34` | The full physical modifier chain on A: attacker passives, then Berserk / Toad, the target's passives and statuses, and the zodiac step. |
| [Formula_PhysStatusHit](../functions/Formula_PhysStatusHit.md) | `0x1403070E4` | Physical status chance: runs the physical caster and target modifier chain on A, adds the zodiac step and rolls the chance. |
| [Formula_ReactionPrecheck](../functions/Formula_ReactionPrecheck.md) | `0x14030AF88` | Gate of the reaction-style handlers (Speechcraft, Throw): decides whether the reaction roll applies. |
| [Formula_RevivePrecheck](../functions/Formula_RevivePrecheck.md) | `0x140309504` | Revive gate: runs the status tail and continues only when a status is pending or the target is Undead. |
| [Formula_SceneVarElemMod](../functions/Formula_SceneVarElemMod.md) | `0x140306134` | Scene-variable element modifier on R+6: damage of some elements is cut or raised by the battle's scene variable 35. |
| [Formula_StatusChance19](../functions/Formula_StatusChance19.md) | `0x140306C10` | The chance that a status effect goes with a damage hit: a 19 percent roll (Nanoflare-style id 219 uses a MA difference) that sets R+18 bit 0x200. |
| [Formula_StatusTailKeepHit](../functions/Formula_StatusTailKeepHit.md) | `0x140306944` | Runs the status application on the inflict record and restores the hit fields it may have touched. |
| [Formula_StealGate](../functions/Formula_StealGate.md) | `0x14030647C` | The steal and break gate: turns the picked equipment into no effect when it is one of four protected ids or the target is protected. |
| [Formula_StealGilApply](../functions/Formula_StealGilApply.md) | `0x140305FA8` | Gil theft result: the caster gains and the target loses an amount from level, Speed and Y. |
| [Formula_TargetPassiveMag](../functions/Formula_TargetPassiveMag.md) | `0x140305D98` | The target's passive modifiers against a magic hit. |
| [Formula_TargetPassivePhys](../functions/Formula_TargetPassivePhys.md) | `0x140305D40` | The target's passive modifiers against a physical hit. |
| [Formula_TargetStatusMag](../functions/Formula_TargetStatusMag.md) | `0x140305E64` | The target's status modifiers against a magic hit. |
| [Formula_TargetStatusPhys](../functions/Formula_TargetStatusPhys.md) | `0x140305DF0` | The target's status modifiers against a physical hit. |
| [Formula_ZeroResult](../functions/Formula_ZeroResult.md) | `0x140305504` | The stock no-effect result: nothing happens and the reason is 5 (nullified). |
| [Formula_Zodiac](../functions/Formula_Zodiac.md) | `0x140305178` | The zodiac compatibility step on A: raises or lowers it by the pair of signs. |
| [Rng_Percent](../functions/Rng_Percent.md) | `0x140278E68` | Draws a battle random number and tells whether it reaches a threshold on a given scale. |
| [sub_1400FA94C](../functions/sub_1400FA94C.md) | `0x1400FA94C` | Fills an effect description (out) from a usable item's or an action's added-effect record. |
| [sub_1403055F0](../functions/sub_1403055F0.md) | `0x1403055F0` | Seeds the attack and defence bytes of the formula working area from the attacker's hands and accessory before a physical formula runs. |
| [sub_140305A48](../functions/sub_140305A48.md) | `0x140305A48` | Scales the working attack by a percentage tied to the equipped item category and stores the result as a 1/100 fraction. |
| [sub_140305C18](../functions/sub_140305C18.md) | `0x140305C18` | Applies the three multiplicative modifiers that follow the attack scale: a 4/3 step, a 3/2 step and a final halving. |
| [sub_1403064D8](../functions/sub_1403064D8.md) | `0x1403064D8` | The shared stat-sap effect: picks which stat byte the formula writes by the ability being resolved. |
| [sub_140306C90](../functions/sub_140306C90.md) | `0x140306C90` | Second half of the physical attack setup: it applies the attacker's state modifiers after the hands are read and returns whether the action may continue. |
| [sub_140306D70](../functions/sub_140306D70.md) | `0x140306D70` | Magic-side counterpart of the physical setup: it seeds the magic working bytes from the caster's hands and accessory. |

## Observed behaviours (1)

| Name | Scope | Summary |
|---|---|---|
| [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md) | engine (battle formulas) | Several shared formula handlers choose their effect by the ability id in the formula block's word +8, and the resolver tests a few single ids, so an ability id none of them lists takes the default branch (usually: no ... |
