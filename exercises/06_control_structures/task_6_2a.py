# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



ip = input("Введите ip адрес в формате 10.0.1.1\n")
ip_list = ip.split('.')
valid_ip = len(ip_list) == 4

for num in ip_list:
    valid_ip = num.isdigit() and int(num) >=0 and int(num)<=255 and valid_ip

if valid_ip:
    first_byte = int(ip_list[0])
    if first_byte >= 1 and first_byte <= 223 :
        print('unicast')
    elif first_byte >= 224 and first_byte <= 239 :
        print('multicast')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
else:
    print("Неправильный IP-адрес")
