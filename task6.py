import copy


def data_transform(items: dict):
    for name, data_v in items.items():
        data_v['ratio'] = round(data_v['calories'] / data_v['cost'], 3)
        data_v['name'] = name
    product_list = list(items.values())
    product_list.sort(key=lambda x: x['ratio'], reverse=True)
    return product_list

def greedy_algorithm(items: dict, budget: float):
    product_list = data_transform(items)
    current_budget = budget
    backpaked_items = list()
    backpaked_value = 0
    backpaked_cal = 0
    for r in product_list:
        #print(r)
        if r['cost'] <= current_budget:
            backpaked_items.append(r)
            current_budget -= r['cost']
            backpaked_value += r['cost']
            backpaked_cal += r['calories']
            #print('Backpaked: ', r)
    return backpaked_value, backpaked_cal, backpaked_items

def dynamic_programming(items: dict, budget: float):
    product_list = data_transform(items)
    for r in product_list:
        r.pop('ratio')

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    n = len(product_list)
    K = [[[0,[]] for w in range(budget + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                K[i][b] = [0,[]]
            elif product_list[i - 1]['cost'] <= b:
                if product_list[i - 1]['calories'] + K[i - 1][b - product_list[i - 1]['cost']][0] > K[i - 1][b][0]:
                    K[i][b][0] = product_list[i - 1]['calories'] + K[i - 1][b - product_list[i - 1]['cost']][0]
                    K[i][b][1] = copy.deepcopy(K[i-1][b- product_list[i - 1]['cost']][1])
                    K[i][b][1].append(product_list[i - 1])
                else:
                    K[i][b] = K[i - 1][b]
            else:
                K[i][b] = K[i - 1][b]
    return K[n][budget]

def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # задаємо бюджет на продукти
    budget = 110

    print('Дані по усім продуктам з рейтингами:')
    for r in data_transform(items):
        print(r)
    print()

    backpaked_value, backpaked_cal, backpaked_items = greedy_algorithm(items, budget)
    print(f'Жадібний алгоритм, \nу рюкзаку: вартість продуктів {backpaked_value} (при бюджеті {budget}). Калорій: {backpaked_cal}')
    print('Продукти у рюкзаку:')
    for r in backpaked_items:
        print(r)
    
    print()

    result = dynamic_programming(items, budget)
    backpaked_cal = result[0]
    backpaked_items = result[1]
    backpaked_value = 0
    for r in backpaked_items:
        backpaked_value += r['cost']
    print(f'Алгоритм динамічного програмування, \nу рюкзаку: вартість продуктів {backpaked_value} (при бюджеті {budget}). Калорій: {backpaked_cal}')
    print('Продукти у рюкзаку:')
    for r in backpaked_items:
        print(r)

if __name__ == '__main__':
    main()