# working with csv files - code snippets
import csv
# standard way of wreading csv file
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)  # print(line[2]) will get us only the emails

# some separation
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip the first row (['first_name', 'last_name', 'email'])
    for line in csv_reader:
        print(line[1], line[1], line[2])  # print(line[2]) will get us only the emails


# write to csv file - make a copy but use tabs instead of commas
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('new_data.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)


# working with csv data using DictReader and DictReader
# Reading csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['email']) # print(line) - all rows as OrderedDict

# DictWriter - reading and then writing to a csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_data_2.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)


# DictWriter - reading and then writing to a csv
# remove some data. First remove email fieldnames and then email key from writer orderedDict
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_data_3.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name'] #1
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email'] # gets rid of email col
            csv_writer.writerow(line)

