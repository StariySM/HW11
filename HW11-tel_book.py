from datetime import datetime, timedelta
from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.n = 0
        self.data = {}
        self.index = 0

    def add_record(self, record):
        self.data.update({record.name.value: record})

    def __iter__(self):
        # print("start __iter__")
        return self

    def __next__(self):
        # print("start __next__")
        if self.index >= len(self.data.keys()):
            raise StopIteration
        key = list(self.data.keys())[self.index]
        self.index += 1
        return key, self.data[key]



    def iterator(self, n):
        # print("start iterator")
        index = 0
        for i in self:
            print(i)
            index += 1
            if index >= n:
                break


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = [phone]
        self.birthday = birthday

    def add(self, new_phone):
        self.phones.append(new_phone)

    def change(self, old_phone, new_phone):
        for i, ph in enumerate(self.phones):
            if ph == old_phone:
                self.phones[i] = new_phone
                break

    def delete(self, old_phone):
        for i, ph in enumerate(self.phones):
            if ph == old_phone:
                self.phones.pop(i)
                break

    def days_to_birthday(self):
        if self.birthday:
            current_birthday_day = datetime(year=datetime.now().year, month=self.birthday.value.month,
                                            day=self.birthday.value.day)
            days_to_birthday = current_birthday_day - datetime.now()
            return days_to_birthday.days


class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass


class Phone(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.isdigit():
            self.__value = value
        else:
            print("telephone number must include only digits")
            self.__value = None


class Birthday(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, '%d.%m.%Y')
        except Exception:
            self.__value = None
            print("date must be in format day.month.year")


# if __name__ == '__main__':
#     name = Name('Bill')
#     phone = Phone('1234567890')
#     rec = Record(name, phone)
#     ab = AddressBook()
#     ab.add_record(rec)
#
#     name = Name('Bill')
#     phone = Phone('1234567890')
#     rec = Record(name, phone)
#     ab = AddressBook()
#     ab.add_record(rec)
#
#     assert isinstance(ab['Bill'], Record)
#     assert isinstance(ab['Bill'].name, Name)
#     assert isinstance(ab['Bill'].phones, list)
#     assert isinstance(ab['Bill'].phones[0], Phone)
#     assert ab['Bill'].phones[0].value == '1234567890'
#     print(name.value)
#     name.value = "Jion"
#     print(name.value)
#
#     print('All Ok)')
#
#
#
#     ab = AddressBook()
#     n1 = Name('Billl')
#     ph1 = Phone('1234567890')
#     rec1 = Record(n1, ph1)
#     ab.add_record(rec1)
#     n2 = Name('Racs')
#     ph2 = Phone('12345678901')
#     rec2 = Record(n2, ph2)
#     ab.add_record(rec2)
#     n3 = Name('Back')
#     ph3 = Phone('12345678901')
#     rec3 = Record(n3, ph3)
#     ab.add_record(rec3)
#     n4 = Name('Jan')
#     ph4 = Phone('12345678901')
#     rec4 = Record(n4, ph4)
#     ab.add_record(rec4)
#     n5 = Name('Jon')
#     ph5 = Phone('12345678901')
#     rec5 = Record(n5, ph5)
#     ab.add_record(rec5)
#
#     ab.iterator(6)
#     ab.iterator(3)
