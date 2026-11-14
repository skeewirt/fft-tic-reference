# GUILayerXform_MapPointInt

- **Address:** `0x1403F8CA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUILayerXform_MapPointInt(GUILayerXform *t, int pt[2])`
- **Callers:** sub_14040B828 (slider), sub_14013DED4
- **Callees:** sub_1403F8A20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps an integer point through the layer's 2x3 matrix (x' = x*m0 + y*m2 + m4, y' = x*m1 + y*m3 + m5) and rounds back to integers (roundf).

## Behavior

- V: the matrix is recomputed first when t+128 is set; core+216+144*layer holds the window-to-UI transforms.

## Open questions

None recorded.
