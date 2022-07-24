item_price = float(input('Цена предмета: '))

scrap_price = float(input('Цена металла:'))
scrap_count = float(input('Кол-во металла для крафта:'))

cuprum_price = float(input('Цена на медь:'))
cuprum_count = float(input('Кол-во меди для крафта:'))

scrap_counter = (scrap_price * 0.01) * scrap_count
cuprum_counter = (cuprum_price * 0.01) * cuprum_count

print('Цена предмета =', item_price)
print('Цена ресурсов =', scrap_counter + cuprum_counter)
print('Разница:', item_price - (scrap_counter + cuprum_counter))
