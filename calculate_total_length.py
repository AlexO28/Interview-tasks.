# написать функцию, которая:
# * принимает на вход массивы arr1 и arr2 непересекающихся целочисленных отрезков вида:
# * arr1 = [[8, 9], [11, 13], [14, 18]]
# * arr2 = [[8, 10], [12, 14], [15, 16], [17, 18]]
# * считает их пересечение, т.е. массив вида:
# * result = [[8, 9], [12, 13], [15, 16], [17, 18]]
# * возвращает сумму длин интервалов в result (в примере 4)
# нужен алгоритм, который работает за O(N + M)
def calculate_total_length(arr1, arr2):
    arr1.sort()
    arr2.sort()
    result = []
    i = 0
    j = 0
    while (i < len(arr1)) and (j < len(arr2)):
        val1 = max(arr1[i][0], arr2[j][0])
        val2 = min(arr1[i][1], arr2[j][1])
        if val1 < val2:
            result.append([val1, val2])
        if arr1[i][0] >= arr2[j][0]:
            i += 1
        else:
            j += 1
    return sum([elem[1] - elem[0] for elem in result])
