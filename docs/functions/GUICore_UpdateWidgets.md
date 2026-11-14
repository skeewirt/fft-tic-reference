# GUICore_UpdateWidgets

- **Address:** `0x1403D76E4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_UpdateWidgets(GUICore *core)`
- **Callers:** frame update
- **Callees:** sub_1403D7670, sub_1403F08C0, sub_14009006C, ResetEvent, SetEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame widget update (the second GUICore update function; see GUICore_UpdateFrame for the other): orders the widgets, wires the ten frame worker slots when a task object exists and updates every widget.

## Behavior

- V: insertion-sorts the widget list (core+16 .. +24) so the widget with the larger word at +62 comes first.
- V: when core+2128 holds an object, waits until the worker counter at +4788 is 0, resets the event (+4776), sets the counters (widget count at +4784, 10 at +4788), clears each widget's +600 field, then registers ten callbacks (sub_1403D79C4 and sub_1403D7A5C wrapped by sub_14009006C) on the object's virtual +48 for the 264-byte slots from core+2136.
- V: for each widget, when there is no task object or the widget's +84 byte is 0, calls sub_1403D7670 and decrements the worker counter, signalling the event when it reaches 0; with no task object it then refreshes the component nodes that have their +562 / +559 flags (sub_1403F08C0).

## Notes

Only the structure was read; the callbacks and the task object at core+2128 are not documented.

## Open questions

What the object at core+2128 is (a job system?) (?).
