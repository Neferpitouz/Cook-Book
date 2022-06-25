from pprint import pprint

file_name = 'example.txt'


def cook_book_from_file(file):
    with open(file, encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            meal_name = line.strip()
            cook_book.update({meal_name: []})
            for item in range(int(file_obj.readline())):
                features = file_obj.readline().strip()
                res = features.split(' | ')
                cook_book[meal_name].append({'ingridient name': res[0], 'quantity': res[1], 'measure': res[2]})

            file_obj.readline()
    return cook_book


# pprint(cook_book_from_file(file_name))


def shopping_list(dishes, person_count):
    cook_book = cook_book_from_file(file_name)
    result = {}
    for dish in dishes:
        if dish in cook_book:
            list_ingridients = cook_book[dish]

        else:
            print(f'Такого блюда как {dish} нет в поваренной книге')
    return result


print(shopping_list(['Фахитос', 'Омлет'], 3))