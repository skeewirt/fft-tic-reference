# GUIComponentGauge_Step

- **Address:** `0x14040DEC4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `_UNKNOWN **GUIComponentGauge_Step(GUIComponentGauge *g)`
- **Callers:** GUIComponentGauge_Update
- **Callees:** GUINode_FindState, sub_14040E350, sub_14040E1B8, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

While the gauge value is animating (+688), eases three displayed fractions toward the target fraction using float tracks of the Increase / Decrease states, drives the GaugeBar / GaugeInc / GaugeDec states from them and posts the current value (event 37).

## Behavior

- V: runs only when g+688 != 0. settled = true; the three ease values (bar, inc, dec) default to 1.0. State 'Decrease' (+4872): when it exists and its +104 is set, the float track of its '#GaugeBar' (+5192) channel group gives the bar ease and the one of '#GaugeDec' (+5224) the dec ease (sub_14040E350 samples track index 4 of the group at the state's frame +80); settled = (state+105 == 0). State 'Increase' (+4856): same with '#GaugeBar' (overrides the bar ease) and '#GaugeInc' (+5208) for the inc ease; settled = false when state+105 is set.
- V: target = (float)(g+648 - g+656) / (float)(g+660 - g+656) (g+648 value, +656 min, +660 max). When settled: g+668 = g+676 = target and g+688 = 0 (animation finished). Otherwise g+668 = clamp((target - g+664) * barEase + g+664, 0, 1), g+676 = clamp((target - g+672) * incEase + g+672, 0, 1) and the third fraction clamp((target - g+680) * decEase + g+680, 0, 1).
- V: g+684 = the third fraction (target when settled); sub_14040E1B8(g, ...) then puts the GaugeBar (+4888), GaugeInc (+4904) and GaugeDec (+4920) states on the frames that match the fractions (each is enabled, hold +109 = 1, frame = clamp((1 - fraction) * state+88, 0, last), read from sub_14040E1B8 for the first; its float arguments come from registers the decompile hides).
- V: event {37, value} with value = (int)((float)(g+660 - g+656) * g+668 + (float)g+656) is posted to the owners.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentGauge_Update](GUIComponentGauge_Update.md)

## Notes

The name is ours (IDB: sub_14040DEC4). Data flow read from the decompile; the fraction pairs are (+664 -> +668, bar track), (+672 -> +676, inc track), (+680 -> +684, dec track). Calling +676 / +684 the increase / decrease ghosts is I from the state names. Not Job Tree related.

## Open questions

? what writes the base values +664 / +672 / +680 and sets +688 (the set-value function, not read). ? sub_14040E1B8's three float arguments.
