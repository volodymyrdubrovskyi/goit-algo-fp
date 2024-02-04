import random
from collections import defaultdict


def main():
    nums = 1_000_000
    counts = defaultdict(int)

    for _ in range(nums):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice = dice1 + dice2
        counts[dice] += 1

    probabilities = {key: count / nums for key, count in counts.items()}
    myKeys = list(probabilities.keys())
    myKeys.sort()
    prob_sort = {i: probabilities[i] for i in myKeys}

    print('| Варіант | Верогідність ')
    print('|---------|--------------')
    for dice, prob in prob_sort.items():
        print(f'|{dice:^8} | {prob:.2%}')

if __name__ == '__main__':
    main()    