# GUITextNode_Init

- **Address:** `0x1403F0BB4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_Init(__int64 node)`
- **Callers:** sub_140136A7C (0x140136ABE), sub_140405490 (0x1404055DC)
- **Callees:** sub_1403EF3B4, sub_140025C74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor defaults of a text node: base init with type 3, vtable, empty containers and default colours / flags.

## Behavior

- V: sub_1403EF3B4(node, 3) (base node init, type 3); vtable at +0 = GUITextNode vftable 0x140721DA0.
- V: three allocator pointer fields at +208, +320, +352, +384 each = qword_143CDAA80[+32] (allocator) or 0, followed by zeroed triples (+216.., +328.., +360.., +392..): empty std-vector / string members. +240 = 15 (small-string capacity), +232 = 0.
- V: +416 dword = 0, +420 word = 256 (two bytes 0 and 1), +444 byte = 0, +448 = 0, +424..+440 zeroed; then sub_140025C74(node+208) (string init).
- V: colours: +280 = 0xFFFFFFFF, +284 = 0xFF606060 (-10461088), +288 = 0xFFC0C0C0 (-4144960), +292 = 0xFF202020 (-14671840). +248/+256 = 0, +264 = 2, +268 = +272 = +276 = 1, +296 = 0.
- V: +304 = 32 (qword write: word +304 = 32, +306/+308 = 0), +312 = 0, +316 byte = 1 (dirty flag; GUITextNode_Copy also sets it to 1).
- I: +300 (font set) is zeroed by the +296 qword store; +304 = 32 would be the size.

## Notes

Defaults here are the node's own; the font-set row defaults are separate (UIFontSetRow_Default). Offsets +248..+316 match those copied by GUITextNode_Copy.

## Open questions

? names of +264/+268/+272/+276 (alignment / flags, defaults 2,1,1,1). ? what the +320..+410 vectors hold (glyph / line lists, I).
