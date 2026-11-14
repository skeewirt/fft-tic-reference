# FFT: The Ivalice Chronicles — Reference

Reverse-engineering reference for the Steam remaster of **FINAL FANTASY TACTICS: The Ivalice Chronicles** (`FFT_enhanced.exe`): functions, runtime structures, globals, registries, shaders, render targets, file formats, flows and observed behaviours, every fact tagged by how it was established.

{{totals}}

## By kind

{{kinds_table}}

## By area

{{areas_table}}

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
