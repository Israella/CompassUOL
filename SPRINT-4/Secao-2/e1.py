with open("number.txt") as file:
    numbers = list(map(int, file.readlines()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
sorted_numbers = sorted(even_numbers, reverse=True)

five_largest_numbers = sorted_numbers[:5]
sum_of_five_largest_numbers = sum(five_largest_numbers)

print(five_largest_numbers)

print(sum_of_five_largest_numbers)
