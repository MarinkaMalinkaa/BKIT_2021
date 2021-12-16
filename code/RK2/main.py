# используется для сортировки
from operator import itemgetter


class Comp:
    """Компьютер"""
    def __init__(self, id, brand, price, disp_cls_id):
        self.id = id
        self.brand = brand
        self.price = price
        self.disp_cls_id = disp_cls_id


class Disp_cls:
    """Дисплейный класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompDisp_cls:
    """
    'Компьютеры дисплейного класса' для реализации
    связи многие-ко-многим
    """
    def __init__(self, disp_cls_id, comp_id):
        self.disp_cls_id = disp_cls_id
        self.comp_id = comp_id


# Дисплейные классы
disp_classes = [
    Disp_cls(1, 'А-класс'),
    Disp_cls(2, 'Б-класс'),
    Disp_cls(3, 'В-класс'),
    Disp_cls(11, 'Г-класс'),
    Disp_cls(22, 'Д-класс'),
    Disp_cls(33, 'Е-класс'),

]

# Компьютеры
comps = [
    Comp(1, 'HP', 1168390, 1),
    Comp(2, 'Asus', 55390, 1),
    Comp(3, 'ThinkPad',78940, 3),
    Comp(4, 'Acer', 97450, 2),
    Comp(5, 'Lenovo', 86980, 3),
]

# Компьютеры и Дисплейные классы для связи многие-ко-многим
comps_disp_classs = [
    CompDisp_cls(1, 1),
    CompDisp_cls(1, 2),
    CompDisp_cls(3, 3),
    CompDisp_cls(2, 4),
    CompDisp_cls(3, 5),

    CompDisp_cls(33, 1),
    CompDisp_cls(22, 2),
    CompDisp_cls(11, 3),
    CompDisp_cls(33, 4),
    CompDisp_cls(22, 5),
]

def first_task(one_to_many):
    task1 = []
    for brand, price, name in one_to_many:
        if brand[0] == "A":
            task1.append((brand, name))
    return task1


def second_task(one_to_many):
    task2_uns = []
    for c in disp_classes:
        # все компьютеры
        d_disp_cls = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(d_disp_cls) > 0:
            c_price = [price for _, price, _ in d_disp_cls]
            c_minPrice = min(c_price)
            task2_uns.append((c.name, c_minPrice))
    task2 = sorted(task2_uns, key=itemgetter(1))
    return task2


def third_task(many_to_many):
    task3_uns = []
    for brand, price, name in many_to_many:
        task3_uns.append((brand, name))

    task3 = list(sorted(task3_uns, key=itemgetter(0)))
    return task3


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.brand, c.price, d.name)
                   for d in disp_classes
                   for c in comps
                   if c.disp_cls_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, dc.disp_cls_id, dc.comp_id)
                         for d in disp_classes
                         for dc in comps_disp_classs
                         if d.id == dc.disp_cls_id]

    many_to_many = [(c.brand, c.price, disp_class_name)
                    for disp_class_name, disp_cls_id, comp_id in many_to_many_temp
                    for c in comps if c.id == comp_id]

    print('\nЗадание 1 \n', first_task(one_to_many))
    print('\nЗадание 2 \n', second_task(one_to_many))
    print('\nЗадание 3 \n', third_task(one_to_many))

if __name__ == '__main__':
    main()
