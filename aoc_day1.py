with open('aoc_day1.txt', 'r') as f:
    arr = []
    freq_list = []
    numbers = [int(lines.strip()) for lines in f]

print(f'part a: {sum(numbers)}')

def find_repeat_freq(numbers):
    freq_list = {0}
    running_freq = 0
    found = False
    while not(found):
        for num in numbers:
            running_freq += num
            if running_freq in freq_list:
                found = True
                return running_freq
            else:
                freq_list.add(running_freq)


assert find_repeat_freq([1, -1]) == 0
assert find_repeat_freq([3, 3, 4, -2, -4]) == 10
assert find_repeat_freq([-6, 3, 8, 5, -6]) == 5
assert find_repeat_freq([7, 7, -2, -7, -4]) == 14

print(f'part b: {find_repeat_freq(numbers)}')