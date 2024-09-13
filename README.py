# def is_close(file_):
#     if file_.closed:
#         print('Файл закрыт')
#     else:
#         print('Файл открыт')

with open ('recipes.txt', encoding = "utf-8") as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        number_ingredients = int(file.readline())
        products = []
        for _ in range(number_ingredients):
            product = file.readline().strip()
            ingredient_name, quantity, measure = product.split(' | ')
            products.append({'ingredient': ingredient_name,
                             'quantity': quantity,
                             'measure': measure})
        file.readline()
        cook_book[name_dish] = products

#print(cook_book)

def list_of_stores_with_ingredients(dishes, person_count):
    list_products = { }
    for dish in dishes:
        if dish in cook_book:
          for ing in cook_book[dish]:
              ing_name = ing.get('ingredient')
              quantity = int(ing.get('quantity')) * person_count
              measure = ing.get('measure')
              if ing_name in list_products:
                  quantity += list_products[ing_name]['quantity']
              list_products[ing_name] = {'quantity':quantity, 'measure': measure}
        else:
            print (f'Блюда {dishes=} нет в книге рецептов')
    print(list_products)

list_of_stores_with_ingredients(['Омлет', 'Фахитос'], 4)



