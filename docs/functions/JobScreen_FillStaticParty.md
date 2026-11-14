# JobScreen_FillStaticParty

- **Address:** `0x14039231C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JobScreen_FillStaticParty(UnitWork *c)`
- **Callers:** 1
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a work record's per-job arrays into the static party-shaped record at 0x143C51F10 that the job screen readers sub_140392800 / sub_14039284C / sub_140392884 read through qword_141D3B778.

## Behavior

- V: mask (+120..122), learned bits, levels, JP and total JP into the globals 0x143C51F88 .. 0x143C52008.

## Open questions

I: the purpose of the static record (a preview of the job change) from its readers.
