# Conventions

## Confidence tags

Every behaviour bullet, member row, note and open question carries one tag.

- **V** decoded: read from the game's code or data (decompilation, disassembly, the file format), or confirmed by a
  live read-only memory read, a trace or a GPU capture. Name the basis when it matters, for example
  `V (live read 2026-10-30)` or `V (mid-frame capture)`.
- **M** measured: fitted or observed on captures or by sampling. A number, not a rule; it stays open until a decoded
  rule replaces it. Name the evidence.
- **I** inferred: reasoning from field order, names, neighbouring code or behaviour; not read directly. Say what the
  inference rests on.
- **?** unknown. Leave a name, effect or value out rather than guess.

Mixed claims are split into separate entries, one tag each.

## Names and addresses

- Names are project names from the research database, not official names.
- Addresses are specific to one game build. `symbols/` maps every named function and global to its RVA
  (`VA - image base`) per build; `symbols/builds.json` identifies the build by the SHA-256 of the executable.
- Live values (memory reads, traces, captures) are dated. A value in the executable image and the value the game
  holds at runtime can differ; both are given when they do (example: the default sampler word).

## References

Objects link to each other by `kind:Name` (see [kinds/README.md](../../kinds/README.md)). Reverse lists
(called by, read by, written by, used in, appears in) are computed from these references.

## What is not here

Analysis notes only: no machine code, no instruction text, no decompiled code, no original executable bytes, no
game assets or data tables. Shaders and file formats are described in words; hashes identify them.
