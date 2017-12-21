import csv
from attempt.database_methods import *

# get data and populate db
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        insert(line['first_name'], line['last_name'], line['email'])


by_last_name = get_by_lastname('Wright')
by_email = get_by_email('samjenkins@bogusemail.com')
print(by_last_name)
print(by_email)
update_email('Sam', 'Jenkins', 'samj@abv.bg')
by_email = get_by_email('samj@abv.bg')
print(by_email)
remove_donor('john-doe@bogusemail.com')
print(get_all())
