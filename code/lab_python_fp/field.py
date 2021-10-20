def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for dictionary in items:
            note = dictionary.get(args[0])
            if note is not None:
                yield note
    else:
        for d in items:
            dictionary = dict()
            for key in args:
                note = d.get(key)
                if note is not None:
                    dictionary[key] = note
            if len(dictionary) != 0:
                yield dictionary


if __name__ == '__main__':

    a1 = list()
    a2 = list()

    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    ]

    for i in field(goods, 'title'):
        a1.append(i)
    print(a1)

    for i in field(goods, 'title', 'price'):
        a2.append(i)
    print(a2)