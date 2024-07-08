# Написать функцию, определяющую, может ли список в результате какой-то перестановки стать палиндромомом
def can_be_palindrome(arr):
    if len(arr) == 0:
        return False
    arr_dict = {}
    for elem in arr:
        if elem in arr_dict:
            arr_dict[elem] += 1
        else:
            arr_dict[elem] = 1
    number_of_odds = 0
    for elem in arr_dict.keys():
        if arr_dict[elem] % 2 == 1:
            number_of_odds += 1
            if number_of_odds > 1:
                return False
    if (len(arr) % 2) == 0:
        return (number_of_odds == 0)
    else:
        return (number_of_odds == 1)
