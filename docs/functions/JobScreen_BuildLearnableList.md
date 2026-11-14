# JobScreen_BuildLearnableList

- **Address:** `0x14028ACD8`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobScreen_BuildLearnableList(const void *job_record, int tab)`
- **Callers:** sub_1403351FC
- **Callees:** sub_14028668C, Job_IsHiddenFromTree, Job_BuildTabAbilityList, Job_IdToIndex, sub_1403609F0, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the ability list a job page shows with the learned flags applied, using the unit learned-bit reader and the job tab builder.

## Behavior

- V: it initialises a bit reader over the job record through sub_14028668C and keeps the resulting list in a stack buffer.
- V: the job id at record +3 is converted through Job_IdToIndex, and Job_IsHiddenFromTree decides whether the learned bits apply.
- V: Job_BuildTabAbilityList supplies the tab list, and the function then walks it to set the learned/learnable state.
- V: the reader pointer is stored at 0x143C49BF0 and the one-shot flag at 0x142FF3CA6 is set.
- V: it writes the pointer to the learned bits at 0x143C49BF0 so the following list consumers read the same bits.
- V: sub_1403609F0 and sub_14041FAE0 refresh the list gadget after the build.
- I: this is the list behind the Learn page, because the learned bits are the only state it adds to the tab list.
- ?: whether a job hidden from the tree gets an all-zero bit set or no learned bits at all; the branch was not followed.

## State touched

- Calls: [sub_14028668C](sub_14028668C.md), [Job_IsHiddenFromTree](Job_IsHiddenFromTree.md), [Job_BuildTabAbilityList](Job_BuildTabAbilityList.md), [Job_IdToIndex](Job_IdToIndex.md)

## Notes

Whole function read (287 bytes). The learned-bit pointer is the ptrmap site the X4 class study lists.

## Open questions

None recorded.
