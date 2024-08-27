def minimum(some_list):
    a = 0
    for x in range(1, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]
    return a

print(minimum([1, 2, 3, 4, 5]))