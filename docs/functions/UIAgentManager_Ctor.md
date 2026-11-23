# UIAgentManager_Ctor

- **Address:** `0x1401CF3DC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `ffto::Game::UI::UIAgentModule *UIAgentManager_Ctor(ffto::Game::UI::UIAgentModule *self)`
- **Callers:** sub_1400E1D30 (0x1400E21A5), the UI manager constructor
- **Callees:** UIAgentManager_CreateAgents

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the singleton UI agent manager: stores its module vtable and allocator objects, starts the agent, addon, font-slot and queued-event containers empty, then calls UIAgentManager_CreateAgents to fill the agent vector. The UI manager constructor allocates the 184-byte object and keeps it at 0x143CD9DA8.

## Behavior

- V: stores the module vtable 0x140713280 at +0; its first slot is the deleting destructor sub_1401CF4DC, which frees a 184-byte object through the allocator that created it.
- V: reads the service global at 0x143CDAA80 and copies its +32 allocator object into +8, +40, +96 and +136; when the global is null it stores zero.
- V: clears the agent vector (+16 begin, +24 end, +32 capacity), the addon map allocator (+40), head (+48), size (+56), the event callback block (+64 callback, +72 context, 16 bytes at +80), the event queue (+96 allocator, +104 begin, +112 end, +120 capacity), the addon id counter (+128), the font-slot vector (+136 allocator, +144 begin, +152 end, +160 capacity), the font-slot state byte (+168) and the init state (+176).
- V: allocates a 48-byte map head through the allocator at +40 (allocator vtable slot +16), points its first three pointers at itself, sets the two bytes at +24 to 1, stores it at +48 and leaves +56 at zero.
- V: calls UIAgentManager_CreateAgents(self) as its last action and returns self; CreateAgents sets +176 to 1.
- V: the only caller is sub_1400E1D30, the UI manager constructor. It allocates 184 bytes through the service global's +16 allocator, zeroes all 184 bytes, calls this ctor and stores the result at 0x143CD9DA8. The manager is therefore the object it receives as self, and the object is 184 bytes.
- V: no field after +176 is written here; the last four bytes stay zero from the caller's clear.
- I: the allocator/begin/end/capacity groups at +8, +96 and +136 are the manager's agent, queued-event and font-slot vectors, and the group at +40 is the keyed addon map (rests on the identical layout and on the append, insert and free helpers that use them).
- ?: what the service global at 0x143CDAA80 is, who owns its +32 allocator, and whether any path can call this constructor twice.

## State touched

- Calls: [UIAgentManager_CreateAgents](UIAgentManager_CreateAgents.md)

## Referenced by

- Appears in flows: [UIAgentLifecycle](../flows/UIAgentLifecycle.md)

## Notes

Whole 255-byte function read, plus its caller and the deleting destructor. The IDB names the class UIAgentModule; this reference uses the name UIAgentManager. The addon map is an ordered map whose head and nodes are 48 bytes. Addresses are build-specific.

## Open questions

The manager global 0x143CD9DA8 and the service global 0x143CDAA80 have no reference records; both are named by address. What the +32 allocator is and who installs it remains open.
