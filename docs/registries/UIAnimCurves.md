# UIAnimCurves

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [UIAnim_Curve](../functions/UIAnim_Curve.md), [UIAnim_InterpToCurve](../functions/UIAnim_InterpToCurve.md)
- **Values stored in:** [KeyTrackKey.curve](../structs/KeyTrackKey.md#curve)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The easing curves of UI keyframes: curve id to blend function of the position t within a key interval (UIAnim_Curve). A UIB file stores the interpolation id n; the game uses curve n + 1 (UIAnim_InterpToCurve), so the file id of a curve is its id minus 1. Every curve is single precision. pi is the float 3.1415927; b(t) is the bounce-out curve (id 32); Bez(x1, y1, x2, y2; t) is a cubic Bezier from (0, 0) to (1, 1) with control points (x1, y1), (x2, y2), solved for x = t (5 bisection steps, then a linear blend of the bracket).

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="step"></a>1 | `Step` | `t < 1 ? 0 : 1` | V | Also the result for id 0 and any id above 39. |
| <a id="linear"></a>2 | `Linear` | `t` | V | Also the curve of any file id outside 0 to 35. |
| <a id="smoothstep"></a>3 | `Smoothstep` | `t*t*(3 - 2t)` | V |  |
| <a id="inquad"></a>4 | `InQuad` | `t*t` | V |  |
| <a id="outquad"></a>5 | `OutQuad` | `t*(2 - t)` | V | UnitJob CursorOver. |
| <a id="inoutquad"></a>6 | `InOutQuad` | `t < 0.5 ? 2t*t : 1 - 2(t-1)^2` | V |  |
| <a id="incubic"></a>7 | `InCubic` | `t^3` | V |  |
| <a id="outcubic"></a>8 | `OutCubic` | `1 + (t-1)^3` | V |  |
| <a id="inoutcubic"></a>9 | `InOutCubic` | `t < 0.5 ? 4t^3 : 1 + 4(t-1)^3` | V |  |
| <a id="inquart"></a>10 | `InQuart` | `t^4` | V |  |
| <a id="outquart"></a>11 | `OutQuart` | `1 - (1-t)^4` | V |  |
| <a id="inoutquart"></a>12 | `InOutQuart` | `t < 0.5 ? 8t^4 : 0.5 + 0.5(1 - (2-2t)^4)` | V |  |
| <a id="inquint"></a>13 | `InQuint` | `t^5` | V |  |
| <a id="outquint"></a>14 | `OutQuint` | `1 - (1-t)^5` | V |  |
| <a id="inoutquint"></a>15 | `InOutQuint` | `t < 0.5 ? 16t^5 : 0.5 + 0.5(1 - (2-2t)^5)` | V |  |
| <a id="inexpo"></a>16 | `InExpo` | `t > 0 ? 2^(10t-10) : 0` | V |  |
| <a id="outexpo"></a>17 | `OutExpo` | `t >= 1 ? 1 : 1 - 2^(-10t)` | V |  |
| <a id="inoutexpo"></a>18 | `InOutExpo` | `t <= 0: 0; t < 0.5: 2^(20t-11); t >= 1: 1; else 0.5 + 0.5(1 - 2^(-10(2t-1)))` | V |  |
| <a id="insine"></a>19 | `InSine` | `1 - cos((t*pi)*0.5)` | V | Second half of the glove's bob. |
| <a id="outsine"></a>20 | `OutSine` | `sin((t*pi)*0.5)` | V | First half of the glove's bob. |
| <a id="inoutsine"></a>21 | `InOutSine` | `(1 - cos(t*pi)) / 2` | V |  |
| <a id="incirc"></a>22 | `InCirc` | `1 - sqrt(1 - t*t)` | V |  |
| <a id="outcirc"></a>23 | `OutCirc` | `sqrt(1 - (t-1)^2)` | V |  |
| <a id="inoutcirc"></a>24 | `InOutCirc` | `t < 0.5 ? 0.5 - sqrt(0.25 - t*t) : 0.5 + sqrt(0.25 - (t-1)^2)` | V | sub_140402BB8. |
| <a id="inback"></a>25 | `InBack` | `t*t*((t-1)*2.70158 + 1)` | V |  |
| <a id="outback"></a>26 | `OutBack` | `(t-1)^2*(t*2.70158 - 1) + 1` | V |  |
| <a id="inoutback"></a>27 | `InOutBack` | `s = (t-0.5)*10.80632; t < 0.5 ? t*t*(s+2) : (t-1)^2*(s-2) + 1` | V | As coded (not the textbook in-out back). |
| <a id="inelastic"></a>28 | `InElastic` | `t <= 0: 0; t >= 1: 1; else (sin(4*pi*t)*1.70158 + 1) * 2^(10(t-1))` | V | sub_140402C14; the in-out variants use it as e(t). |
| <a id="outelastic"></a>29 | `OutElastic` | `1 - e(1 - t)` | V |  |
| <a id="inoutelastic"></a>30 | `InOutElastic` | `t < 0.5 ? 0.5*e(2t) : 0.5 + 0.5(1 - e(2 - 2t))` | V |  |
| <a id="inbounce"></a>31 | `InBounce` | `1 - b(1 - t)` | V |  |
| <a id="outbounce"></a>32 | `OutBounce` | `b(t): t < 0.36363637 ? 7.5625 t*t : t < 0.72727275 ? 7.5625 (t-0.54545456)^2 + 0.75 : t < 0.90909094 ? 7.5625 (t-0.8181818)^2 + 0.9375 : 7.5625 (t-0.95454544)^2 + 0.984375` | V | sub_140402CA0. |
| <a id="inoutbounce"></a>33 | `InOutBounce` | `t < 0.5 ? 0.5 - 0.5 b(1 - 2t) : 0.5 + 0.5 b(2t - 1)` | V |  |
| <a id="beziera"></a>34 | `BezierA` | `Bez(1, 0, 0.6666667, 1; t)` | V | Ids 34 to 39 are Bezier easings (sub_140402D38); t <= 0 gives 0 and t >= 1 gives 1. |
| <a id="bezierb"></a>35 | `BezierB` | `Bez(0.3333333, 0, 0, 1; t)` | V |  |
| <a id="bezierinoutab"></a>36 | `BezierInOutAB` | `t < 0.5 ? 0.5 Bez(1, 0, 0.6666667, 1; 2t) : 0.5 + 0.5 Bez(0.3333333, 0, 0, 1; 2t-1)` | V | The last id UIAnim_InterpToCurve returns (file id 35). |
| <a id="bezierc"></a>37 | `BezierC` | `Bez(1, 0, 0, 1; t)` | V | Ids 37 to 39 are in the evaluator but not reachable from a UIB file (UIAnim_InterpToCurve stops at 36). |
| <a id="beziercout"></a>38 | `BezierCOut` | `1 - Bez(1, 0, 0, 1; 1 - t)` | V |  |
| <a id="beziercinout"></a>39 | `BezierCInOut` | `t < 0.5 ? 0.5 Bez(1, 0, 0, 1; 2t) : 0.5 + 0.5(1 - Bez(1, 0, 0, 1; 2 - 2t))` | V |  |

## Behavior

- V: UIB interpolation id n maps to curve n + 1 for n = 0 .. 35 and to curve 2 otherwise (UIAnim_InterpToCurve).
- V (data): the Hand's Loop keys use file ids 19, 18 and 1: curves 20, 19 and 2.

## Referenced by

- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md)
- Read by: [UIAnim_Curve](../functions/UIAnim_Curve.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
