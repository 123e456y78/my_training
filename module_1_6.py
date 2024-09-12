my_dict = {'Илья': 2004, 'Вика': 2001}
print('Словарь:', my_dict)
print('Год рождения Илья:', my_dict['Илья'])
print('Год рождения Маша:', my_dict.get('Маша', 'нет такого ключа'))
my_dict['Маша'] = 2004
my_dict.get ('Саша', 2006)
removed_year = my_dict.pop('Вика')
print('Значение удалённого элемента \'Вика\':', removed_year)
print('Изменённый словарь:', my_dict)
print()
my_set = {23,23, 'Арбуз','Арбуз', 4.13, 4.13}
print('Множество:', my_set)
my_set.add('Малина')
my_set.add(36)
my_set.remove (4.13)
print('Изменённое множество:', my_set)
