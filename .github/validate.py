"""Validate this repository against its own format. Exit status 1 when anything is wrong.

Policy: this repository holds only original written notes and interpretation. It does not republish other people's
content, and it contains no game code, game data or assets. This check confirms the notes are original: no machine
code, original bytes, decompiled output or private material in any page or record.

    python .github/validate.py [ROOT]

Checks, all driven by the repository's own definitions (kinds/*.json, areas.json):
  records     every line of data/<plural>.jsonl is a valid record of its kind: required fields filled, field
              types right, confidence tags one of V / M / I / ?, references resolve to an existing record
              (and member), area slugs exist; kind-specific rules (event opcodes: docs/guides/opcodes-format.md)
  pages       every record of a kind with pages has docs/<plural>/<key>.md and every page has a record
  content     no machine code, original bytes, decompiled text or private paths in any page
              or record
  links       every relative link in a page points at an existing file
  symbols     every record of a kind with a symbol map has an entry in symbols/<file> and vice versa
Uses the standard library only (it runs in CI as is).
"""
import json
import re
import sys
from pathlib import Path

CONF = ("V", "M", "I", "?")
MNEM = (r"mov|movzx|movsx|movss|movaps|lea|cmp|test|jmp|jz|jnz|je|jne|ja|jb|jae|jbe|jg|jl|jge|jle|call|"
        r"push|pop|xor|and|or|add|sub|imul|idiv|shl|shr|sar|ret|nop|cvtsi2ss|mulss|addss")
RULES = [
    ("asm-in-code-span", re.compile(r"`(?:" + MNEM + r")\s+[^`]*[,\[][^`]*`", re.I)),
    ("asm-bare-line", re.compile(r"^\s*(?:" + MNEM + r")\s+[a-z0-9_\[]+\s*,", re.I | re.M)),
    ("hex-byte-run", re.compile(r"(?<![0-9A-Za-z])(?:[0-9A-Fa-f]{2}[ ,]){4,}[0-9A-Fa-f]{2}(?![0-9A-Za-z])")),
    ("private-path", re.compile(r"[A-Za-z]:[\\/]|/Users/|\\Users\\|\bout/|\btools/|\bnotes/|\bmods/|\.i64")),
    ("decompiler-code", re.compile(r"\*\(\s*_?(?:BYTE|WORD|DWORD|QWORD|uint\d+_t|int\d+_t)\s*\*|\bLODWORD\(|\bHIDWORD\(|^\s*\w+\s*=\s*\*\(|\bJUMPOUT\(")),
]
REF = re.compile(r"^(?:(?P<kind>[a-z-]+):)?(?P<name>[A-Za-z0-9_.\-]+)(?:#(?P<member>[A-Za-z0-9_]+))?(?P<detail>.*)$")
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def gate(text: str) -> list:
    bad = []
    for name, rx in RULES:
        for m in rx.finditer(text):
            bad.append(f"line {text.count(chr(10), 0, m.start()) + 1}: {name}: {m.group(0).strip()[:70]}")
    return bad


def strings_of(v) -> list:
    if isinstance(v, str):
        return [v]
    if isinstance(v, dict):
        return [s for k, x in v.items() for s in [str(k)] + strings_of(x)]
    if isinstance(v, list):
        return [s for x in v for s in strings_of(x)]
    return []


def gate_json(text: str) -> list:
    bad = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip():
            bad += [f"record {i}: {b}" for b in gate("\n".join(strings_of(json.loads(line))))]
    return bad


# ---------------------------------------------------------------- kind-specific rules

OPCODE_BLOCKS = {None, "frames", "task", "input", "message"}
ASM_IN_TEXT = re.compile(r"\b(?:" + MNEM + r")\s+(?:[re]?[abcd]x|[abcd][lh]|[re]?[sd]il?|[re]?[sb]pl?|r\d{1,2}[dwb]?|xmm\d+|\[)[^,]*,", re.I)


def validate_opcode(key: str, r: dict) -> list:
    """Event opcode records (docs/guides/opcodes-format.md, schema 1)."""
    bad, tag = [], f"opcode:{key}"
    if not re.fullmatch(r"0x[0-9A-F]{2}", r.get("op") or ""):
        bad.append(f"{tag}: bad op {r.get('op')!r}")
    if r.get("conf") not in ("V", "I", "?"):
        bad.append(f"{tag}: bad conf {r.get('conf')!r}")
    if r.get("blocks") not in OPCODE_BLOCKS:
        bad.append(f"{tag}: bad blocks {r.get('blocks')!r}")
    if r.get("conf") in ("V", "I") and not r.get("evidence"):
        bad.append(f"{tag}: conf {r['conf']} needs evidence")
    if r.get("conf") == "?" and (r.get("name") or r.get("effect")):
        bad.append(f"{tag}: a named or described opcode must not have conf '?'")
    used, limit = [], r.get("operand_bytes_enhanced")
    for o in r.get("operands") or []:
        if not isinstance(o, dict) or set(o) != {"at", "size", "type", "meaning"}:
            bad.append(f"{tag}: operand object keys")
            continue
        if isinstance(o["at"], int) and isinstance(o["size"], int):
            span = range(o["at"], o["at"] + o["size"])
            if o["at"] < 1 or (limit is not None and o["at"] + o["size"] - 1 > limit):
                bad.append(f"{tag}: operand at {o['at']} size {o['size']} does not fit {limit} operand bytes")
            if any(b in used for b in span):
                bad.append(f"{tag}: operands overlap at {o['at']}")
            used.extend(span)
    for fld in ("name", "effect", "where"):
        if isinstance(r.get(fld), str) and ASM_IN_TEXT.search(r[fld]):
            bad.append(f"{tag}: asm in {fld}: {r[fld][:50]}")
    return bad


VALIDATORS = {"opcode": validate_opcode}


# ---------------------------------------------------------------- records

def load_kinds(root: Path) -> dict:
    return {k["kind"]: k for k in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((root / "kinds").glob("*.json")))}


def check_value(kind, key, f, spec, v, slugs) -> list:
    t, tag = spec["type"], f"{kind}:{key}.{f}"
    empty = v is None or v == "" or v == []
    if spec.get("required") and empty:
        return [f"{tag}: required field is empty"]
    if empty:
        return []
    if t in ("name", "string", "code", "md") and not isinstance(v, str):
        return [f"{tag}: must be a string"]
    if t == "addr" and not (isinstance(v, str) and re.fullmatch(r"0x[0-9A-F]+", v)):
        return [f"{tag}: must be an address like 0x1400F8474"]
    if t == "int" and not isinstance(v, int):
        return [f"{tag}: must be an integer"]
    if t == "conf" and v not in CONF:
        return [f"{tag}: must be one of {CONF}"]
    if t == "area" and v not in slugs:
        return [f"{tag}: area '{v}' is not in areas.json"]
    if t == "tagged":
        if not isinstance(v, list):
            return [f"{tag}: must be a list"]
        return [f"{tag}: entry {i} must be {{conf, basis, text}} with conf one of {CONF}" for i, e in enumerate(v)
                if not (isinstance(e, dict) and e.get("conf") in CONF and isinstance(e.get("text"), str) and e["text"])]
    if t in ("list", "refs") and not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
        return [f"{tag}: must be a list of strings"]
    if t == "members":
        if not isinstance(v, list) or not all(isinstance(m, dict) for m in v):
            return [f"{tag}: must be a list of objects"]
        bad = []
        for m in v:
            if "conf" in m and m["conf"] not in CONF:
                bad.append(f"{tag}: member {m.get(spec.get('key', 'name'))}: conf '{m['conf']}'")
            if not m.get(spec.get("key", "name")) and m.get(spec.get("key", "name")) != 0:
                bad.append(f"{tag}: member without '{spec.get('key', 'name')}'")
        return bad
    return []


def validate_records(root: Path, kinds: dict) -> tuple:
    areas = json.loads((root / "areas.json").read_text(encoding="utf-8"))
    slugs = {a["slug"] for a in areas["areas"]}
    records, bad = {}, []
    for kind, kd in kinds.items():
        f = root / "data" / f"{kd['plural']}.jsonl"
        records[kind] = {}
        if not f.exists():
            bad.append(f"data/{kd['plural']}.jsonl: missing")
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except ValueError:
                bad.append(f"data/{kd['plural']}.jsonl:{i}: not valid JSON")
                continue
            key = str(r.get(kd["key"]))
            if key in records[kind]:
                bad.append(f"{kind}:{key}: defined twice")
            records[kind][key] = r
            for fld in r:
                if fld not in kd["fields"] and fld != "referenced_by":
                    bad.append(f"{kind}:{key}: field '{fld}' is not in kinds/{kind}.json")
            for fld, spec in kd["fields"].items():
                bad += check_value(kind, key, fld, spec, r.get(fld), slugs)
            if kind in VALIDATORS:
                bad += VALIDATORS[kind](key, r)
    # references
    for kind, kd in kinds.items():
        for key, r in records[kind].items():
            for fld, spec in kd["fields"].items():
                refs = []
                if spec["type"] == "refs":
                    refs = [(x, spec.get("to")) for x in r.get(fld) or []]
                if spec["type"] == "members":
                    refs = [(m.get(c["field"]), None) for c in spec.get("columns", []) if c.get("type") == "ref"
                            for m in r.get(fld) or [] if m.get(c["field"])]
                for ref, default in refs:
                    if not resolves(ref, default, records, kinds):
                        bad.append(f"{kind}:{key}.{fld}: reference '{ref}' does not resolve")
    return records, bad


def resolves(ref, default_kind, records, kinds) -> bool:
    m = REF.match(ref.strip())
    if not m:
        return False
    kind, name, member = m.group("kind") or default_kind, m.group("name"), m.group("member")
    if kind is None:
        hits = [k for k in records if name in records[k]]
        if len(hits) != 1:
            return False
        kind = hits[0]
    rec = records.get(kind, {}).get(name)
    if rec is None:
        return False
    if member:
        spec = kinds[kind]["fields"].get("members", {})
        return any(str(x.get(spec.get("key", "name"))) == member for x in rec.get("members") or [])
    return True


# ---------------------------------------------------------------- tree

def audit(root: Path) -> list:
    root = Path(root)
    kinds = load_kinds(root)
    records, bad = validate_records(root, kinds)
    for kind, kd in kinds.items():
        folder = root / "docs" / kd["plural"]
        if not (folder / "README.md").exists():
            bad.append(f"docs/{kd['plural']}/README.md: missing index")
        if kd.get("pages", True):
            pages = {p.stem for p in folder.glob("*.md") if p.name != "README.md"}
            for k in sorted(set(records[kind]) - pages):
                bad.append(f"{kind}:{k}: no page docs/{kd['plural']}/{k}.md")
            for k in sorted(pages - set(records[kind])):
                bad.append(f"docs/{kd['plural']}/{k}.md: page without a record")
        if kd.get("symbols"):
            sf = root / "symbols" / kd["symbols"]
            if not sf.exists():
                bad.append(f"symbols/{kd['symbols']}: missing")
            else:
                data = json.loads(sf.read_text(encoding="utf-8"))
                mapped = set(data.get(kd["plural"], data.get("functions", data.get("globals", {}))))
                for n in sorted(set(records[kind]) - mapped):
                    bad.append(f"symbols/{kd['symbols']}: no entry for {kind} {n}")
                for n in sorted(mapped - set(records[kind])):
                    bad.append(f"symbols/{kd['symbols']}: entry {n} has no record")
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if ".git" in p.relative_to(root).parts or not p.is_file() or rel == "LICENSE" or rel.startswith(("templates/", ".github/")):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        if p.suffix == ".jsonl":
            bad += [f"{rel}: {b}" for b in gate_json(text)]
        elif p.suffix in (".md", ".json"):
            bad += [f"{rel}: {b}" for b in gate(text)]
        if p.suffix == ".md":
            for m in LINK.finditer(text):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:")) or not re.search(r"\.(?:md|json|jsonl)$|/", target):
                    continue
                if not (p.parent / target).resolve().exists():
                    bad.append(f"{rel}: broken link {target}")
    return bad


def main(argv) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parents[1]
    bad = audit(root)
    for b in bad:
        print(b)
    print(f"validate: {len(bad)} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
