# GUIFontSlots_AcquireTexturePart

- **Address:** `0x1403DA918`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int GUIFontSlots_AcquireTexturePart(GUIFontSlots *slots, const char *path, __int64 a3)`
- **Callers:** GUITextNode_PlaceIcon, sub_1403F40AC, sub_1403F43C8, sub_1400F4F20
- **Callees:** sub_1403DB0EC, sub_1403DBB00, sub_1403DAB60, sub_1403DA4C0, sub_140037C84 / sub_140037C04 (hash), sub_140091124, sub_140011750 (alloc), GUISlotVec32_Insert (sub_1403EE918)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gets a kind-2 slot (texture part) for a path: reuses an existing record with the same name (refcount +1), otherwise requests the resource, appends a new 32-byte record with refcount 1 and returns its id.

## Behavior

- V: first sub_1403DB0EC(slots, buf, a3, path) copies the path (256 bytes) into a local buffer, rewriting '_2k_' to '_4k_' when present, and returns whether the path had _2k_ or _4k_ (flag v7). When slots+424 != 0 the buffer is then translated through sub_1403DBB00 (table 125, key 2001, column index = the dword at slots+424).
- V (reuse): sub_1403DAB60(slots, buf) scans the kind-2 vector for a record with refcount != 0 whose name string (the resource object's +24, or the empty string) equals buf; when found sub_1403DA4C0 increments its refcount and the function returns the existing id (the value in r11 after the call, not a Hex-Rays variable).
- V (create): otherwise a name hash is computed (a rolling hash with the xor constant 0x50C5D1F over the lower-cased path, '\\' mapped to '/', seed 0x811C9DC5 = -2128831035 for an empty path), the resource is requested with sub_140091124(qword_143CD9B88, buf, hash, 0, out), a 40-byte auxiliary object is allocated through the allocator at qword_143CDAA80 + 8 (zeroed, byte +35 = the 2k/4k flag) and a 32-byte record {+0 resource ptr, +16 aux ptr, +24 u16 refcount = 1, +26 = 0, +28 loaded = 0} is inserted with GUISlotVec32_Insert at slots+72.
- V: returns (index + 1) | 0x2000000 for a new record.

## State touched

- Calls: [GUISlotVec32_Insert](GUISlotVec32_Insert.md)

## Notes

Slot id layout (V, from the decode in GUIFontSlots_Release / _GetResource): id = (index + 1) | (kind << 24); kind 0 = plain slot vector (16-byte records at slots+16, refcount u16 at rec+8, loaded byte rec+12), kind 1 = vector at slots+48 (16-byte records, refcount rec+8), kind 2 = texture-part vector at slots+80 (32-byte records, refcount rec+24, loaded byte rec+28), kind 3 = image vector at slots+112 (16-byte records, refcount rec+8). The resource pointer is the first qword of the record. The name is ours (IDB: sub_1403DA918). The call from GUITextNode_PlaceIcon passes the icon slot's name path from the slot record (+56).

## Open questions

? what sub_140091124 does (resource handle create or find; it returns a pointer whose +24 is the name). ? the hash function body (sub_140037C04). ? the meaning of the 2001 / 2000 translation rows of table 125 (language / platform path override?).
