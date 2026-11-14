# FFT: The Ivalice Chronicles — Reference

Reverse-engineering reference for the Steam remaster of **FINAL FANTASY TACTICS: The Ivalice Chronicles** (`FFT_enhanced.exe`): functions, runtime structures, globals, registries, shaders, render targets, file formats, flows and observed behaviours, every fact tagged by how it was established.

2550 records in 12 kinds; 1783 functions.

## By kind

| Kind | Records | What it covers |
|---|---|---|
| [Functions](docs/functions/README.md) | 1783 | Code: one page per function of the game executable: what it does, whom it calls, and the state it reads and writes. |
| [Event opcodes](docs/opcodes/README.md) | 242 | The event script language: one flat data record per opcode (format: docs/guides/opcodes-format.md). Index page only; the records are the documentation. |
| [Structures](docs/structs/README.md) | 68 | Runtime records: objects and blocks the game keeps in memory, field by field, with who writes and who reads each field. |
| [Globals](docs/globals/README.md) | 190 | Global variables and singletons at fixed addresses of the current build (build-aware RVAs in symbols/globals.json). |
| [Registries](docs/registries/README.md) | 12 | Name-to-id tables the engine builds at runtime (sampler, texture and constant-buffer slots, ...): every entry with its id, its value and its meaning. |
| [Shaders](docs/shaders/README.md) | 9 | GPU shader programs from the game's technique files: stage, interface, bindings and what they compute (in words; no bytecode). |
| [Shader programs](docs/programs/README.md) | 4 | Engine shader programs: a selector and program index resolved to its vertex and pixel shader, and the passes that use it. |
| [Render targets](docs/render-targets/README.md) | 8 | GPU surfaces the renderer keeps by index: size, format and what each one holds at which point of the frame. |
| [File formats](docs/formats/README.md) | 16 | Layouts of the game's file formats (described, never copied): headers, records, string pools. |
| [Flows](docs/flows/README.md) | 22 | Ordered sequences across functions and state: what happens in which order (a frame, a render pass, a load), and why the order matters. |
| [Observed behaviours](docs/behaviors/README.md) | 136 | Behaviour of the engine, driver or GPU that no single function owns (conversion rules, ordering effects, inherited state), with the evidence. |
| [Tables](docs/tables/README.md) | 60 | Where the game keeps its data tables, NXD files and the fixed tables inside the executable: what each holds, how it is keyed, how big its rows are, and which code reads it. Describes the tables; it does not reproduce their contents. |

## By area

| Area | Contents |
|---|---|
| [Ability data](docs/areas/ability-data.md) | Functions: 6, Registries: 2, Flows: 1, Observed behaviours: 10, Tables: 3 |
| [Application and startup](docs/areas/app-startup.md) | Functions: 16, Structures: 1, Globals: 2, Observed behaviours: 2, Tables: 1 |
| [Battle](docs/areas/battle.md) | Functions: 251, Structures: 18, Globals: 42, Registries: 1, Flows: 3, Observed behaviours: 21, Tables: 14 |
| [Data access](docs/areas/data.md) | Functions: 54, Structures: 1, Globals: 2, Registries: 1, File formats: 6, Flows: 3, Observed behaviours: 5, Tables: 1 |
| [Display](docs/areas/display.md) | Functions: 3 |
| [Errands](docs/areas/errands.md) | Functions: 25, Structures: 1, Globals: 2, Observed behaviours: 3, Tables: 2 |
| [Event commands](docs/areas/event-commands.md) | Functions: 57 |
| [Event system](docs/areas/event-system.md) | Functions: 162, Structures: 1, Globals: 5, Observed behaviours: 3 |
| [Battle formulas](docs/areas/formulas.md) | Functions: 138, Observed behaviours: 1 |
| [Graphics](docs/areas/graphics.md) | Functions: 161, Structures: 9, Globals: 14, Registries: 3, Shaders: 9, Shader programs: 4, Render targets: 8, File formats: 2, Flows: 6, Observed behaviours: 39, Tables: 3 |
| [Input](docs/areas/input.md) | Functions: 15, Structures: 2, Globals: 1 |
| [Items and shops](docs/areas/items.md) | Functions: 95, Structures: 9, Globals: 29, Registries: 2, Flows: 1, Observed behaviours: 6, Tables: 14 |
| [Job data](docs/areas/job-data.md) | Functions: 35, Structures: 1, Globals: 1, Registries: 1, Flows: 1, Observed behaviours: 22, Tables: 3 |
| [Job list and unlock](docs/areas/job-list.md) | Functions: 21, Structures: 2 |
| [Job tree](docs/areas/job-tree.md) | Functions: 44, Structures: 3, Flows: 1, Observed behaviours: 7 |
| [Math](docs/areas/math.md) | Functions: 5 |
| [Resource](docs/areas/resource.md) | Functions: 27, Structures: 1 |
| [Save data](docs/areas/save-data.md) | Functions: 140, Structures: 3, Globals: 8, File formats: 6, Flows: 4, Observed behaviours: 4 |
| [UI framework](docs/areas/ui-framework.md) | Functions: 421, Structures: 12, Globals: 7, Registries: 1, File formats: 2, Flows: 1, Observed behaviours: 11 |
| [Unit data](docs/areas/unit-data.md) | Functions: 69, Structures: 4, Globals: 5, Registries: 1, Flows: 1, Observed behaviours: 2, Tables: 1 |
| [Unit rendering](docs/areas/unit-rendering.md) | Functions: 38 |

## How this repository is organised

- `kinds/` defines every object type (fields, references, index columns). Adding a type is adding one file there and one template; see [kinds/README.md](kinds/README.md).
- `templates/` holds the page template of each kind; `areas.json` maps records to area pages.
- `data/<kind>.jsonl` holds one record per object (the source of every page, for tools and AI readers); `docs/<kind>/` holds the pages, `docs/areas/` the area pages, `docs/guides/` the conventions and process.
- `symbols/` maps names to build-specific addresses (RVAs, sizes and hash fingerprints only).
- Every page and record is generated from the research notes; references between objects are links, and the reverse lists (called by, read by, written by, used in, ...) are computed, never typed by hand.

## Conventions

See [docs/guides/conventions.md](docs/guides/conventions.md). In short: **V** decoded from code or data or confirmed live, **M** measured, **I** inferred, **?** unknown; addresses are build-specific; names are project names, not official ones; analysis notes only, no machine code, decompiled text or original bytes.

## No game files / no affiliation

No game assets, binaries, machine-code excerpts or original executable bytes are included. You need your own legally purchased copy of the game to use these notes.

FINAL FANTASY TACTICS is a trademark of Square Enix. This project is not affiliated with or endorsed by Square Enix.

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). Share and adapt these notes for any purpose, including commercially, as long as you give attribution to the author (skeewirt), link the licence and say if you changed anything.

This repository holds original interpretation and notes only. It does not republish other people's content, and it contains no game code, game data or assets; the licence covers only the notes. Square Enix's game and its contents remain theirs.
