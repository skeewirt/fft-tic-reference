# NxdDataRouteRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.route table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | V | Read in the code: Name of the route used to build its UI names: the file 'ui/ffto/worldmap/wm_route_<name>.uib' (UIAddon row 138) and the map states 'Show_R_<name>', 'Hide_R_<name>', 'R_<name>_Color_Default', 'R_<name>_Color_Grayout'. Observed in the stock rows: 51 distinct values, 0 empty. |
| <a id="town"></a>`0x8` | town | `int32` | V | Read in the code: Town (table 52) key of the route's first end point: the route grows from it, and it is one of the two points marked when the route is listed as closed. Observed in the stock rows: 0 to 42, 37 distinct values. |
| <a id="town_2"></a>`0xC` | town_2 | `int32` | V | Read in the code: Town key of the route's second end point (where the route grows to, unless reversed). Observed in the stock rows: 0 to 46, 42 distinct values. |
| <a id="state_suffix"></a>`0x10` | state_suffix | `string (int32 offset)` | V | Read in the code: Suffix of the state names the route-grow effect plays ('Show<suffix>' / 'Hide<suffix>' instead of 'Show' / 'Hide') when the route grows forward; empty = plain names. Observed in the stock rows: 6 distinct values, 46 empty. |
| <a id="state_suffix_2"></a>`0x14` | state_suffix_2 | `string (int32 offset)` | V | Read in the code: The same suffix used when the route grows reversed. Observed in the stock rows: 6 distinct values, 46 empty. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataRoute](../tables/NxdDataRoute.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 7 columns not decoded.
