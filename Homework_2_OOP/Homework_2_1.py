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

print(f'cook_book = {cook_book}')