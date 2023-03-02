color1 = 'красный'
color2 = 'синий'
color3 = 'желтый'
a = input('Введите первый цвет: ')
b = input('Введите второй цвет: ')
if (a != color1 and a != color2 and a != color3) and (b != color1 and b != color2 and b != color3):
    print('Цвета введены неправильно')
else:
    if ((a == color1) and (b == color2)) or ((a == color2) and (b == color1)):
        print('фиолетовый')
    elif ((a == color1) and (b == color3)) or ((a == color3) and (b == color1)):
        print('оранжевый')
    elif ((a == color2) and (b == color3)) or ((a == color3) and (b == color2)):
        print('зеленый')
