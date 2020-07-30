import random

number_of_streaks = 0

for experiment_number in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flip_results = []
    for flip_number in range(100):
        if random.randint(0, 1) == 0:
            flip_results.append('H')
        elif random.randint(0, 1) == 1:
            flip_results.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index, item in enumerate(flip_results):
        if index + 6 == len(flip_results) - 1:
            break

        if all(j == flip_results[index] for j in flip_results[index:index+6]):
            number_of_streaks += 1
            break

print(f'Number of streaks: {number_of_streaks}, \
out of {experiment_number + 1} experiments')
print(f'Chance of streak: {number_of_streaks / 100}%')
