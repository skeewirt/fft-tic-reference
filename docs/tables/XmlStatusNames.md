# XmlStatusNames

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x14077DBE0`
- **Rows:** 27 rows of 8 bytes
- **Keyed by:** XML status code (I)
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Names of the XML parser status codes (success, no attribute, wrong attribute type, file not found, could not be opened, read error, parsing errors per node kind, empty document, mismatched element, cannot convert text, no text node, depth exceeded), the words true and false and five markup openers. Verdict: text.

## Behavior

- V: slot 21 is not a string: it holds a data pointer that the program writes while running (a write reference exists in the code), so the table has 26 string slots and one runtime slot
- V: no string of the list has a reference pointing inside it
- V: 27 pointers; two boolean words, 19 status names, one more pointer and 5 markup openers
- I: the one code reference sits in a small formatter that prints a single string

## Notes

Our names. Tags: V layout, I use.

## Open questions

- ?: the exact code to name mapping
