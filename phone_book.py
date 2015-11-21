#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import pickle
import os


class PhoneBook(object):
    def __init__(self, name):
        self.content = {}
        self.name = name
        self.pikle_file = self.name + '.pikle'
        self.load()

    def load(self):
        if os.path.exists(self.pikle_file):
            open_file = open(self.pikle_file, 'rb')
            self.content = pickle.load(open_file)

    def save(self):
        save_file = open(self.pikle_file, 'wb')
        pickle.dump(self.content, save_file)
        save_file.close()

    def add_contact(self):
        self._input_contact_()

    def del_contact(self, name):
        res = name in self.content
        if res:
            self.content.pop(name)
            return True
        else:
            return False

    def list(self):
        for name, number in self.content.items():
            print(name, '-', number)

    def search_contact(self, name):
        res = name in self.content.keys()
        if res:
            print(name, '- ТЕЛЕФОН: ', self.content.get(name))
        else:
            print(name, '- не найден: ')

    def edit_contact(self, name):
        res = name in self.content.keys()
        if res:
            self.content.pop(name)
            self._input_contact_()
        else:
            print(name, '- не найден: ')

    def _input_contact_(self):
        name = input('ИМЯ : ').title()
        number = input('Телефон : ')
        self.content[name] = number
        print(name, '- запись добавлена')
