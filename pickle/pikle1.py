# Вариант 9
import pickle
import os


class Pickle:
    def __init__(self, surname, name, phone, date):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.date = date

    def __str__(self):
        return f'{self.surname} {self.name} {self.phone} {self.date}'


def zagruzit(dum):
    with open(search_file(), 'wb') as f:
        pickle.dump(dum, f)


def download():
    with open(search_file(), 'rb') as f:
        for_print = pickle.load(f)
        return for_print


def sort_by(list_friends):
    return sorted(list_friends, key=lambda x: int(x.date.split(':')[2] + x.date.split(':')[1] + x.date.split(':')[0]))


def search_file():
    for i in os.walk(os.getcwd()):
        for j in i[2]:
            if '.pickle' in j:
                return j


print('Команда "print" выводит не сортированный выриант')
print('Команда "sort print" выводит сортированный выриант')
print('Команда "load" загружает новую запись в список')
print('Команда "search" выполняет поиск')
print('Команда "rename" переименновывает файл')
while True:
    z = input()
    if z == 'print':
        for i in download():
            print(i)
    elif z == 'sort print':
        for i in sort_by(download()):
            print(i)
    elif z == 'load':
        print('Напишите запись в формате')
        print('<name> <surname> <phone number> <date(через двоеточие)>')
        try:
            text = input().split()
            q = download()
            q.append(Pickle(text[0], text[1], int(text[2]), text[3]))
            zagruzit(q)
            print('Записал')
        except:
            print('Что-то не работает')
    elif z == 'search':
        x = input('Кого хотите найти? ')
        q = []
        for i in download():
            if x in str(i):
                q.append(i)
        if q:
            for i in q:
                print(i)
        else:
            print('Не удалось найти')
    elif z == 'rename':
        x = input('Введите имя: ')
        os.rename(search_file(), f'{x}.pickle')
        print('Название успешно изменено')
    else:
        print('Неизвестная команда')
