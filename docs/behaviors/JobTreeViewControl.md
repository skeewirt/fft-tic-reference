# JobTreeViewControl

- **Kind:** observed behaviour
- **Scope:** what a smooth stick scroll and a zoom of the Job Tree can use
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [GUINode_SetPosition](../functions/GUINode_SetPosition.md), [GUINode_SetScale](../functions/GUINode_SetScale.md), [GUINode_BuildLocalMatrix](../functions/GUINode_BuildLocalMatrix.md), [GUINode_UpdateColourAndMatrix](../functions/GUINode_UpdateColourAndMatrix.md), [GUIWidget_GetNodeScreenRect](../functions/GUIWidget_GetNodeScreenRect.md), [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [ListScroll_HandleStick](../functions/ListScroll_HandleStick.md), [ListScroll_Step](../functions/ListScroll_Step.md), [FreeCursor_StepFromSticks](../functions/FreeCursor_StepFromSticks.md), [Pad_ReadSticks](../functions/Pad_ReadSticks.md), [JobTree_HandleInput](../functions/JobTree_HandleInput.md), [JobScreenFrame](../flows/JobScreenFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The tree root is one node; its position (scroll) and scale are plain integer / float fields whose change reaches every panel, arrow, label and the finger cursor's target in the same UI pass. The game has a stick-scroll pattern for lists that keeps the cursor where it is until it leaves the view. Nothing in the tree reads a stick.

## Behavior

- V: scale is stored at node +80 / +84 (GUINode_SetScale) and enters the node's local matrix about the pivot; a child's matrix is its local matrix times the parent's, and the accumulated scale is kept at +184 / +188 (GUINode_UpdateColourAndMatrix). A scale on the root therefore scales every descendant that is drawn through these matrices; the root's pivot is (960, 540), so a zoom is about the screen centre.
- V: the finger cursor's target is GUIWidget_GetNodeScreenRect of the focused panel node: its corners go through the node's matrix and every ancestor's. A moved or scaled root is followed by the glove with no extra code (the glove glides toward the new target, 40 percent of the gap per UI frame), but the rect is rounded to integers.
- I: mouse hit tests (GUIWidget_HitTestPoint -> HitTestChildren, GUINode_ComputeRectInMatrix) rectangle-test each node through the accumulated matrix, so a scaled root should hit-test scaled; not seen live.
- V: the tree widget's own stock scroll is absent.
- V: the game's pattern for stick scrolling with a focused item is ListScroll_HandleStick / ListScroll_Step: the right stick scrolls the list whole rows at a time and the focus is only moved (to the first or last visible item) when the focused item has left the view; the free pointer of FreeCursor_StepFromSticks moves axis x frame time x 10 px.
- V: the unused controls on this screen are both sticks, both triggers and the stick clicks (no reader); LB / RB are the unit switch of the job list but not read by the tree.
- V (live): the footer is another widget and stays when the tree root moves; the 'Job Tree' title and the floor are part of the root and scroll with it.
- V (live 2026-11-10, uitree): the tree's moved and scaled node is the widget's root node ('Widget', kind 1); its child 'JobTree' is a reference node (kind 12, position 0, scale 1) whose component object is at node +304; that component's own node (+0x110) has the children LayerRoot (panels and arrows, at (0, 32)), MainTab (title band), BG (the floor plate, at (185, 0), pivot = its size / 2) and BGBlur (hidden). A node's name key at +16 resolves through the interned name table at 0x143CDA2A0 (bucket = low 16 bits, 1-based, 32 bytes each, entry vector at +16 / +24 of 16-byte entries, the first word the name); children chain from +208 through the sibling at +32.
- ?: clipping: nothing found that clips the tree widget to a rectangle other than the screen; a component has an optional clip-rectangle effect group (comp +216, ComponentEffects_Collect) that the tree does not enable (not checked per component).

## Open questions

? live: set the root scale to 0.75 through gamecall (GUINode_SetScale on the root) and look at the picture, the glove and a mouse hover; ? the footer and title bands that a clamp should keep clear.
