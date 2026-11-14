# FormatArgRecord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 264 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One argument of a formatted UI text string: a 256-byte text area and a type dword at +0x100. The banner builds a vector of these, either from the descriptor or from the message object's stored entries, and hands it over with the template, which substitutes them into the <string=...> and <num=...> markers.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="text"></a>`0x0` | text | `char[256]` | V | Argument text when the type is not 1: up to 255 characters. For an integer argument the dword at +0 holds the value (V, decompile of the argument push and the filler). |
| <a id="type"></a>`0x100` | type | `uint32` | V | 1 = integer (value in the dword at +0); any other value = the string at +0 is used (V, decompile). |

## Behavior

- V: one record is appended by FormatArgs_Push (FormatArgs_Push) to the vector held by the format-arguments object (write pointer at +0x10, end at +0x18) (decompile).
- V: BattleMsg_FillArgs (sub_1401EC074) resets the vector, then either fills it from the descriptor or copies up to 40 stored entries from the message object at a 524-byte stride (decompile).

## Notes

The stored 524-byte entry is wider than this 264-byte vector record; its layout is not decoded (?).

## Open questions

? the stored entry's layout; ? whether the string area is always terminated inside 256 bytes.
