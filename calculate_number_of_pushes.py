def calculate_number_of_pushes(m, n, password):
    if len(password) == 1:
        return 0
    total_number_of_pushes = 0
    for j in range(1, len(password)):
        total_number_of_pushes += calculate_distance(m, n, password[j - 1], password[j])
    return total_number_of_pushes

def calculate_distance(m, n, i, j):
    x1, y1 = find_coordinates(m, n, i)
    x2, y2 = find_coordinates(m, n, j)
    return max(abs(x1 - x2), abs(y1 - y2))

def find_coordinates(m, n, i):
    main_part, remainder = divmod(i - 1, n)
    return main_part, remainder
