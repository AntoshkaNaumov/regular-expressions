import csv

def reading_csv_file():
  # читаем адресную книгу в формате CSV в список contacts_list
  with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list

def writing_csv_file(contact_list):
# код для записи файла в формате CSV
  with open('phonebook.csv', 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contact_list)