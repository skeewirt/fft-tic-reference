# Build symbol map

Durable, build-aware function map for TIC. The map keeps the **semantic name** stable and records where that function lives in each game build.

**No game code is stored here.** The map contains names, RVAs, sizes and hash fingerprints only. It does not contain raw bytes, instruction text, decompiled code, game files or assets.

## Files

| File | Contents |
|---|---|
| `builds.json` | Build profiles: input-file SHA-256, file name/size, image base |
| `functions.json` | One record per function page: area, doc page, per-build RVA/size/fingerprint |
| `globals.json` | One record per global page: area, doc page, per-build RVA |
| `formulas.json` | Formula ID -> semantic name/title, plus old-size evidence |

## Build identity

The build id is `sha256:<hash of the input executable>`. Never assume a VA without a build id:

- **RVA** = `VA - image base` (stable under ASLR).
- **VA** = `image_base + RVA` (only valid for that build).
- The `image_base` is recorded per build.

## Fingerprints

Each function stores a hash-only fingerprint:

- `mnemonics` — hash of the first 48 instruction mnemonics, operands ignored.
- `calls` — hash of the sorted direct-call target RVAs inside the function.
- `insn_count`, `call_count`, `size` — structural counts.

No bytes or disassembly text are persisted. Fingerprints are used only to find the same function in a new build.

## Formula table

The current dispatcher at `0x14030D720` indexes:

```text
off_140682BD0[formula_id - 1]()
```

So the formula table base is **RVA `0x682BD0`** and formula `N` is at entry `N-1`. `formulas.json` records the 87 documented formulas; `functions.json` holds their current RVAs and fingerprints. Formula 30/94/95 share one target (aliases), and F106 is the re-dispatch entry that also serves as the generic dispatcher.

## Coverage

`functions.json` has one entry per page in `docs/functions/` and `globals.json` one per page in `docs/globals/`;
both are rewritten for the current build whenever the reference is rebuilt (entries for other builds are kept).
The 87 formula functions were mapped from older research by formula table index and size, then re-documented
against the current build.

## Example record

```json
{
  "JobTree_Ctor": {
    "area": "job-tree",
    "doc": "docs/functions/JobTree_Ctor.md",
    "builds": {
      "sha256:...": {
        "rva": "0x133368",
        "size": 307,
        "fingerprint": {
          "mnemonics": "sha256:...",
          "calls": "sha256:...",
          "insn_count": 48,
          "call_count": 3,
          "size": 307
        }
      }
    }
  }
}
```
