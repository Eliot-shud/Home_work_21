from courier import Courier
from request import Request
from shop import Shop
from store import Store
from exceptions import CourierError, RequestError


store = Store(items=[])
shop = Shop(items=[])

store.items = {
    'печенька': 25,
    'круасаны': 25,
    'елка': 25,
    'пончик': 3,
    'зонт': 5,
    'ноутбук': 1,
}

shop.items = {
     'печенька': 4,
     'собачка': 2,
     'елка': 1,
     'зонт': 1,
     'пончик': 1,
}

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nДобрый день!\n')

    while True:
        # вывод содержимого складов
        for storage in storages:
            print(f'Сейчас в {storage}:\n {storages[storage].items}')

        # ввод от пользователя
        user_input = input(
            'Введите запрос в формате "Достать 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )

        if user_input in ('stop', 'стоп'):
            break

        # ввод пользователя
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        # доставляем товар
        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except CourierError as error:
            print(error.message)


if __name__ == '__main__':
    main()