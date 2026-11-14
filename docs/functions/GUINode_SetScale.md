# GUINode_SetScale

- **Address:** `0x1403EF738`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_SetScale(GUINode *node, float sx, float sy)`
- **Callers:** GUINode_ApplyAnimChannels (scale track), about 12 screen routines (sub_1400FD238, sub_140106C54, sub_140127544, sub_1401389C4, sub_14013ABCC, sub_140157580, sub_140159E1C, sub_14015CF00, sub_140161F80 and more)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a node's scale pair (+80 / +84, floats); the node is marked dirty when either value changed by more than 1.19e-7.

## Behavior

- V: when |node+80 - sx| or |node+84 - sy| exceeds 1.1920929e-7 both are stored and the dirty byte node+149 is set; nothing else is touched.
- V: a dirty node rebuilds its matrix in GUINode_UpdateColourAndMatrix and GUINode_UpdateSubtree dirties every child, so the scale reaches the whole subtree on the next UI pass (the scale acts about the node's pivot, GUINode_BuildLocalMatrix).
- V: callers outside the animation sampler exist in about a dozen screen routines (cross references of the function), so game code scales nodes directly as well as through authored scale tracks.

## Referenced by

- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_1403EF738). A zoom of the Job Tree would be this call on the tree root node (pivot 960, 540); the matrices below it follow (GUINode_UpdateColourAndMatrix multiplies each child by the parent's matrix and accumulates the scale at +184 / +188).

## Open questions

None recorded.
