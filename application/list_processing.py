from re import sub

def place_data(num_pattern, num_pattern_new, contacts_list):
    contacts_list_new = list()
    for page in contacts_list:
        page_string = ','.join(page) # объединение в строку
        format_page = sub(num_pattern, num_pattern_new, page_string) # замена шаблонов в строке
        page_list = format_page.split(',') # формируем список строк
        contacts_list_new.append(page_list)
        return contacts_list_new
    

def change_phone_format(name_pattern, name_pattern_new):
    contacts_list = list() # создаем список
    for page in place_data:
        page_string = ','.join(page) # объединение в строку
        format_page = sub(name_pattern, name_pattern_new, page_string)
        page_list = format_page.split(',') # формируем список строк
        if page_list not in contacts_list:
            contacts_list.append(page_list)
            return contacts_list

def merge_records():    
# убираем дубликаты
    for i in change_phone_format:
        for j in change_phone_format:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] is '':
                    i[2] = j[2]
                if i[3] is '':
                    i[3] = j[3]
                if i[4] is '':
                    i[4] = j[4]
                if i[5] is '':
                    i[5] = j[5]
                if i[6] is '':
                    i[6] = j[6]
            contact_list = list()
            for page in change_phone_format:
                if page not in contact_list:
                    contact_list.append(page)
            return contact_list