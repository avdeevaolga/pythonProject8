import os


# Задание 1

def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as file_recipes:
        cook_book = {}
        for line in file_recipes:
            dish = line.strip()
            ingredients_list = []
            ingredients_quantity = file_recipes.readline()
            for a in range(int(ingredients_quantity)):
                ingredient_name, quantity, measure = file_recipes.readline().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[dish] = ingredients_list
            file_recipes.readline()
    return cook_book


# print(get_cook_book())

# Задание 2


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_dict = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for recipe in cook_book[dish]:
                if recipe['ingredient_name'] in shop_dict:
                    shop_dict[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count
                else:
                    shop_dict[recipe['ingredient_name']] = {'measure': recipe['measure'], 'quantity': (recipe['quantity'] * person_count)}
        else:
            error = 'Данного блюда нет в нашем меню'
            return error
    return shop_dict


# print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 50))

