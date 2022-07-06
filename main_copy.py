from re import sub
from application.working_file import reading_csv_file, writing_csv_file

contacts_list = reading_csv_file()

num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                  r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                  r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    
num_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page) # объединение в строку
  format_page = sub(num_pattern, num_pattern_new, page_string) # замена шаблонов в строке
  page_list = format_page.split(',') # формируем список строк
  contacts_list_new.append(page_list)
  #print(contacts_list_new)
    
name_pattern = r'^(\w+)(\s*)(\,?)(\w+)' \
                   r'(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = list() # создаем список
for page in contacts_list_new:
  page_string = ','.join(page) # объединение в строку
  format_page = sub(name_pattern, name_pattern_new, page_string)
  page_list = format_page.split(',') # формируем список строк
  if page_list not in contacts_list:
    contacts_list.append(page_list)
    #print(contacts_list)
    
# убираем дубликаты
for i in contacts_list:
  for j in contacts_list:
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
    for page in contacts_list:
      if page not in contact_list:
        contact_list.append(page)
    #print(contact_list)```

writing_csv_file(contact_list)
