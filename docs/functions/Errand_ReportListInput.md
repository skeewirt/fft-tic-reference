# Errand_ReportListInput

- **Address:** `0x14036F94C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_ReportListInput(int64_t record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 14)
- **Callees:** Errand_ComputeRewards, HelpMessage_Open, sub_1402D541C, sub_1402EDB48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the list of errands with a report ready (table index 14): confirm computes the rewards and opens the report prompt (kind 15).

## Behavior

- V: cancel clears 0x140D49620 and 0x140D49624 and starts the close; the help action opens HelpMessage_Open(4193).
- V: confirm calls Errand_ComputeRewards for the errand number held at record + 52 + 4 x row, stores the cursor, sets text id 47130, builds a window and pushes kind 15 with that errand number in record dword 4.
- V: after the close it pops and re-opens the screen below.
- I: the list holds errands with a report ready, from the call of Errand_ComputeRewards.

## State touched

- Calls: [Errand_ComputeRewards](Errand_ComputeRewards.md), [HelpMessage_Open](HelpMessage_Open.md)

## Open questions

None recorded.
