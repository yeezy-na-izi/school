# Вариант 9
import pickle
import os


class Books:
    def __init__(self, name, name_of_book, initial, surname, year, ves):
        self.name = name
        self.name_of_book = name_of_book
        self.initial = initial
        self.surname = surname
        self.year = int(year)
        self.izdatelstvo = ves

    def __str__(self):
        return f'{self.name} {self.surname} {self.year} {self.izdatelstvo} {self.name_of_book} {self.initial}'


def zagruzit(dum):
    with open(search_file(), 'wb') as f:
        pickle.dump(dum, f)


def download():
    with open(search_file(), 'rb') as f:
        for_print = pickle.load(f)
        return for_print


def sort_by_name(list_books):
    return sorted(list_books, key=lambda book: book.name)


def sort_by_surname(list_books):
    return sorted(list_books, key=lambda book: book.surname)


def search_file():
    for block in os.walk(os.getcwd()):
        for j in block[2]:
            if '.dat' in j:
                return j


print('Команда "print" выводит не сортированный вариант')
print('Команда "sort print surname" выводит сортированный вариант по фамилии автора')
print('Команда "sort print name" выводит сортированный вариант по названию книги')
print('Команда "load" загружает новую запись в список')
print('Команда "search" выполняет поиск')
print('Команда "rename" переименновывает файл')
while True:
    z = input()
    if z == 'print':
        for i in download():
            print(i)
    elif z == 'correct':
        q = download()
        r = int(input('Введите индекс'))
        a = input('Введите продукт ').split()
        q[r - 1] = Books(a[0], a[1], a[2], a[3])
        zagruzit(q)
    elif z == 'sort print surname':
        for i in sort_by_surname(download()):
            print(i)
    elif z == 'sort print name':
        for i in sort_by_name(download()):
            print(i)
    elif z == 'load':
        print('Напишите запись в формате')
        print('<author_name> <name_of_book> <initial_of_author> <surname> <year> <izdatelstvo>')
        try:
            text = input().split()
            q = download()
            q.append(Books(text[0], text[1], text[2], text[3], text[4], text[5]))
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
        os.rename(search_file(), f'{x}.dat')
        print('Название успешно изменено')
    elif z == 'delete':
        x = int(input('Введите порядковый номер '))
        q = download()
        q.pop(x - 1)
        zagruzit(q)
    else:
        print('Неизвестная команда')
