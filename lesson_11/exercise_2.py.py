
war_of_numbers = [12, 90, 75]


def who_win(numbers: list[int]) -> int:
    odd = []    
    even = []
    for item in numbers:
        if item % 2 == 0:
            odd.append(item)
        else:
            even.append(item)
    if sum(odd) > sum(even):
        return sum(odd)
    elif sum(odd) < sum(even):
        return sum(even)


print(who_win(war_of_numbers))