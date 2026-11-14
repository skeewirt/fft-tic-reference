# GUITextNode_Copy

- **Address:** `0x1403F0E24`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUITextNode_Copy(__int64 dst, __int64 src)`
- **Callers:** sub_140136A7C, sub_1403FAD88
- **Callees:** sub_1403EF54C, sub_140025C74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a text node's configuration fields from src into dst and marks dst dirty.

## Behavior

- V: sub_1403EF54C(dst, src) copies the base node first.
- V: if dst+208 != src+208 it runs sub_140025C74(dst+208) (re-init of the string member at +208; the string content itself is not copied here).
- V: dword copies +248, +252, +256, +260, +264, +268, +272, +276, +280, +284, +288, +292 (text id, flags, colours); +296 is forced to 0 on dst (not copied).
- V: +300 dword, +304 word, +306 word, +308 word, bytes +310..+315 copied; dst+316 = 1 at the end (needs relayout).
- V: callers sub_140136A7C (0x140136AE0) and sub_1403FAD88 (0x1403FAF10).

## Notes

Does not duplicate the laid-out glyph vectors (+320..); the node relayouts because +316 = 1.

## Open questions

? whether sub_140025C74 clears or re-inits the string (called without src content).
