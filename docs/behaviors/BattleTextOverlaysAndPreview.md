# BattleTextOverlaysAndPreview

- **Kind:** observed behaviour
- **Scope:** battle: event dialogue, notice banner, attack / item preview, deployment placement
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUICore_GetFocus](../functions/GUICore_GetFocus.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where the battle's dialogue, notices and action preview are drawn, how placement works, and what the preview numbers meant in play, as seen live.

## Behavior

- V (live, 2026-11-08, Siedge Weald): event dialogue is drawn in ffto_event.uib, which never takes the focus (the sortie screen keeps it through the battle opening): node Title holds the speaker, node Text the line. Two balloons can be drawn at once (the previous one stays while the next opens); A advances one box, with a moment between boxes where none is drawn.
- V (live): the red notice banner is ffto_common_error.uib, node Title, also never focused; it read 'Unable to use. The unit either lacks any usable abilities or does not meet their requirements.' when a Monk with no learned Martial Arts chose that command, and faded within a few seconds while the list stayed closed.
- V (live): the action preview (ffto_battle_main_ver04.uib) has node TextHit = hit chance, TextDamage = the damage, or the recovery for an item, TextHPNum = actor and target HP, and a second percentage in node Textmatch. Nine previews in one battle matched the result exactly when the action landed; a Potion's 'Recovery 30' was capped at the target's max HP (41/53 to 53, 24/51 to 51).
- V (live): the hit chance depends on the side attacked from: a Bomb facing -y (unit +0x51 = 0) showed 80 % from its front tile and 100 % from its side tile; the 80 % attack missed, the side attack landed. Earlier front attacks showed 62 % and 82 %.
- I (live): Textmatch varied by attacker and target pair (75 % for a Knight against a Black Goblin and 100 % against a Bomb; 75 % for a Monk against a Goblin and a Bomb), which fits a zodiac compatibility figure; not checked against the zodiac table.
- V (live): a Chemist's Potion can target any tile within 4 (a full diamond of radius 4).
- V (live): deployment: after a unit is placed, the tile cursor moves to a free tile by itself and the unit carousel opens on the next unit not yet placed; placing the last free member opens 'Commence battle? Yes / No' by itself. From the second placement on, the sortie screen holds the focus with no glove; before the first it has no focus.
- V (live): A on a battleground first shows the location's name on black while the battle loads; units are already in the battle table, no unit has the turn (slot 0xFFFFFFFF); deployment follows by itself.
- V (live): the footer (ffto_footer_02.uib) keeps hidden labels of the previous footer in its tree (e.g. 'Commence Battle' through the first turns): only labels visible up their node chain are on screen. While an action of the player's side plays, the footer is hidden.
- V (live): the camera turns by itself between turns and phases (yaws 0x200, 0x600, 0xA00, 0xE00 seen), and pad directions for the tile cursor and the facing prompt follow it.

## Notes

The preview and dialogue layouts are the game's own. Read with the project debugger (state reads and the UI text scanner).

## Open questions

? What Textmatch is exactly (zodiac compatibility suspected). ? Whether the hit chance from the back differs from the side.
