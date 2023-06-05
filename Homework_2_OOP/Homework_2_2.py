with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for name_dishes in file:
        number_ingredients = int(file.readline())
        ingredients = []
        for i in range(number_ingredients):
            name_ingredient, amount, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': name_ingredient,
                'quantity': amount,
                'measure': measure
            })
        file.readline()
        cook_book[name_dishes.strip()] = ingredients

# print(f'cook_book = {cook_book}')

def get_shop_list_by_dishes(dishes, person_count):
    list = {}
    for dish in dishes:
        if dish in cook_book:
            for composition in cook_book[dish]:
                if composition['ingredient_name'] in list:
                    list[composition['ingredient_name']]['quantity'] += int(composition['quantity']) * person_count
                else:
                    list[composition['ingredient_name']] = {'measure': composition['measure'],
                                                  'quantity': (int(composition['quantity']) * person_count)}
        else:
            print('В меню блюда в "СТОПЕ"')
    print(list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)