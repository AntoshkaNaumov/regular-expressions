from re import sub, findall
from application.working_file import reading_csv_file, writing_csv_file

def merge_records(record_one, record_two):
    '''Функция убирающая дубли'''
    result = list()
    for index in range(len(record_one)):
        result.append(record_one[index]) if record_one[index] else result.append(record_two[index])
    return result

num_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
num_pattern_new = r'+7(\2)-\3-\4-\5 \6\7'

contacts_list = reading_csv_file() # вызываем функцию чтения файла

contacts = list()
for row in contacts_list:
    record = list()
    complete_name = findall(r'(\w+)', ' '.join(row[:3])) # возращает список совпадений, в качестве параметра используем строку полученную с помощью join 
    #print(row)
    complete_name.append('') if len(complete_name) < 3 else ...
    #print(complete_name)
    record += complete_name
    record.append(row[3])
    record.append(row[4])
    record.append(sub(num_pattern, num_pattern_new, row[5]).strip()) # возвращает строку, полученную путем замены 
    record.append(row[6])
    contacts.append(record)

#print(contacts)

contact_dict = dict()
for item in contacts:
    contact_dict[item[0]] = merge_records(item, contact_dict[item[0]]) if item[0] in contact_dict else item

writing_csv_file(contact_dict.values()) # вызов функции записи в файл

