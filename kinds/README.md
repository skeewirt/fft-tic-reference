# Kinds: the object types of this reference

Every object documented here has a **kind** (function, structure, global, registry, shader, shader program, render
target, file format, flow, observed behaviour, event opcode, ...). Each kind is defined by one file in this folder,
`<kind>.json`, and rendered by one template, `templates/<kind>.md`. Records of the kind live in
`data/<plural>.jsonl` and (when the kind has pages) in `docs/<plural>/<Name>.md`, with an index at
`docs/<plural>/README.md`.

## Adding a new kind

1. Write `kinds/<kind>.json` (format below).
2. Write `templates/<kind>.md` (copy the closest existing template; keep the `## Referenced by` / `{{references}}`
   block so links from other kinds show up).
3. Add records. Nothing else changes: the README, the area pages, the indexes and the reverse lists pick the kind up
   automatically.

## Kind file

| Key | Meaning |
|---|---|
| `kind` | Id used in references (`kind:Name`). Lower case, hyphens allowed. |
| `plural` | Folder name under `docs/` and file name under `data/`. |
| `title`, `singular` | Display names. |
| `description` | One sentence: what the kind covers (shown in the README and the index). |
| `key` | The field that names a record (usually `name`). |
| `pages` | `true`: one page per record. `false`: index page only (the records are the documentation). |
| `template` | Page template in `templates/`. |
| `symbols` | Optional: the build-aware address map in `symbols/` for this kind. |
| `fields` | The record fields, in output order (types below). `required: true` makes a field mandatory. |
| `index` | Columns of the index and area tables. |

## Field types

| Type | Value | Rendered as |
|---|---|---|
| `name` | The record key | text |
| `string` | One line | text |
| `code` | One line | `code` |
| `addr` | Address in the current build | `0x...` (RVAs per build in `symbols/`) |
| `int`, `hex` | Number | decimal / `0x...` |
| `conf` | `V`, `M`, `I` or `?` | text |
| `area` | Area label | link to the area page (mapping in `areas.json`) |
| `md` | Markdown paragraph(s) | as written |
| `tagged` | List of `{conf, basis, text}` | `- V (basis): text` bullets |
| `list` | List of strings | bullets |
| `refs` | List of references | links |
| `members` | List of objects (struct fields, registry entries, flow steps, ...) | table; `columns` lists the member fields, `key` the member that anchors the row |
| `data` | Any JSON value | data file only |

## References and reverse lists

A reference is `kind:Name`, `kind:Name#member` (a struct field, registry entry, flow step, ...) or either of these
followed by free text (`struct:RenderContext#sampler_words [14, 15]`). A `refs` field (or a `members` column of type
`ref`) may declare an `inverse`:

```json
"writes": {"type": "refs", "inverse": {"name": "written_by", "label": "Written by"}}
```

Every reference then appears on the target as well: on its page under **Referenced by** (or, for a member, as a
column of its table), and in its data record under `referenced_by`. Reverse lists are always computed; nobody types
"called by" or "written by" by hand.

## Confidence

Every behaviour entry, member and record that states a fact carries a tag: **V** decoded from code or data or
confirmed by a live read or capture (name the basis when it matters), **M** measured (a number, not yet a rule),
**I** inferred (say what it rests on), **?** unknown. See [docs/guides/conventions.md](../docs/guides/conventions.md).
