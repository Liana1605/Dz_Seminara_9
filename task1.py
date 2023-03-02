class phone_book:
    """"Телефонный справочник"""
    emp_count = 0

    def __init__(self, name, number, type):
        self.name = name
        self.number = number
        self.type = type
        phone_book.emp_count += 1

    def display_count(self):
        print('Всего номеров: %d' % phone_book.emp_count)

    def display_phone_book(self):
        print('Имя: {}, Контакт: {}, Тип: {}'.format(self.name, self.number, self.type))

# Это создаст первый объект класса Employee  
emp1 = phone_book('Анжела', 79105862777, 'мобильный')  
# Это создаст второй объект класса Employee  
emp2 = phone_book('Дмитрий', 79506563233, 'домашний')  
emp1.display_phone_book()  
emp2.display_phone_book()  
print("Всего сотрудников: %d" % phone_book.emp_count)    