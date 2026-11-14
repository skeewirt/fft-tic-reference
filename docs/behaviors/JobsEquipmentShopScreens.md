# JobsEquipmentShopScreens

- **Kind:** observed behaviour
- **Scope:** Units > Status, Jobs, equipment list, Outfitter (Buy)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUICore_GetFocus](../functions/GUICore_GetFocus.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Screen identities, cell layouts and the memory handles (job byte, item id, gil) of the world map management screens, as seen live.

## Behavior

- V (live, 2026-11-05): world map Y opens the roster (ffto_unit_chara_ver02.uib, about 3 s with an empty focus), A opens Status (ffto_status_ver03.uib, glove on Equipment & Abilities at 117,450), DOWN reaches Job (117,626); A on Job opens the Jobs grid (ffto_jobchange_ver03.uib), X there opens the Job Tree (ffto_job_tree.uib); B steps back one screen each. X on the map opens worldmap_base_info.uib; A on a settlement opens the town menu (worldmap_top_layer.uib).
- V (live): Jobs grid cells are title text nodes 184 wide, 270 px apart horizontally and 202 px vertically; the glove sits at (+19, -22) from a cell's text; the grid scrolls. A on a cell opens a horizontal small menu anchored to the cell: Learn Abilities, then Change Job 284 px to the right. A on Change Job shows 'Job changed to <name>!' with a Close button; A on Close returns to Status.
- V (live): a unit's job byte is at save-unit +2 (Squire 0x01, Chemist 0x4B); it changes the moment Change Job is confirmed.
- V (live): on Status, A on Equipment & Abilities moves the glove into the right panel (first slot = right hand at 272,557); A on a slot opens its item list (ffto_equip_ver03.uib, heading 'Equippable Weapons'), cells are NameEquip nodes 68 px apart with the glove at (-112, +22); A on an item equips it and stays on the list. The right-hand item id is the u16 at save-unit +0x14 (Broadsword 19); the list depends on the job.
- V (live): Outfitter: ffto_shop_top_ver02.uib (Buy / Sell / Fitting), Buy list ffto_shop_ver02.uib (same NameEquip cells, TextPrice next to each), A on an item opens the amount selector (glove about 1461,512), A opens ffto_shop_confirm_ver02.uib (Total Price, Buy and Equip / Cancel), A buys: gil (event variable 44) dropped by exactly the price (200 for a Broadsword). After a purchase the screen has no focus until B returns to the list.

## Notes

Cell positions are node offsets summed down the widget tree; the debugger's `pick` command uses them.

## Open questions

? The slot offsets of the other four equipment slots. ? Sell, Fitting (Try Then Buy), the Tavern and Warriors' Guild.
