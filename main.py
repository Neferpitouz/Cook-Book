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
            for item in list_ingridients:
                if result.get(item['ingridient name']) == None:
                    result.update({item['ingridient name']: []})
                    result[item['ingridient name']].append({'quantity': item['quantity']})
                    result[item['ingridient name']].append({'measure': item['measure']})
                    quantity = int(result[item['ingridient name']][0]['quantity'])
                    result[item['ingridient name']][0]['quantity'] = quantity * person_count
                else:
                    quantity = int(item['quantity']) * person_count
                    result[item['ingridient name']][0]['quantity'] = quantity

        else:
            print(f'Такого блюда как {dish} нет в поваренной книге')
    return result


pprint(shopping_list(['Запеченный картофель', 'Омлет'], 2))


def sorting(files_list):
    files_str = {}
    for each in files_list:
        with open(each, encoding='utf-8') as file_obj:
            text = file_obj.readlines()
            files_str.update({each: len(text)})
    sorted_dict = {}
    sorted_keys = sorted(files_str, key=files_str.get)
    for w in sorted_keys:
        sorted_dict[w] = files_str[w]
    return sorted_dict


def file_merge(files_name):
    result = []
    for file_name in files_name.keys():
        with open(file_name, encoding='utf-8') as file_obj:
            result.append(f'{file_name}\n')
            text = file_obj.readlines()
            result.append(f'{len(text)}\n')
            for strokes in text:
                result.append(f'{str(strokes)}')
            result.append(f'\n')
    with open('result.txt', 'w', encoding='utf-8') as file_result:
        for each in result:
            file_result.write(each)
    return result


file_merge(sorting(['File 1.txt', 'File 2.txt', 'File 3.txt', 'File 4.txt']))