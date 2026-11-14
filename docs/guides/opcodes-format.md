# Opcode records: format and rules

**This is how opcodes are documented. Do not write per-opcode prose pages.**

The event interpreter (`EventScript_Run`) handles about 170 opcodes. Opcode knowledge is kept as **data**, one flat JSON record per opcode, because the main reader is an AI that filters and cross-references it. Function sheets (`docs/functions/`) stay the place for how a *function* works; this file is the place for what an *opcode* is.


## Record fields (schema 1)

One JSON object per line, UTF-8, LF line endings, keys in this order. Every field is always present. **Unknown is `null`, never a guess.**

| Field | Type | Meaning |
|---|---|---|
| `op` | string | Opcode byte as `"0xNN"` (uppercase hex, two digits). Unique. |
| `name` | string or null | Project name in PascalCase, chosen from verified behavior. Null until verified. |
| `operand_bytes` | int or null | Operand bytes after the opcode byte, original (classic) rule. Null for variable length. |
| `operand_bytes_enhanced` | int or null | Same under the enhanced-edition rule (differs for 0x10, 0x51, 0xEB). |
| `variable_length` | bool | True when the length is read from the instruction itself (opcode 0xE6). |
| `operands` | list | One object per decoded operand: `{"at": int, "size": int, "type": "u8"/"u16"/"u32"/"var"/..., "meaning": string or null}`. `at` is the byte offset after the opcode byte, starting at 1. Empty list when nothing is decoded. |
| `effect` | string or null | One short factual sentence. No code, no bytes. |
| `blocks` | string or null | What the instruction waits for: `"frames"`, `"task"`, `"input"`, `"message"`, or null when it does not wait or is unknown. |
| `starts_task` | string or null | Name of the task body function it starts, if any. |
| `reads_vars` | list of strings | Variable references it reads, e.g. `"operand@3:u16"` or `"var 39"`. |
| `writes_vars` | list of strings | Same, for writes. |
| `calls` | list of strings | Sheet-named functions it calls, e.g. `"SceneVar_Alu"`. Only names that have a function sheet. |
| `explicit_case` | bool | True when the interpreter has a case label or comparison for this opcode. False only means none was found by that scan, **not** that the opcode is unhandled. |
| `where` | string or null | Function that handles it, e.g. `"EventScript_Run"`. Null when no handler has been located. |
| `conf` | string | `"V"` verified, `"I"` inferred, `"?"` unknown. Applies to `name`, `effect` and `operands` together. |
| `evidence` | list of strings | Pointers a reader can re-check, e.g. `"EventScript_InstructionLength"`. Never code. Required when `conf` is `V` or `I`. |
| `build` | string | Build the record was verified on, e.g. `"sha256:937233f7"`. |

## Rules

1. **Source is the game, not another project.** Every `V` fact comes from the current build's code. Other projects' notes may point at where to look; they are not evidence and are never copied (their licenses differ from ours).
2. **A record with `conf: "?"` is allowed and expected.** Length and `explicit_case` can be verified without knowing what the opcode does. Fill the rest when it is verified.
3. **No prose beyond `effect`.** One sentence, plain facts. Anything longer belongs on a function sheet.
4. **No code, bytes, instruction text or private paths** in any field. The audit checks this.
5. **Enums are exact.** `conf` and `blocks` use only the values above.
6. **Names are ours.** Chosen from verified behavior, PascalCase, no community-name guessing. Rename freely; ids (`op`) never change.
7. **When an opcode is verified,** update `opcodes_source.py`, regenerate, audit, then commit and push both repos like any function sheet.
8. **Cross-reference by name.** `calls` and `starts_task` use function-sheet names so a reader can jump to the sheet; each name must exist in the symbol map.
9. **Run-time facts stay on the sheets.** Variable layouts, task tables and the length rule are documented on `EventVar_*`, `SceneVar_*`, `EventScript_InstructionLength` and friends; records point to them.

## Reading it efficiently

`docs/opcodes.md` is a one-line-per-opcode index (op, name, operand bytes, short effect). Load it for orientation, then read `data/opcodes.jsonl` records for details. Filters such as "every opcode that starts a task" or "every opcode that writes a variable" are simple field tests on the data file.
