# GUIOwnerMap_Find

- **Address:** `0x1403DC1A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *GUIOwnerMap_Find(Map *m, int key)`
- **Callers:** GUIOwners_PostEvent, sub_1400FDFF4, sub_140188428, sub_1403D7008
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks an int key up in a std::map<int, T*> (red-black tree head at m+16) and returns the stored pointer or null.

## Behavior

- V: lower_bound walk from head->parent (+8): node key is the int at node+32, left = +0, right = +16, sentinel flag = byte +25; value = node+40. Returns 0 when not found (lower bound is the head or its key > the wanted one).

## Notes

The name is ours (IDB: sub_1403DC1A8). 3184 hits per 4 s. A plain MSVC std::map find; no arithmetic.

## Open questions

? What the key is in GUIOwners_PostEvent (I: owner / event id).
