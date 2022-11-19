def craft_price(item):
    weapons = ('пул', 'пуш', 'дроб', "пулемёт", "дробовик", "пушка")
    cabs = ('каб', 'кабина')
    truster = ('уск', "ускор", "ускоритель")
    fuel = ('бак', "бочка")
    radar = ('радар', "радар", "рубин")
    module = ("радио", "радик", "радиатор", "домкрат")
    wheels = ('колесо', "колёса")

    white_item_crafts = {
        cabs: (75, 15),
        weapons: (30, 6),
        truster: (55, 11),
        fuel: (60, 12),
        radar: (35, 8),
        module: (20, 4),
        wheels: (15, 3)
    }

    for item_set in white_item_crafts:
        if item in item_set:
            craft_needs = white_item_crafts[item_set]  # (scrap, cuprum)

            white_item_price = float(input('Цена белого предмета: '))
            scrap_price = (float(input('Цена металла: ')) * 0.01) * craft_needs[0]
            cuprum_price = (float(input('Цена меди: ')) * 0.01) * craft_needs[-1]

            print('Цена предмета = ', white_item_price)
            print('Цена ресурсов = ', scrap_price + cuprum_price)


craft_price(input('Деталь: '))

