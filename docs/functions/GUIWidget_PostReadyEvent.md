# GUIWidget_PostReadyEvent

- **Address:** `0x1403FC0FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUIWidget_PostReadyEvent(GUIWidget *w)`
- **Callers:** vtable entries (0x1407045A8, 0x140721E40, 0x143D42220)
- **Callees:** GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable entry: posts the event record xmmword_140723260 to the widget's owners (w+288) and returns whether the reply field was set.

## Behavior

- V: ev = 16-byte constant xmmword_140723260; GUIOwners_PostEvent(w+288, w, &ev); returns ev dword[3] != 0 (owners write the reply there).

## State touched

- Calls: [GUIOwners_PostEvent](GUIOwners_PostEvent.md)

## Notes

The name is ours (IDB: sub_1403FC0FC). 868 hits per 4 s. I: a query event ('is the widget busy / ready'); the constant's event id was not read.

## Open questions

? Event id inside xmmword_140723260.
