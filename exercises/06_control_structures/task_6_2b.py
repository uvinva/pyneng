# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    
    ip = input("Введите ip адрес в формате 10.0.1.1\n")
    ip_list = ip.split('.')
    valid_ip = len(ip_list) == 4

    for num in ip_list:
        valid_ip = num.isdigit() and int(num) >=0 and int(num)<=255 and valid_ip
    if valid_ip:
        break
    print("Неправильный IP-адрес")

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
