def make_timetable(meetings):
    if len(meetings) == 0:
        return 0
    if len(meetings) == 1:
        return 1
    meetings.sort()
    start = 0
    end = 0
    max_number_of_rooms = 1
    number_of_rooms = 0
    while (start < len(meetings)) and (end < len(meetings)):
        if end == start:
            end += 1
            number_of_rooms += 1
            continue
        if meetings[start][0] <= meetings[end][0] < meetings[start][1]:
            number_of_rooms += 1
            end += 1
        else:
            max_number_of_rooms = max(max_number_of_rooms, number_of_rooms)
            start += 1
            number_of_rooms -= 1
    max_number_of_rooms = max(max_number_of_rooms, number_of_rooms)
    return max_number_of_rooms
