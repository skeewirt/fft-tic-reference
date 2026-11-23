# Errand_ProfitEndStep

- **Address:** `0x1402D35F8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Errand_ProfitEndStep(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 55)
- **Callees:** EventVar_Read, Errand_TreasureMilestone, sub_1400DF354, UIGuide_Show, sub_14033FDAC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the errand end sequence (table index 55): waits, sends the profit-end notification and goes through a short prompt.

## Behavior

- V: record dword 2 is the state: default waits for sub_1400FC794(0) and calls sub_1402D34D4; 1 waits for the loading flag dword 0x14184B208, queues music 532 and sub_14033FDAC(3, 16), counts the errand flag variables 864 to 959 with mask 0x4 set and sends a ProfitEndNotification to the achievement object with the errand grade, the count and Errand_TreasureMilestone, then goes to state 2.
- V: state 2 counts frames in dword 3 and at 180 queues sub_14033FDAC(2, 16), (1, 547) and (3, 16) and goes to state 3.
- V: state 3 shows a guide (UIGuide_Show with id 7021) when a field of the widget is 20 and sub_1400EB79C() is 0, reads the widget result: 4 pops and calls sub_140370EDC, 21 copies dword 4 to dword 3 and clears the prompt.
- I: it ends by returning to the errand board.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [Errand_TreasureMilestone](Errand_TreasureMilestone.md), [UIGuide_Show](UIGuide_Show.md), [sub_14033FDAC](sub_14033FDAC.md)

## Open questions

None recorded.
