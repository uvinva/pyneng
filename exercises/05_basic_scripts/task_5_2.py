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

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network = input('Введите адрес сети: ')
network_list = network.split('/')
ip = network_list[0].split('.')
mask = int(network_list[1])
mask_bin = '1' * mask + '0' * (32-mask)
mask_oct1 = int(mask_bin[0:8],2)
mask_oct2 = int(mask_bin[8:16],2)
mask_oct3 = int(mask_bin[16:24],2)
mask_oct4 = int(mask_bin[24:32],2) 
ip0 = int(ip[0])
ip1 = int(ip[1])
ip2 = int(ip[2])
ip3 = int(ip[3])
template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''
print(template.format(ip0,ip1,ip2,ip3,mask,mask_oct1,mask_oct2,mask_oct3,mask_oct4))