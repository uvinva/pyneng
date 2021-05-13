# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
prefix = ospf_route.split()[0]
ad_metric = ospf_route.split()[1].strip('[]')
next_hop = ospf_route.split()[3].split(',')[0]
last_update = ospf_route.split()[4].split(',')[0]
outbound_int = ospf_route.split()[5]
ospf_route_template = '''
Prefix                {0:<15}
AD/Metric             {1:<15}
Next-Hop              {2:<15}
Last update           {3:<15}
Outbound Interface    {4:<15}
'''
print(ospf_route_template.format(prefix,ad_metric,next_hop,last_update,outbound_int))
