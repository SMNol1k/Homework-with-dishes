import os
import pprint as pprint

cook_book = {}
with open("files/cook.txt", "r", encoding="utf-8") as f:
    sp_list = f.read().split("\n\n")
    for i in sp_list:
        sp_dish = i.split("\n")
        for j in range(2, len(sp_dish)):
            value_out = sp_dish[j].split(" | ")
            value = {}
            value['ingredient_name'] = value_out[0]
            value['quantity'] = int(value_out[1])
            value['measure'] = value_out[2]
            if sp_dish[0] in cook_book:
                cook_book[sp_dish[0]].append(value)
            else:
                cook_book[sp_dish[0]] = [value]

pprint.pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
pprint.pprint(shop_list)
