def type_alcohol(litres):
    price = 1.9
    final_price = 0
    if litres <= 20:
        final_price = litres * price
        discount = final_price * 0.03
        final_price -= discount
    else:
        final_price = litres * price
        discount = final_price * 0.05
        final_price -= discount
    return final_price


def type_gasoline(litres):
    price = 2.5
    final_price = 0
    if litres <= 20:
        final_price = litres * price
        discount = final_price * 0.04
        final_price -= discount
    else:
        final_price = litres * price
        discount = final_price * 0.06
        final_price -= discount
    return final_price


def fuel_station(litres, type):
    if type == "A":
        return type_alcohol(litres)
    else:
        return type_gasoline(litres)


print(fuel_station(21, "A"))
