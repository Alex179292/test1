
def total_revenue(purchases):
    print(f"Общая выручка: {sum([x['price']*x['quantity'] for x in purchases])}")


def items_by_category(purchases):
    categories = list(set(items['category'] for items in purchases ))
    item_dict={}
    for x in categories:
        for y in purchases:
            if y['category']==x:
                item_dict.setdefault(x, []).append(y['item'])
    print(f"Товары по категориям: {dict(sorted(item_dict.items(),reverse=True))}")


def expensive_purchases(purchases, min_price):
    print(f"Покупки дороже {min_price}: {[x for x in purchases if x['price']>min_price]}")


def average_price_by_category(purchases):
    categories = list(set(items['category'] for items in purchases ))
    item_dict={}
    for x in categories:
        for y in purchases:
            if y['category']==x:
                item_dict.setdefault(x, []).append(y['price'])
    print(f"Средняя цена по категориям: {dict(sorted({x:(sum(item_dict[x])/len(item_dict[x])) for x in item_dict.keys()}.items(),reverse=True))}")


def most_frequent_category(purchases):
    item_dict = {}
    for x in purchases:
        item_dict.setdefault(x['category'], []).append(x['quantity'])
    item_dict = sorted({key:sum(map(lambda x: x,item_dict[key])) for key in item_dict}.items(), key=lambda item: item[1])[-1][0]
    print(f"Категория с наибольшим количеством проданных товаров: {item_dict}")

total_revenue (purchases)
items_by_category(purchases)
expensive_purchases(purchases,1.0)
average_price_by_category(purchases)
most_frequent_category(purchases)