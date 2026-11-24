# GUIWidget_FindComponentById

- **Address:** `0x1403F9D18`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIWidget_FindComponentById(GUIWidget *w, NameKey *key)`
- **Callers:** GUIWidget_GetNodeScreenRect, sub_1402977C8, sub_140297990, sub_1403FAD88, sub_14040AEE8, sub_14040B128, sub_14040D298, sub_14040D48C, sub_14040DB1C (10 total)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Round-robin search of the widget's component vector for the component whose id (dword comp+8) equals the key's id (dword key+48); remembers where it found it.

## Behavior

- V: n = vector count (w+104..+112); empty -> 0. For k = 0..n-1: idx = (u32 w+280 + k) mod n; comp = vec[idx]; when comp+8 = key+48: w+280 = idx and return comp. None -> 0 (cursor unchanged).

## Referenced by

- Called by: [GUITabButton_Deselect](GUITabButton_Deselect.md), [GUITabButton_Select](GUITabButton_Select.md)

## Notes

The name is ours (IDB: sub_1403F9D18). 56 hits per 4 s. Same cursor trick as the by-name finder GUIWidget_FindComponentByName (cursor w+280), but keyed on an int id instead of the two string keys.

## Open questions

? What comp+8 is (I: component class / instance id).
