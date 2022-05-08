from pprint import pprint
cook_book = {}
with open('cook_book.txt', 'r', encoding='utf-8') as file:
    while True:
        key = (file.readline().strip()).strip()
        if not key:
            break
        cook_book[key] = []
        ingredient_count = int(file.readline().strip())
        for line in range(ingredient_count):
            ingredient = file.readline().strip().split("|")
            cook_book[key] += [{'ingredient_name': ingredient[0].strip(), 'quantity': int(ingredient[1].strip()), 'measure': ingredient[2].strip()}]
        file.readline()


def get_shop_list_by_dishes(dishes: list, person_count: int):
    list_main = []
    ingredient_list = []
    for dish, item in cook_book.items():
        if dish in dishes:
            for name in item:
                list_main.append(name.get('ingredient_name'))
                name.pop('ingredient_name')
                ingredient_list.append(name)
    for i in ingredient_list:
        i['quantity'] *= person_count

    shop_dishes = dict(zip(list_main, ingredient_list))
    return shop_dishes


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


