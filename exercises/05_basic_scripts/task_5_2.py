# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network_address = input("Введите IP-сеть в формате: 10.1.1.0/24\n")
network = network_address.split('/')[0].split('.')
mask = network_address.split('/')[1]
mask_bin = '1' * int(mask) + '0' * (32-int(mask))
template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{8}
{4:<10}{5:<10}{6:<10}{7:<10}
{4:08b}  {5:08b}  {6:08b}  {7:08b}'''
print(template.format(int(network[0]), int(network[1]), int(network[2]), int(network[3]), int(mask_bin[0:8],2), int(mask_bin[8:16],2), int(mask_bin[16:24],2), int(mask_bin[24:],2),mask))
