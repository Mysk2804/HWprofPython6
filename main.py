documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def command_people(doc, number):
    for number_doc in doc:
        if number_doc['number'] == number:
            print(f'{number_doc["name"]}, владелец данного документа.')
            return True
    print('Человека с таким документом не существует.')
    return False



def command_shelf(directories, nabor_polki):
    for number_keys, nomber_values in directories.items():
        for nomber_val in nomber_values:
            if nomber_val == nabor_polki:
                print(number_keys)
                return True
    print('Нет такого документа.')
    return False



def command_list(doc):
    for list_ in doc:
        print(f'{list_["type"]} "{list_["number"]}" "{list_["name"]}"')
        return True



def command_add(add, shel, tipe: str, number: str, name: str, shelf: str):
    # tipe = input('Введите название документа: ')
    # number = input('Введите номер документа: ')
    # name = input('Введите Имя и Фамилию: ')
    # shelf = input('Введите номер полки: ')
    if int(shelf) <= len(shel):
        documents_ = {"type": tipe, "number": number, "name": name}
        shel[shelf].append(number)
        add.append(documents_)
        print(f'Человек по имени {name} успешно добавлен в базу.')
        return True
    else:
        print('Данной полки не существует, данные не записаны.')
        return False



def command_delete(documents, directories, number: str):
    for doc in documents:
        if doc["number"] == number:
            doc["number"] = ''
            for keys, val in directories.items():
                for i in val:
                    if i == number:
                        val.remove(number)
                        directories[keys] = val
                        return f'Документ {number} был удален с базы'
    return 'Такого документа в базе нет'



# print("Команды для вополнения программы: ")
# print('p - people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
# print('s - shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
# print('l - list – команда, которая выведет список всех документов')
# print(
#     'a - add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
# print()
#
#
# def command(doc, derectories):
#     while True:
#         command_ = input('Введите команду: ')
#         if command_ == 'p':
#             command_people(documents, "10006")
#         elif command_ == 's':
#             command_shelf(directories, "10006")
#         elif command_ == 'l':
#             command_list(documents)
#         elif command_ == 'a':
#             command_add(documents, directories, "pasport", "10006", "Oleg Olegovski", "3")
#         elif command_ == 'd':
#             command_delete(documents, derectories, "10006")
#         elif command_ == 'q':
#             print ('Выход')
#             return

if __name__ == '__main__':
    command_add(documents, directories, "pasport", "10006", "Oleg Olegovski", "3")
    command_list(documents)
    command_people(documents, "10006")
    command_shelf(directories, "10006")