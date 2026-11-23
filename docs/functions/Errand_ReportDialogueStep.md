# Errand_ReportDialogueStep

- **Address:** `0x14036FD50`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Errand_ReportDialogueStep(int64_t record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 16)
- **Callees:** PackedBlock766_Load, sub_14019DF88, sub_14037085C, sub_1402D541C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the errand report dialogue (table index 16): shows the report, prints the result texts and closes through sub_14037085C.

## Behavior

- V: record dword 3 is the state: 1 reads the unit grid's result code (14 prints text id 47129, 15 prints none) and waits for the message and grid windows; 2 waits for the sound counter and then loads a packed block chosen by the grade (g_ErrandGrade high dword 1 or 2) from a byte table indexed by 0x140D49488 (+96 for grade 2).
- V: states 1 and 2 end by clearing dword 3 and calling sub_14037085C(0); any other state calls it at once.

## State touched

- Calls: [PackedBlock766_Load](PackedBlock766_Load.md)

## Open questions

None recorded.
