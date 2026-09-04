def make_timetable(meetings):
    if len(meetings) == 0:
        return 0
    if len(meetings) == 1:
        return 1
    starts = sorted([m[0] for m in meetings])
    ends = sorted([m[1] for m in meetings])
    start = 0
    end = 0
    max_rooms = 0
    current_rooms = 0
    while start < len(meetings):
        if starts[start] < ends[end]:
            current_rooms += 1
            start += 1
        else:
            current_rooms -= 1
            end += 1            
        max_rooms = max(max_rooms, current_rooms)
    return max_rooms
