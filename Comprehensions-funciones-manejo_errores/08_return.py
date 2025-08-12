
def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max + 1):
        sum += x
    return sum

result = sum_with_range(1, 10)  # 55
print(result)
result_2 = sum_with_range(5, 15)  # 110
print(result_2)
result_3 = sum_with_range(10, 20)  # 165
print(result_3)