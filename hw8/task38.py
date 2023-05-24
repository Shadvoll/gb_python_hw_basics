class Record:
    def __init__(self,  index: int, surname: str, name: str, phone_number: str, description: str):
        self.index = int(index)
        self.phone_number = phone_number
        self.surname = surname
        self.name = name
        self.description = description

    def show(self):
        print(self)

    def record_to_csv_format(self):
        return f'{self.index},{self.surname},{self.name},{self.phone_number},{self.description}'

    def __str__(self):
        result = f'ID: {self.index}\n'
        result += f'Фамилия: {self.surname}\n'
        result += f'Имя: {self.name}\n'
        result += f'Телефон: {self.phone_number}\n'
        result += f'Описание: {self.description}\n'
        return result


class Phonebook:
    def __init__(self, phone_book_filename: str = None, records: list = None):
        self.phone_book_filename = phone_book_filename
        self.records = []
        if phone_book_filename is not None:
            self.phone_book_filename = phone_book_filename
            self.records += self.read_csv(phone_book_filename)
        if records is not None:
            self.records += records

    def read_csv(self, filename: str):
        data = []
        with open(filename, 'r', encoding='utf-8') as fin:
            for line in fin:
                record = Record(*line.strip().split(','))
                data.append(record)
        return data

    def write_csv(self):
        with open(self.phone_book_filename, 'w', encoding='utf-8') as fout:
            for elem in self.records:
                fout.write(f'{elem.record_to_csv_format()}\n')

    def write_txt(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as fout:
            fout.write(str(self))

    def search_by_surname(self, surname: str):
        results = [record for record in self.records if record.surname == surname]
        return Phonebook(records=results)

    def search_by_phonenumber(self, phonenumber: str):
        results = [record for record in self.records if record.phone_number == phonenumber]
        return Phonebook(records=results)

    def add_user(self, record: Record):
        self.records.append(record)
        self.write_csv()

    def change_record(self, new_data: Record):
        for idx, record in enumerate(self.records):
            if record.index == new_data.index:
                self.records[idx] = new_data
                self.write_csv()
                return True
        return False

    def remove_user_by_id(self, index):
        for record in self.records:
            if record.index == index:
                self.records.remove(record)
                self.write_csv()
                return True
        return False

    def show_all(self):
        print(self)

    def get_last_index(self):
        return self.records[-1].index

    def is_index_present(self, index):
        return any(record.index == index for record in self.records)

    def show_menu(self) -> int:
        print("\nВыберите необходимое действие:\n"
              "1. Отобразить весь справочник\n"
              "2. Найти абонента по фамилии\n"
              "3. Найти абонента по номеру телефона\n"
              "4. Добавить абонента в справочник\n"
              "5. Изменить запись по id\n"
              "6. Удалить запись по id\n"
              "7. Сохранить справочник в текстовом формате\n"
              "8. Закончить работу")
        choice = int(input())
        return choice

    def work_with_phonebook(self):
        choice = self.show_menu()
        while (choice != 8):
            if choice == 1:
                print(self)
            elif choice == 2:
                name = self.get_surname_from_input()
                print("Результаты поиска: ")
                result_phonebook = self.search_by_surname(name)
                if result_phonebook:
                    print(result_phonebook)
                else:
                    print("Нет результатов")
            elif choice == 3:
                number = self.get_phone_number_from_input()
                print("Результаты поиска: ")
                result_phonebook = self.search_by_phonenumber(number)
                if result_phonebook:
                    print(result_phonebook)
                else:
                    print('Нет результатов')
            elif choice == 4:
                new_index = self.get_last_index() + 1
                record = self.new_record_from_input(new_index)
                self.add_user(record)
            elif choice == 5:
                index = self.get_id_from_input()
                if self.is_index_present(index) is False:
                    print('Такого id нет!')
                else:
                    record = self.new_record_from_input(index)
                    if self.change_record(new_data=record) is True:
                        print('Успех!')
                    else:
                        print('Такого пользователя нет')
                # изменение
            elif choice == 6:
                index = self.get_id_from_input()
                if self.remove_user_by_id(index) is True:
                    print('Успех!')
                else:
                    print('Такого пользователя нет!')
                # удаление
            elif choice == 7:
                filename = self.get_filename_from_input()
                self.write_txt(filename)
            choice = self.show_menu()

    @staticmethod
    def new_record_from_input(index: int):
        record_lst = []
        fields = ["Фамилия", "Имя", "Телефон", "Описание"]
        for field in fields:
            record_lst.append(input(f'Введите {field}: '))
        return Record(index, *record_lst)

    @staticmethod
    def get_surname_from_input():
        return input('Введите Фамилию пользователя: ')

    @staticmethod
    def get_phone_number_from_input():
        return input('Введите телефонный номер пользователя: ')

    @staticmethod
    def get_filename_from_input():
        return input('Введите имя файла для экспорта: ')

    @staticmethod
    def get_id_from_input():
        return int(input('Введите ID пользователя: '))

    def __str__(self):
        result = ''
        for record in self.records:
            result += '\n'
            result += str(record)
            result += '\n'
        return result
    
    def __bool__(self):
        return bool(self.records)


if __name__ == "__main__":
    phonebook = Phonebook("phonebook.csv")
    phonebook.work_with_phonebook()
