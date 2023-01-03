cook_book_dict = {}  # Create new dict


def get_shop_list_by_dishes(dishes, person_count):
    ingridient_dict = {}
    for dish, ingridients in cook_book_dict.items():
        if dish in dishes:
            for ingridient in ingridients:
                ingridient_dict[ingridient['ingredient_name']] = {
                    "measure": ingridient["measure"],
                    "quantity": (int(ingridient["quantity"]) * person_count),

                }
    return ingridient_dict



with open('recipes.txt', 'a', encoding='utf-8') as file:  # open file
    data = file.read()  # закидываем в переменную весь файл
    list_recipes = data.split('\n\n')  # Сплитуем по \n\n
    # print(len(list_recipes))
    for dish in list_recipes:
        # print(dish)
        items_dish = dish.split('\n')
        # print(items_dish)
        cook_book_dict[items_dish[0]] = []
        # print(cook_book_dict)
        ingredients_list = items_dish[2:]
        for ingridient in ingredients_list:
            items_ingridient = ingridient.split('|')
            # print(items_ingridient)
            ingr_to_insert = {
                'ingredient_name': items_ingridient[0],
                'quantity': items_ingridient[1],
                'measure': items_ingridient[2],
            }
            cook_book_dict[items_dish[0]].append(ingr_to_insert.copy())
print(cook_book_dict)

