from exceptions import InvalidRequest, InvalidStorageName


class Request:

    def __init__(self, request, storages):

        # разделяем строку по пробелам
        splitted_request = request.lower().split(' ')

        # если элементов не 7, выводим ошибку
        if len(splitted_request) != 7:
            raise InvalidRequest

        # вносим значения в атрибуты класса
        self.amount = int(splitted_request[1])
        self.product = splitted_request[2]
        self.departure = splitted_request[4]
        self.destination = splitted_request[6]

        # проверяем пункты отправки и назначения существуют
        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName