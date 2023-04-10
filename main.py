# 1. Открыть файл
# 2. Сохранить файл
# 3. Просмотреть контакты +
# 4. Создать контакт +
# 5. Найти контакт +
# 6. Изменить контакт +
# 7. Удалить контакт +
# 8. Выход +

# Главное меню

# import readfile

# def readfile():


def main_menu():
    print("Главное меню PHONE_BOOK")
    print("1.Показать всю книгу")
    print("2.Создать контакт")
    print("3.Редактировать запись")
    print("4.Поиск контакта")
    print("5.Удалить контакт")
    print("6.Вернуться в главное меню")


# menu = main_menu()


# Пункт 1. Показать всю книгу(+)
def show_all_contacts():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close
    for i in data:
        print(i)


# show_contacts = show_all_contacts()


# Пункт 2. Добавить новую запись(+)

def add_new_contact():
    file = open('sample.txt', 'a', encoding='UTF-8')
    data = input("\nВведите ФИО, номер телефона, комментарий через символ (;)")
    data += '\n'
    file.write(data)



# Пункт 3.Редактировать запись

def edit_contact():
    find_string = input("Введите поисковый запрос:")
    replace_string =input("Введите обновленные данные: ")
    file = open('sample.txt', 'w', encoding='UTF-8')
    data = file.readlines()
    new_data = []
    for data_str in data:
        if find_string in data_str:
            print("found data = ", data_str)
            new_data.append(replace_string)
        else:
            new_data.append(data_str)
    file.close
    file = open('sample.txt', 'w', encoding='UTF-8')


# Пункт 4. Поиск контакта(+)
def find_contact():
    find_string = input("Введите поисковый запрос: ")
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for index, data_str in enumerate(data):
        if find_string in data_str:
            print("found data = ", data_str)
    

# Выбор кнопки меню. Консоль управления
if __name__ == "__main__":
    main_menu()
    while True:
        botton = int(input("Введите пункт меню: "))
        if botton == 1:
            show_all_contacts()
        if botton == 2:
            add_new_contact()
        if botton == 3:
            edit_contact()
        if botton == 4:
            find_contact()
