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
ip_correct = False
while not ip_correct:
    ip = input('Введите ip в формате 10.1.1.1: ')
    ip_list = ip.split('.')
    if (ip_list.count == 4) and (ip_list[0].isdigit() and
        ip_list[1].isdigit() and
        ip_list[2].isdigit() and
        ip_list[3].isdigit()):
        if ip.count('.') == 3:
            if (0 <= int(ip_list[0]) <=255) and (0 <= int(ip_list[1]) <=255) and (0 <= int(ip_list[2]) <=255) and (0 <= int(ip_list[3]) <=255):
                ip_correct = True
            else:
                print('Неправильный IP-адрес')
        else:
            print('Неправильный IP-адрес')
    else:
        print('Неправильный IP-адрес')
    
if 1 <= int(ip_list[0]) <= 223 :
    print('unicast')
elif 224 <= int(ip_list[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
