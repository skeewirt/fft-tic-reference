# ItemClassNumbers

- **Kind:** registry
- **Area:** [Items and shops](../areas/items.md)
- **Values stored in:** [ItemCategories](ItemCategories.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item class numbers (item class n is allowed to a job when bit 7 - n % 8 of byte n / 8 of its exe.job equip_flags is set; the class is the equip_category of the item's exe.item row) with their names.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="unarmed"></a>0 | `Unarmed` | `class 0` | V | Bare hands; the bit solved over the stock job rows. |
| <a id="knife"></a>1 | `Knife` | `class 1` | V | Solved from the stock job rows (one bit explains every job that lists the name). |
| <a id="ninjablade"></a>2 | `NinjaBlade` | `class 2` | V | As above. |
| <a id="sword"></a>3 | `Sword` | `class 3` | V | As above. |
| <a id="knightsword"></a>4 | `KnightSword` | `class 4` | V | As above. |
| <a id="katana"></a>5 | `Katana` | `class 5` | V | As above. |
| <a id="axe"></a>6 | `Axe` | `class 6` | V | As above. |
| <a id="rod"></a>7 | `Rod` | `class 7` | V | As above. |
| <a id="staff"></a>8 | `Staff` | `class 8` | V | As above. |
| <a id="flail"></a>9 | `Flail` | `class 9` | V | As above. |
| <a id="gun"></a>10 | `Gun` | `class 10` | V | As above. |
| <a id="crossbow"></a>11 | `Crossbow` | `class 11` | V | As above. |
| <a id="bow"></a>12 | `Bow` | `class 12` | V | As above. |
| <a id="instrument"></a>13 | `Instrument` | `class 13` | V | As above. |
| <a id="book"></a>14 | `Book` | `class 14` | V | As above. |
| <a id="polearm"></a>15 | `Polearm` | `class 15` | V | As above. |
| <a id="pole"></a>16 | `Pole` | `class 16` | V | As above. |
| <a id="bag"></a>17 | `Bag` | `class 17` | V | As above. |
| <a id="cloth"></a>18 | `Cloth` | `class 18` | V | Stock items of this class: Damask Cloth, Cashmere, Wyrmweave Silk (equip_category 18). |
| <a id="shield"></a>19 | `Shield` | `class 19` | V | Items: Escutcheon, Buckler, round and metal shields (equip_category 19). |
| <a id="helmet"></a>20 | `Helmet` | `class 20` | V | Items: Leather Helm, Bronze Helm, Iron Helm (equip_category 20). |
| <a id="hat"></a>21 | `Hat` | `class 21` | V | Items: Leather Cap, Plumed Hat, Red Hood (equip_category 21). |
| <a id="hairadornment"></a>22 | `HairAdornment` | `class 22` | V | Items: Hairband, Barrette, Ribbon (equip_category 22). |
| <a id="armor"></a>23 | `Armor` | `class 23` | V | Items: Leather Armor, Linen Cuirass, Bronze Armor (equip_category 23). |
| <a id="clothing"></a>24 | `Clothing` | `class 24` | V | Items: Clothing, Leather Clothing, Ringmail (equip_category 24). |
| <a id="robe"></a>25 | `Robe` | `class 25` | V | Items: Hempen Robe, Silken Robe (equip_category 25). |
| <a id="shoes"></a>26 | `Shoes` | `class 26` | V | Items: Battle Boots, Spiked Boots (equip_category 26). |
| <a id="armguard"></a>27 | `Armguard` | `class 27` | V | Items: Power Gauntlets, Genji Gloves, Bracers (equip_category 27). |
| <a id="ring"></a>28 | `Ring` | `class 28` | V | Items: Reflect Ring, Protect Ring, Angel Ring (equip_category 28). |
| <a id="armlet"></a>29 | `Armlet` | `class 29` | V | Items: Diamond Bracelet, Jade Armlet, Japa Mala (equip_category 29). |
| <a id="cloak"></a>30 | `Cloak` | `class 30` | V | Items: Shoulder Cape, Leather Cloak, Elven Cloak (equip_category 30). |
| <a id="perfume"></a>31 | `Perfume` | `class 31` | V | Items: Chantage and the other perfumes (equip_category 31). |
| <a id="fellsword"></a>35 | `FellSword` | `class 35` | V | Appears in stock job rows; the solve fixes the bit (no stock item has this class). |
| <a id="liprouge"></a>36 | `LipRouge` | `class 36` | V | Appears in stock job rows; the solve fixes the bit (no stock item has this class). |

## Behavior

- V: the names of classes 18..31 were checked a second way against the stock item names per equip_category; the groups that always co-occur in the stock job rows (Armguard / Cloak / Shoes, HairAdornment / Perfume, Armlet / Ring) are separated by that item check.
- V: the Dragoon's list (Perfume, Cloak, Armlet, Ring, Armguard, Shoes, Robe, Armor, HairAdornment, Helmet, Shield, Polearm, Unarmed) reproduces the stock row byte for byte.

## Open questions

? Classes 32..34 and 37..39 have no name and no stock user.
