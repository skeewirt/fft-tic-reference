# FFT: The Ivalice Chronicles — Reference

Reverse-engineering reference for the Steam remaster of **FINAL FANTASY TACTICS: The Ivalice Chronicles** (`FFT_enhanced.exe`): functions, runtime structures, globals, registries, shaders, render targets, file formats, flows and observed behaviours, every fact tagged by how it was established.

4311 records in 12 kinds; 2277 functions.

## By kind

| Kind | Records | What it covers |
|---|---|---|
| [Functions](docs/functions/README.md) | 2277 | Code: one page per function of the game executable: what it does, whom it calls, and the state it reads and writes. |
| [Event opcodes](docs/opcodes/README.md) | 242 | The event script language: one flat data record per opcode (format: docs/guides/opcodes-format.md). Index page only; the records are the documentation. |
| [Structures](docs/structs/README.md) | 535 | Runtime records: objects and blocks the game keeps in memory, field by field, with who writes and who reads each field. |
| [Globals](docs/globals/README.md) | 222 | Global variables and singletons at fixed addresses of the current build (build-aware RVAs in symbols/globals.json). |
| [Registries](docs/registries/README.md) | 30 | Name-to-id tables the engine builds at runtime (sampler, texture and constant-buffer slots, ...): every entry with its id, its value and its meaning. |
| [Shaders](docs/shaders/README.md) | 9 | GPU shader programs from the game's technique files: stage, interface, bindings and what they compute (in words; no bytecode). |
| [Shader programs](docs/programs/README.md) | 4 | Engine shader programs: a selector and program index resolved to its vertex and pixel shader, and the passes that use it. |
| [Render targets](docs/render-targets/README.md) | 8 | GPU surfaces the renderer keeps by index: size, format and what each one holds at which point of the frame. |
| [File formats](docs/formats/README.md) | 20 | Layouts of the game's file formats (described, never copied): headers, records, string pools. |
| [Flows](docs/flows/README.md) | 30 | Ordered sequences across functions and state: what happens in which order (a frame, a render pass, a load), and why the order matters. |
| [Observed behaviours](docs/behaviors/README.md) | 261 | Behaviour of the engine, driver or GPU that no single function owns (conversion rules, ordering effects, inherited state), with the evidence. |
| [Tables](docs/tables/README.md) | 673 | Where the game keeps its data tables, NXD files and the fixed tables inside the executable: what each holds, how it is keyed, how big its rows are, and which code reads it. Describes the tables; it does not reproduce their contents. |

## By area

| Area | Contents |
|---|---|
| [Ability data](docs/areas/ability-data.md) | Functions: 6, Structures: 12, Registries: 2, Flows: 1, Observed behaviours: 7, Tables: 14 |
| [Application and startup](docs/areas/app-startup.md) | Functions: 19, Structures: 3, Globals: 2, Observed behaviours: 5, Tables: 2 |
| [Battle](docs/areas/battle.md) | Functions: 386, Structures: 70, Globals: 50, Registries: 2, File formats: 1, Flows: 6, Observed behaviours: 68, Tables: 89 |
| [Data access](docs/areas/data.md) | Functions: 60, Structures: 112, Globals: 2, Registries: 3, File formats: 5, Flows: 3, Observed behaviours: 13, Tables: 116 |
| [Display](docs/areas/display.md) | Functions: 3, Structures: 5, Tables: 5 |
| [Errands](docs/areas/errands.md) | Functions: 29, Structures: 10, Globals: 2, Observed behaviours: 3, Tables: 11 |
| [Event commands](docs/areas/event-commands.md) | Functions: 57 |
| [Event system](docs/areas/event-system.md) | Functions: 203, Structures: 28, Globals: 5, File formats: 1, Observed behaviours: 20, Tables: 29 |
| [Battle formulas](docs/areas/formulas.md) | Functions: 151, Observed behaviours: 1 |
| [Graphics](docs/areas/graphics.md) | Functions: 173, Structures: 53, Globals: 14, Registries: 3, Shaders: 9, Shader programs: 4, Render targets: 8, File formats: 2, Flows: 6, Observed behaviours: 53, Tables: 48 |
| [Input](docs/areas/input.md) | Functions: 23, Structures: 12, Globals: 1, Registries: 2, Flows: 1, Observed behaviours: 1, Tables: 9 |
| [Items and shops](docs/areas/items.md) | Functions: 106, Structures: 28, Globals: 29, Registries: 2, Flows: 2, Observed behaviours: 12, Tables: 33 |
| [Job data](docs/areas/job-data.md) | Functions: 38, Structures: 15, Globals: 2, Registries: 1, Flows: 1, Observed behaviours: 28, Tables: 15 |
| [Job list and unlock](docs/areas/job-list.md) | Functions: 21, Structures: 2 |
| [Job tree](docs/areas/job-tree.md) | Functions: 45, Structures: 4, Flows: 1, Observed behaviours: 7 |
| [Math](docs/areas/math.md) | Functions: 5, Structures: 5, Tables: 6 |
| [Resource](docs/areas/resource.md) | Functions: 36, Structures: 7, Observed behaviours: 1, Tables: 15 |
| [Save data](docs/areas/save-data.md) | Functions: 138, Structures: 13, Globals: 8, File formats: 4, Flows: 3, Observed behaviours: 5, Tables: 10 |
| [UI framework](docs/areas/ui-framework.md) | Functions: 663, Structures: 134, Globals: 8, Registries: 12, File formats: 7, Flows: 6, Observed behaviours: 30, Tables: 234 |
| [Unit data](docs/areas/unit-data.md) | Functions: 76, Structures: 4, Globals: 6, Registries: 3, Observed behaviours: 6, Tables: 1 |
| [Unit rendering](docs/areas/unit-rendering.md) | Functions: 39, Structures: 18, Observed behaviours: 1, Tables: 20 |

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
