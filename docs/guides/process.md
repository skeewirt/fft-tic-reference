# Process

## When something is studied

Document what was studied, in the kind it belongs to, at the time it is studied:

- a **function** that was read gets a sheet (new) or an update (existing): address, prototype, callers / callees,
  tagged behaviour, open questions; and the state it touches as references (`reads`, `writes`, `calls`).
- a **structure**, **global**, **registry**, **shader**, **render target**, **file format** that was decoded gets a
  record of its kind, member by member, each member tagged.
- an **order of events** that matters (a frame, a pass, a load) becomes a **flow**.
- a fact that no single function owns (inherited state, a conversion rule of the GPU) becomes an
  **observed behaviour**.
- a new type of thing becomes a new kind ([kinds/README.md](../../kinds/README.md)).

Re-verify against the current build before writing; write in our own words; never copy code.

## Checklist

- [ ] address / identity verified against the current build
- [ ] every entry tagged **V** / **M** / **I** / **?**, with the basis named where it matters
- [ ] references to the objects touched (so the reverse lists stay complete)
- [ ] no machine code, original bytes, assets or private paths
- [ ] database names applied, the reference rebuilt and audited

## Opcodes

Event opcodes are data records, never prose pages: [opcodes-format.md](opcodes-format.md).
