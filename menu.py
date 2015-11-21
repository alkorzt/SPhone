#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from phone_book import PhoneBook

# Константы
PHONE_BOOK_NAME = 'main'
LINE = '=========================================================='


class Menu(object):
    @staticmethod  # Декоратор статического метода
    def menu_entries():
        pb = PhoneBook(PHONE_BOOK_NAME)
        print(LINE)
        print('Телефонная книга 0.1')

        while True:
            print(LINE)
            print('Вводите команду, h - справка, q - выход')

            choose = input()

            if choose.lower() in ['a']:
                pb.add_contact()
            elif choose.lower() in ['e']:
                name = input('Какую запись вы хотите редактировать (ИМЯ): ').title()
                pb.edit_contact(name)
            elif choose.lower() in ['s']:
                name = input('Какую запись вы хотите найти (ИМЯ): ').title()
                pb.search_contact(name)
            elif choose.lower() in ['d']:
                name = input('Какую запись вы хотите удалить (ИМЯ): ').title()
                res = pb.del_contact(name)
                if res:
                    print(name, ' - запись была успешно удалена')
                else:
                    print('ОШИБКА: Имени нет в базе')
            elif choose.lower() in ['l']:
                pb.list()
            elif choose.lower() in ['h']:
                print('''\
                МЕНЮ КОМАНД:
    ======================================
    a(Add)      - Добавить запись в книгу
    e(Edit) -   - Редактирование записи
    s(Search)   - Поиск контакта
    d(Delete)   - Удаление контакта
    h(Help)     - Показать эту справку
    l(List)     - Отобразить все контакты отсортированные по алфавиту
    q(Quit)     - Выход из программы''')
            elif choose.lower() in ['q']:
                print('Завершение работы программы')
                pb.save()
                raise SystemExit
            else:
                print('Команда не распознана')
